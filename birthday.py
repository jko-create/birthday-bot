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
        
        # 8 پیام اصلی و پرانرژی
        messages = [
            f"🚨 Level up alert! Happy Birthday to {p['name']}{age_text}! Keep being awesome. 🔥🥂",
            f"🎉 Massive happy birthday to {p['name']}{age_text}! Cheers to another great year ahead. Let's celebrate! 🥳🎂",
            f"✨ Wishing a fantastic birthday to {p['name']}{age_text}! Here's to health, happiness, and an amazing year. 🍷",
            f"🎂 Another trip around the sun! Happy Birthday {p['name']}{age_text}! Have an absolute blast today! 💥",
            f"🥂 Happy Birthday {p['name']}{age_text}! Time to celebrate the legend that you are. Have an epic one! 👑🎉",
            f"🎈 Huge birthday shoutout to {p['name']}{age_text}! Hope your day is as iconic as you are. Let’s party! 🍻✨",
            f"🥳 Happy Birthday {p['name']}{age_text}! Wishing you 365 days of good vibes and unforgettable moments. 🚀",
            f"🔥 It’s {p['name']}’s day! Happy Birthday{age_text}! Ready to make some epic memories today? 🍹🎊"
        ]
        
        # 9 تیکه طنز جوان‌پسند
        funny_quotes = [
            "Old enough to know better, but still young enough to do it anyway! 😈🍻",
            "Another year of making highly questionable decisions together! Let's go! 🚀😂",
            "You’re one year older, but definitely not any wiser! 🧠🤷‍♂️",
            "Happy birthday to someone who is still young enough to blame their mistakes on their youth! 🤪🎉",
            "Here’s to pretending we have our lives together for another year! 🥂🤡",
            "Officially adding another year of pretending to be a responsible adult! Good luck with that. 🕴️🧢",
            "Happy birthday! Let’s do things we’ll definitely regret but laugh about tomorrow! 🍻🔥",
            "You might be aging, but your maturity level is safely staying exactly the same. 🧸😎",
            "Another year closer to becoming that weird friend everyone warns people about! 👽🤘"
        ]
        
        final_text = random.choice(messages) + "\n\n" + random.choice(funny_quotes)

