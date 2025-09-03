#function with arguments and return type
def convert(days):
    months=(days%365)//30
    years=days//365
    return months,years
convert(500)
