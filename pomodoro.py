import time

work_time = 25 #minutes
break_time = 5 #minutes

def run_time(time1):
    for t in range (time1, -1, -1):
        minutes = t/60
        seconds = t%60
        print(str(minutes) + ":" + str(seconds))
        time.sleep(1)


def run_timer():
    do_pomodoro = True
    break_counter = 0
    run_time(5)
    while(do_pomodoro):
        if(break_counter >= 3):
            run_time(30)
            do_pomodoro = False
        else:
            run_time(5)
            break_counter += 1


print(run_timer())
