from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    print(timedelta(days=365, hours=5, minutes=1));
    now = datetime.now();
    print(now);
    print(str(now + timedelta(days=365)));
    print(str(now + timedelta(weeks=2, days=3)));
    t = datetime.now() - timedelta(weeks=1);
    s = t.strftime("%A %B %d, %Y");
    print(s);
    today = date.today();
    afd = date(today.year, 4, 1);
    if afd < today : 
        print("April Fools' Day already went by", ((today-afd).days));
        afd = afd.replace(year=today.year+1);
    time_to_afd = afd - today;
    print("It is", time_to_afd.days);
    
if __name__ == "__main__":
    main();
