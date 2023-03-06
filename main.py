import questionary as qt
import get
from habit import Habit
import analytics

# opening message on the screen
print("""
****** Welcome to Joram's Habit Tracker *******
""")
print("""
****** Always maintain streaks for a good health*******
""")
#  App interface. On this a user shall be required to select a choice
def menu():
    """
    CLI Interface utilized with questionary library to
    pretty display the menu of the habit tracker for the user.
    """
    # this part shows six choices where an app user has to choose from
    choice = qt.select(
        "Select from the list on what you wish to do?",
        choices=[
            "Add/Delete a Habit OR Category",
            "Modify Habit's coverage",
            "Mark a Habit as Completed",
            "Show Habits (All or Sort them by their coverage)",
            "Habit Analytics",
            "Close App"
        ]).ask()

    if choice == "Add/Delete a Habit OR Category":
        # under this choice, i have more four sub-choices
        second_choice = qt.select(
            "Would you like to Add, Delete Habit or Category?",
            choices=[
                "Add a Habit",
                "Delete a Habit",
                "Delete Category",
                "Get to Main Menu"
            ]).ask()

        if second_choice == "Add a Habit":
            habit_name = get.habit_name()
            habit_periodicity = get.habit_periodicity()
            habit_category = get.habit_category()
            habit = Habit(habit_name, habit_periodicity, habit_category)
            habit.add()

        elif second_choice == "Delete a Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habits in the database
                print("\nSorry!! No habit found in database: Please add a habit first.\n")
            else:
                habit = Habit(habit_name)
                if get.habit_delete_confirmation(habit_name):
                    habit.remove()
                else:
                    print("\n we find it hard to get somethings right :)\n")

        elif second_choice == "Delete Category":
            try:
                habit_category = get.defined_categories()
            except ValueError:  # ValueError is raised when there are no categories in the database
                print("\nNo category found! Please add a habit & category using the 'Add a habit' option.\n")
            else:
                if get.category_delete_confirmation():
                    habit = Habit(category=habit_category)
                    habit.delete_category()
                else:
                    print("\nThanks for confirming!\n")

        elif second_choice == "Get to Main Menu":
            menu()

    elif choice == "Modify Habit's coverage":
        try:
            habit_name = get.habits_from_db()
        except ValueError:  # ValueError is raised when there are no habits in the database
            print("\nDatabase empty; Please add a habit first.\n")
        else:
            new_periodicity = get.habit_periodicity()
            if get.periodicity_change_confirmed():
                habit = Habit(habit_name, new_periodicity)
                habit.change_periodicity()
            else:
                print(f"\nCoverage of {habit_name} remains unchanged! Thanks for confirming.\n")

    elif choice == "Mark Habit as Completed":
        try:
            habit_name = get.habits_from_db()
        except ValueError:  # ValueError is raised when there are no habits in the database
            print("\nNo habit defined; please add a habit first to complete it!\n")
        else:
            habit = Habit(habit_name)
            habit.mark_as_completed()

    elif choice == "Show Habits (All or Sort them by their coverage)":
        second_choice = get.show_period_choices()  # Fetches choices list from Get module
        if second_choice == "View All Habits":
            analytics.show_habits_data()  # Analytics module contains the tabular formatted data visualizer
        elif second_choice == "View Daily Habits":
            analytics.show_habits_data("daily")
        elif second_choice == "View Weekly Habits":
            analytics.show_habits_data("weekly")
        elif second_choice == "View Monthly Habits":
            analytics.show_habits_data("monthly")
        elif second_choice == "Get to Main Menu":
            menu()

    elif choice == "Habit Analytics":
        second_choice = get.analytics_choices()
        if second_choice == "View All Habit's Streaks":
            analytics.show_habit_streak_data()
        elif second_choice == "View Longest Streak of Specific Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habits in the database
                print("\nNo habit data found in the database; Please add a habit first\n")
            else:
                analytics.show_habit_streak_data(habit_name)
        elif second_choice == "View Streak Log of Specific Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habit's log in the database
                print("\nNo habit log found; Please add a habit first\n")
            else:
                analytics.show_habit_logged_data(habit_name)
        elif second_choice == "Get to Main Menu":
            menu()

    elif choice == "Close App":
        print("\nNice time! Always maintain your streaks")  #incase the user closes app, this is the bye message
        exit()  # exit() completely close the application


if __name__ == "__main__":
    while True:
        menu()
