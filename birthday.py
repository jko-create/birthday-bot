import csv, io, os, datetime, requests, jdatetime, random

print("🤖 Bot is starting...")
t = datetime.date.today()
j = jdatetime.date.fromgregorian(date=t)
print(f"📅 Today (Miladi): {t.month}/{t.day}")
print(f"📅 Today (Shamsi): {j.month}/{j.day}")

try:
    r = requests.get(os.environ["SHEET_URL"])
    # استفاده از utf-8-sig برای جلوگیری از مشکلات فاصله‌های پنهان
    rows = list(csv.DictReader(io.StringIO(r.content.decode("utf-8-sig"))))
    print(f"📊 Found {len(rows)} rows in the sheet.")
except Exception as e:
    print(f"❌ Error reading sheet: {e}")
    rows = []

for p in rows:
    name = p.get("name", "Unknown").strip()
    if not name: 
        continue
        
    print(f"👤 Checking person: {name}")
    try:
        y, m, d = int(p["year"]), int(p["month"]), int(p["day"])
    except Exception as e:
        print("   ⚠️ Skipped: Empty or invalid numbers in sheet.")
        continue
        
    cal_type = str(p.get("cal", "")).strip()
    is_shamsi = (cal_type == "شمسی")
    
    today_month, today_day = (j.month, j.day) if is_shamsi else (t.month, t.day)
    current_year = j.year if is_shamsi else t.year
    
    print(f"   🗓 Target Date: {m}/{d} ({cal_type}) | Matches Today? {(m, d) == (today_month, today_day)}")
    
    if (m, d) == (today_month, today_day):
        age = current_year - y
        age_text = f" ({age})" if age > 0 else ""
        
        messages = [
            f"🚨 Level up alert! Happy Birthday to {name}{age_text}! Keep being awesome. 🔥🥂",
            f"🎉 Massive happy birthday to {name}{age_text}! Cheers to another great year ahead. Let's celebrate! 🥳🎂",
            f"✨ Wishing a fantastic birthday to {name}{age_text}! Here's to health, happiness, and an amazing year. 🍷"
        ]
        
        funny_quotes = [
            "Old enough to know better, but still young enough to do it anyway! 😈🍻",
            "Another year of making highly questionable decisions together! Let's go! 🚀😂",
            "You’re one year older, but definitely not any wiser! 🧠🤷‍♂️"
        ]
        
        final_text = random.choice(messages) + "\n\n" + random.choice(funny_quotes)
        
        print("   🚀 Sending message to Telegram...")
        response = requests.post(
            f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage",
            json={"chat_id": os.environ["CHAT_ID"], "text": final_text})
                  
        print("   ✅ Telegram Response:", response.text)
        
print("🏁 Bot finished.")
