import time

work_time = 25 #minutes
break_time = 5 #minutes

def run_time(t_run):
    for t in range (t_run, -1, -1):
        minutes = int(t/60)
        seconds = t%60
        print(str(minutes) + ":" + str(seconds))
        time.sleep(1)


def run_timer():
    do_pomodoro = True
    break_counter = 0
    run_time(1500)
    while(do_pomodoro):
        if(break_counter >= 3):
            run_time(1800)
            do_pomodoro = False
        else:
            run_time(300)
            break_counter += 1


print(run_timer())
