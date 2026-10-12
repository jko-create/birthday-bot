import csv, io, os, datetime, requests, jdatetime

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
        age_text = f" {age} سالگی" if age > 0 else ""
        
        requests.post(
            f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage",
            json={"chat_id": os.environ["CHAT_ID"],
                  "text": f"🎂 امروز تولد{age_text} {p['name']} عزیزه، !"})
      
