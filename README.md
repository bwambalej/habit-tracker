<!-- TABLE OF CONTENTS -->
# Table of Contents
- [Habit Tracker](#Joram-habit-tracker)
  * [Habit Tracker's Core Functionality][def]
    + [See Progress and Streaks](#see-progress-and-streaks)
- [Getting Started](#getting-started)  
  * [Installing](#installing)
    + [Packages for running tests](#packages-for-running-tests)
  * [How To Run the Program](#how-to-run-the-program)
  * [Running Tests](#running-tests)
- [Usage](#usage)
  * [Add/Remove Habit OR Category](#add-remove-habit-or-category)
      - [1. Adding a habit](#1-adding-a-habit)
      - [2. Remove Habit](#2-remove-habit)
      - [3. Delete Category](#3-delete-category)
      - [4. Get to Main Menu](#4-get-to-main-menu)
  * [Modify Habit's coverage](#modify-habit-s-coverage)
  * [Mark Habit as Completed](#mark-habit-as-completed)
  * [Show Habits (All or Sort them by their coverage)](#show-habits-all-or-sort-them-by-their-coverage-)
      - [1. View All Habits](#1-view-all-habits)
      - [2. View Daily Habits](#2-view-daily-habits)
      - [3. View Weekly Habits](#3-view-weekly-habits)
      - [4. View Monthly Habits](#4-view-monthly-habits)
      - [5. Get to Main Menu](#5-get-to-main-menu)
  * [Habit Analytics](#habit-analytics)
      - [1. View All Habit's Streaks](#1-view-all-habit-s-streaks)
      - [2. View Longest Streak of Specific Habit](#2-view-longest-streak-of-specific-habit)
      - [3. View Streak Log of Specific Habit](#3-view-streak-log-of-specific-habit)
      - [4. Get to Main Menu](#4-get-to-main-menu-1)
  * [Close App](#close-app)
- [Contact](#contact)

# Habit Tracker

In one way or another, many people work to better
themselves. Our ideal selves motivate us to improve,
whether it's through increasing our sleep and fitness
routines or the amount of time we spend doing the things
we love.
In fact, who we are is shaped by the little things we do
every day. And an excellent tool for changing them is this habit
tracker


## Habit Tracker's Core Functionality
Basically, a user of the habit tracker can:
* Add/Delete a Habit OR Category
* Modify Habit's coverage
* Mark a Habit as Completed
* Show Habits (All or Sort them by their coverage)

### See Progress and Streaks
The user can also view: 
* All of their generated habits 
* All of their created habits for a certain period
* All of their created streaks 
* The longest streak of any given habit 
* The history of any specific streak of any habit

# Getting Started
**Important**: Ensure that your Operating System has Python 3.8 or later installed. Python's most recent version can be downloaded from [here.](https://www.python.org/downloads/)

## Installing
You can download the latest version of Python from [here.](https://www.python.org/downloads/) <br>

<br> After installing Python, you can also install the following libraries. <br>

<br>[Questionary](https://www.python.org/downloads/) - Questionary is a Python library for building pretty command line interfaces. 
<br>You can install by running the below command:<br>
```
pip install questionary
```

### Packages for running tests
You must have the following packages installed in order to run the tests:
<br>Pytest - For testing functions:<br>
```
pip install -U pytest
```
<br>Freezegun - For freezing time: <br>
```
pip install freezegun
```

## How To Run the Program
Download the files from this repository (if not previously downloaded) after the dependencies have been installed, then place them in a separate folder. Go to your downloaded folder by [cd] (https://www.alphr.com/change-directory-in-cmd/) into your command or terminal window. Then, enter the command that follows to run the program:
```
python main.py
```
For Python 3.10+
```
python3 main.py
```
After doing this, the CLI will be launched, and your Habit Tracker will display the following options for you to select from:

```
****** Welcome to Joram's Habit Tracker *******


****** Always maintain streaks for a good health*******

 Select from the list on what you wish to do? (Use arrow keys)
  Add/Delete a Habit OR Category
   Modify Habit's coverage
   Mark a Habit as Completed
   Show Habits (All or Sort them by their coverage)
   Habit Analytics
   Close App

```

## Running tests
To run the test, use [cd] (https://www.alphr.com/change-directory-in-cmd/) to navigate to the test folder (included within the repository), and then type ```pytest```. 

# Usage

## Add/Remove Habit OR Category
#### 1. Adding a habit
The first step should be to establish a habit, which you can do by starting the program and choosing:
```
Add/Delete a Habit OR Category
```
The user will then be exposed to a sub-menu, where they must select *Add habit* and enter the necessary data:
```
Would you like to Add, Remove Habit or Category? (Use arrow keys)
 » Add Habit
   Remove Habit
   Delete Category
   Get to Main Menu

```
#### 2. Remove Habit
You can select the habit you want to eliminate and hit enter after this option displays a list of the habits you've developed.

#### 3. Delete Category
A list of generated categories will be displayed for the user to choose from, just like when eliminating a habit.

#### 4. Get to Main Menu
the user is returned to the main menu.

## Modify Habit's Periodicity
User will have to select the habit they'd like to change the periodicity of and then a new prompt will ask the user to select the new periodicity for the habit.

## Mark Habit as Completed
This option allows the user to indicate their habit as finished. 

## Show Habits (All or Sort them by their coverage)

#### 1. View All Habits
Lists all the created habits along with their information like *Name, Periodicity, Category and Date/Time*.


#### 2. View Daily Habits
Lists all the habits in the daily period.
#### 3. View Weekly Habits
Lists all the habits in the weekly period.
#### 4. View Monthly Habits
Lists all the habits in the monthly period.
#### 5. Back to Main Menu
back to home 

## Habit Analytics
#### 1. View All Habit's Streaks
Lists all the habits and their streaks.

#### 2. View Longest Streak of Specific Habit
Lists the longest streak ever achieved by a specific habit.
#### 3. View Streak Log of Specific Habit
Shows the streak history of the specific habit.
#### 4. Back to Main Menu
And menu it is!

## Close App
Exits the App.

# Contact

JORAM BWAMBALE - [Email](mailto:jorambwambale@iu-study.org)

Project Link: [https://github.com/bwambalej/habit-tracker](https://github.com/bwambalej/habit-tracker)

<p align="right">(<a href="#top">back to top</a>)</p>


[def]: #habit-tracker-s-core-functionality
