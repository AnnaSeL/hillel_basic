# print(1)
# from art import *
from datetime import date, datetime, timedelta

today = date.today() + timedelta(days=1)
tomorrow = today + timedelta(days=1, weeks=1)
print(date.today().strftime('%d-%m-%Y'))
print(tomorrow.strftime('%d-%m-%Y'))

now = datetime.now()
print(now.strftime('%d-%m-%Y %H:%M'))

try:
    obj_date = date(123, 10, 1)
    print(obj_date)
except ValueError:
    print('OUR YEAR IS FAILED')

def custom_print(*args, **kwargs):
    for arg in args:
        print(kwargs['first'], arg, kwargs['second'] )

param = {'first': '<<>>', 'second': '>><<'}
custom_print(1,2,3, None, 'AWESOME!', 'ANOTHER ON!', **param)

#dict comprehension {k:v .. k}
