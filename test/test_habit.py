import pytest
from habit import Habit
from db import add_habit, connect_database, fetch_habits_as_choices, habit_exists, remove_habit, \
    fetch_categories, update_periodicity, fetch_habit_periodicity, update_habit_streak, get_streak_count
from freezegun import freeze_time


@pytest.fixture(scope='module')
def db():
    print('\n*****SETUP*****\n')
    db = connect_database("test_habit.db")
    print("Created temporary test_habit.db for test purpose.\n")
    print("Initiating tests...\n")
    yield db 
    print("\nClosing connection with test database...\n")
    db.close()
    print("Connection successfully terminated!")
    import os
    os.remove("test_habit.db")
    print("\nDeleted test_habit.db file.")
    print("\nTest sucessfully completed :)")


def test_add(db):
    habit = Habit("Weightcheck", "daily", "Health", database="test_habit.db")
    habit.add()
    habit1 = Habit("Medication", "daily", "Health", database="test_habit.db")
    habit1.add()
    assert habit_exists(db, "Weightcheck")
    assert habit_exists(db, "Medication")


def test_remove(db):
    assert habit_exists(db, "Weightcheck") is True
    habit = Habit("Weightcheck", "daily", "Health", database="test_habit.db")
    habit.remove()
    assert habit_exists(db, "Weightcheck") is False


def test_delete_category(db):
    assert len(fetch_categories(db)) == 1
    habit3 = Habit("Walking", "daily", "fun", database="test_habit.db")
    habit3.add()
    assert len(fetch_categories(db)) == 2
    habit3.delete_category()
    assert len(fetch_categories(db)) == 1


def test_change_periodicity(db):
    assert fetch_habit_periodicity(db, "Medication") == "daily"
    habit1 = Habit("Medication", "weekly", database="test_habit.db")
    habit1.change_periodicity()
    assert fetch_habit_periodicity(db, "Medication") == "weekly"


# Time format (YYYY-MM-DD)
@freeze_time("2023-03-06")
def test_add_custom_habits(db):
    habit4 = Habit("dancing", "daily", "leisure", database="test_habit.db")
    habit4.add()
    habit5 = Habit("firewood", "weekly", "lighting", database="test_habit.db")
    habit5.add()
    habit6 = Habit("swimming", "monthly", "passingtime", database="test_habit.db")
    habit6.add()
    assert habit_exists(db, "dancing")


@freeze_time("2023-03-06")
def test_mark_habit4_as_completed(db):
    habit4 = Habit("dancing", "daily", "leisure", database="test_habit.db")
    habit4.mark_as_completed()
    assert get_streak_count(db, "dancing") == 1


@freeze_time("2023-03-06")
def test_mark_habit4_as_completed_again(db):
    habit4 = Habit("dancing", "daily", "leisure", database="test_habit.db")
    habit4.mark_as_completed()
    assert get_streak_count(db, "dancing") != 2


@freeze_time("2023-03-06")
def test_mark_habit4_as_completed_next_day(db):
  habit4 = Habit("dancing", "daily", "leisure", database="test_habit.db")
    habit4.mark_as_completed()
    assert get_streak_count(db, "dancing") == 2


@freeze_time("2023-03-06")
def test_mark_habit5_as_completed(db):
    assert get_streak_count(db, "fishing") == 0
    habit5 = Habit("firewood", "weekly", "lighting", database="test_habit.db")
    habit5.mark_as_completed()
    assert get_streak_count(db, "firewood") == 1


# Testing a day later
@freeze_time("2022-03-07")
def test_mark_habit5_as_completed_next_day(db):
habit5 = Habit("firewood", "weekly", "lighting", database="test_habit.db")
    habit5.mark_as_completed()
    assert get_streak_count(db, "fishing") != 2


# Testing a week later
@freeze_time("2022-03-12")
def test_mark_habit5_as_completed_next_week(db):
habit5 = Habit("firewood", "weekly", "lighting", database="test_habit.db")
    habit5.mark_as_completed()
    assert get_streak_count(db, "firewood") == 2


@freeze_time("2022-03-06")
def test_mark_habit6_as_completed(db):
    habit6 = Habit("swimming", "monthly", "passingtime", database="test_habit.db")
    habit6.mark_as_completed()
    assert get_streak_count(db, "swimming") == 1


# Testing 7 days later
@freeze_time("2022-03-13")
def test_mark_habit6_as_completed_10days_later(db):
   habit6 = Habit("swimming", "monthly", "passingtime", database="test_habit.db")
    habit6.mark_as_completed()
    assert get_streak_count(db, "swimming") != 2


# Testing a month later
@freeze_time("2022-04-06")
def test_mark_habit6_as_completed_month_later(db):
      habit6 = Habit("swimming", "monthly", "passingtime", database="test_habit.db")
    habit6.mark_as_completed()
    assert get_streak_count(db, "swimming") == 2
