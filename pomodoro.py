import time

import tkinter
#from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *

import winsound

root = tkinter.Tk()
root.withdraw()

#determines from user input how many pomodoros are to be performed given the number of hours the user wants to be working for
def setup_pomodoro():
    day_length = int(simpledialog.askstring("Welcome!", "Good day sir! \nHow long would you like your workday to be?"))
    if(!(day_length.is_integer())):
        messagebox.showinfo("Error", "Please enter a valid number of hours.")
        setup_pomodoro()
    num_pomodoro_sessions = int((day_length*3600) / 10500)
    return num_pomodoro_sessions

#starts the clock when called, for however much time its told to run for
def run_clock(t_run):
    for t in range (t_run, -1, -1):
        minutes = int(t/60)
        seconds = t%60
        print(str(minutes) + ":" + str(seconds))
        time.sleep(1)

#decides what tasks are performed during the short breaks
def pick_short_tasks(counter, list_exercises):
    short_tasks = ["refill water", "message girlfriend", "use the bathroom", "shoulder stretches"]
    messagebox.showinfo("Time for a short break!!", "\n During this time you should do the following things:\n 1. " + list_exercises[counter] + "\n 2. " + short_tasks[counter])

#sets up the list of exercises (one to be performed each short break) from user input
def setup_exercises():
    exercises_todo = []
    for i in range(0,4):
        exercise = simpledialog.askstring("Exercises to do", "Please enter an exercise: ")
        exercises_todo.append(exercise)
    return exercises_todo    

#sets up exercises and number of pomdoros
#initializes counters for number of breaks, number of (short) tasks and number of pomodoro sessions performed
#pulls up messages boxes for when pomodoros start and finish
#if 4 short breaks have been performed, a long break is performed
#once the specified number of pomodoros have been performed, it says goodnight
def run_timer():
    total_pomodoros = setup_pomodoro()
    exercises_todo = setup_exercises()
    pomodoro_count = 0
    break_counter = 0
    task_counter = 0
    while(pomodoro_count <= total_pomodoros):
        messagebox.showinfo("Pomodoro started!", "\n If you wish to start a 25-minute work period, please click the button below.")
        run_clock(1500)
        if((break_counter != 0) and ((break_counter/3).is_integer())):
            messagebox.showinfo("Time for a long break!!", "\n During this time, you should do the following things:\n 1. Eat something. \n 2. Take out the dog")
            run_clock(1800)
        else:
            pick_short_tasks(task_counter, exercises_todo)
            task_counter += 1
            run_clock(300)
            messagebox.showinfo("Your break is over!", "\nTime to get back to work!")
            break_counter += 1
    messagebox.showinfo("All done!", "I'd say that's enough work for one day! \nGoodnight sir!")

#runs the program
run_timer()
