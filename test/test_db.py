from db import add_habit, connect_database, fetch_habits_as_choices, habit_exists, remove_habit, \
    fetch_categories, update_periodicity, fetch_habit_periodicity, update_habit_streak, get_streak_count


class TestDatabase:
    """
    TestDatabase class contains method that tests the important functions of db module
    """

    def setup_method(self):
        self.db = connect_database("test_db.db")
               add_habit(self.db, "Weightcheck", "daily", "Health", "06/03/2023 11:00", 0)
        add_habit(self.db, "Medication", "daily", "Health", "06/03/2023 11:00", 0)
        add_habit(self.db, "running", "daily", "Health", "06/03/2023 11:00", 0)
        add_habit(self.db, "cleaning", "weekly", "fun", "06/03/2023 11:00", 0)
        add_habit(self.db, "washing", "monthly", "work", "06/03/2023 11:00", 0)
        add_habit(self.db, "nosmoking", "daily", "games", "06/03/2023 11:00", 0)

    def test_fetch_habits_as_choices(self):
        assert len(fetch_habits_as_choices(self.db)) == 6

    def test_fetch_categories(self):
        assert len(fetch_categories(self.db)) == 4

    def test_remove_habit(self):
        remove_habit(self.db, "nosmoking")
        assert habit_exists(self.db, "nosmoking") is False
        assert len(fetch_habits_as_choices(self.db)) == 5

    def test_update_periodicity(self):
        update_periodicity(self.db, "washing", "weekly")
        assert fetch_habit_periodicity(self.db, "washing") == "weekly"

    def test_update_habit_streak(self):
        update_habit_streak(self.db, "Medication", 1, "07/03/2023 13:00")
        assert get_streak_count(self.db, "Medication") == 1

    def teardown_method(self):
        self.db.close()
        import os
        os.remove("test_db.db")
