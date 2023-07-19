import time


def my_decorator(func):
    def countdown_wrapper():
        timer = 3
        while timer > 0:
            print(timer)
            timer -= 1
            time.sleep(1)
        func()
    return  countdown_wrapper

@my_decorator
def get_time():
    cur_time = time.strftime('%H:%M')
    print(cur_time)
    return cur_time

get_time()
