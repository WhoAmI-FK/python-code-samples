from calendar import weekday
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today();
    print(today);
    
    print("Date's components: ", today.day, " ", today.month, " ", today.year);

    print(today.weekday());
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
    print(days[int(today.weekday())]);
    today = datetime.now();
    print("The current date and time is", today);
    t = datetime.time(datetime.now());
    print(t);
if __name__ == "__main__":
    main();