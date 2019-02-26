# custom-pomodoro

This is a customized productivity clock/timer based on the Pomodoro method.

## What is the pomodoro method?

Pomodoro is a productivity method named for the Italian word for tomato. See the wikipedia article [here!](https://en.wikipedia.org/wiki/Pomodoro_Technique)


## How does this program work?

This program uses python 3 and the Tkinter module to put a custom spin on the pomodoro method.

My program starts by greeting the user and ask them how many hours they would like to work for - this determines how many pomodoro "sessions" will take place, and when to stop the program.

!(screenshot)[https://github.com/keeganosler/custom-pomodoro/blob/master/readme_images/enter_exercises.PNG]

Then the program prompts the user to input a list of physical exercises (situps, pushups, etc) to be performed during the short break.  There are 2 preloaded tasks, one of which will be performed during every short break along with one of the entered exercises.

Once one pomodoro session (25 minutes) has been performed, the program informs the user that it's time for a short break and tells the user what to do during this break.

After 4 pomodoro sessions have been performed, the program informs the user that it's time for a longer break (30 mins) and tells the user what to do during these times (these are preloaded tasks).

After the full day is over, the program informs the user it's time to stop working and says goodnight.
