import datetime
today = datetime.datetime.today()
print('Today is:', today)
original_date = datetime.date(2020, 2, 28)
days_to_add = datetime.timedelta(hours=24)
print(today.year, today.month, today.day)
print('Adding 5 days to', original_date,':')
print(original_date+days_to_add)
