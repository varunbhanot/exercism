import datetime
def add_gigasecond(birth_date):
    delta = datetime.timedelta(seconds=1000000000)
    return birth_date + delta

