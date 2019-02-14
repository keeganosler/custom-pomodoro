import time

import tkinter
from tkinter import messagebox
import winsound

root = tkinter.Tk()
root.withdraw()

def run_time(t_run):
    for t in range (t_run, -1, -1):
        minutes = int(t/60)
        seconds = t%60
        print(str(minutes) + ":" + str(seconds))
        time.sleep(1)  

def pick_short_tasks(counter):
    exercises = ["situps", "pullups", "plank", "pushups"]
    short_tasks = ["refill water", "message girlfriend", "use the bathroom", "shoulder stretches"]
    exercise_todo = exercises[counter]
    short_task_todo = short_tasks[counter]
    messagebox.showinfo("Time for a short break!!", "\n During this time you should do the following things:\n 1. " + exercise_todo + "\n 2. " + short_task_todo)

def run_timer():
    do_pomodoro = True
    break_counter = 0
    task_counter = 0
    while(do_pomodoro):
        messagebox.showinfo("Pomodoro started!", "\n If you wish to start a 25-minute work period, please click the button below.")
        run_time(8)
        if(break_counter >= 3):
            messagebox.showinfo("Time for a long break!!", "\n During this time, you should do the following things:\n 1. Eat something. \n2. Take out the dog")
            run_time(10)
            do_pomodoro = False
        else:
            pick_short_tasks(task_counter)
            task_counter += 1
            run_time(5)
            messagebox.showinfo("Your break is over!", "\nTime to get back to work!")
            break_counter += 1

print(run_timer())

