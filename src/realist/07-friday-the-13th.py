from datetime import date, timedelta

def friday_the_13th():
    current_date = date.today()

    def increment_month(d):
        mm = 1 if d.month == 12 else d.month + 1
        yy = d.year + 1 if mm == 1 else d.year
        
        return date(yy, mm, d.day)
        
    if current_date.day == 13 and current_date.weekday() == 4:
        return current_date.isoformat()
    
    clap_date = current_date + timedelta(13 - current_date.day)
    
    if current_date > clap_date:
        clap_date = increment_month(clap_date)
    
    while True:
        if clap_date.weekday() == 4:
            return clap_date.isoformat()
        clap_date = increment_month(clap_date)