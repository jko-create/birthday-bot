import csv, io, os, datetime, requests, jdatetime, random

t = datetime.date.today()
j = jdatetime.date.fromgregorian(date=t)

r = requests.get(os.environ["SHEET_URL"])
rows = csv.DictReader(io.StringIO(r.content.decode("utf-8")))

for p in rows:
    try:
        y, m, d = int(p["year"]), int(p["month"]), int(p["day"])
    except (ValueError, KeyError):
        continue
        
    is_shamsi = p["cal"].strip() == "شمسی"
    today_month, today_day = (j.month, j.day) if is_shamsi else (t.month, t.day)
    current_year = j.year if is_shamsi else t.year
    
    if (m, d) == (today_month, today_day):
        age = current_year - y
        age_text = f" ({age})" if age > 0 else ""
        
        messages = [
            f"🚨 Level up alert! Happy Birthday to {p['name']}{age_text}! Keep being awesome. 🔥🥂",
            f"🎉 Massive happy birthday to {p['name']}{age_text}! Cheers to another great year ahead. Let's celebrate! 🥳🎂",
            f"✨ Wishing a fantastic birthday to {p['name']}{age_text}! Here's to health, happiness, and an amazing year. 🍷",
            f"🎂 Another trip around the sun! Happy Birthday {p['name']}{age_text}! Have an absolute blast today! 💥"
        ]
        
        random_msg = random.choice(messages)
        
        response = requests.post(
            f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage",
            json={"chat_id": os.environ["CHAT_ID"],
                  "text": random_msg})
                  
        print(f"Telegram Response for {p['name']}:", response.text)
