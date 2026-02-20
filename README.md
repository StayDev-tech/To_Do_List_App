# TO-DO List App (Console)

## Description

This is a simple **console-based To-Do List application** built in Python.
It allows users to add, view, and remove tasks directly from the terminal.
The app is designed to be lightweight, easy to use, and educational for beginners learning Python

## Features

- **Add Task:** Enter a new task to your to-do list.
  - Prevents adding empty tasks.
  - Prevents adding duplicate tasks.
- **View Tasks:** Display all current tasks in the list.
- **Remove Tasks:** Remove a task by specifying its number in the list.
  - Handles invalid numbers or empty lists gracefully.
- **Interactive Menu:** A simple text-based menu to navigate the app.
- **Looping Menu:** The menu keeps running until the user chooses to quit.

## How to use

1. Run the program:

   ```bash
       main.py
   ```

2. Use the menu options:
   - Enter 1 to add a task.
   - Enter 2 to view tasks.
   - Enter 3 to remove a task.
   - Enter 4 to quit the program.

3. Follow prompts in the terminal for each option.

## Requirements

- Python 3.x
- No external libraries required

## Notes

- Data is stored in memory, so tasks will disappear when the program is closed.
- Future improvements could include saving tasks to a file, marking tasks as completed, or adding due dates.
