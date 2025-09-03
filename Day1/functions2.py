#with arguments and non return
def convert(days):
    years=days/365
    months=(days%365)//30
    remaining_days=(days%365)%30
    print("years:",years)
    print("months:",months)
    print("remaining days:",remaining_days)
convert(500)
    