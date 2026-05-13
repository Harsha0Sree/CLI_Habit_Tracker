import json
from datetime import datetime, timezone


class User:
    def __init__(self, name, habits):
        self.name = name
        self.habits = habits

    def add_habit(self, new_habit):
        for habit in self.habits:
            if habit.name == new_habit.name:
                print("Habit already exists")
                return False
        self.habits.append(new_habit)
        return True

    def to_dict(self):
        dicted_habits = []
        for habit in self.habits:
            dicted_habits.append({"name": habit.name, "logs": habit.logs})

        data = {"name": self.name, "habits": dicted_habits}
        return data


class Habit:
    def __init__(self, name, logs=None):
        self.name = name
        self.logs = logs if logs is not None else []

    def log_habit(self):
        date_when_logged = datetime.now(timezone.utc).strftime("%d/%m/%Y")

        if date_when_logged not in self.logs:
            self.logs.append(date_when_logged)
            return True

        print("Habit already logged today")
        return False

    def calculate_streak(self):
        date_objects = sorted(
            [datetime.strptime(dates, "%d/%m/%Y").date() for dates in self.logs]
        )

        if not date_objects:
            return 0

        today = datetime.now(timezone.utc).date()
        latest_date = date_objects[-1]

        # streak is broken
        if (today - latest_date).days > 1:
            return 0

        streak = 1
        current_index = len(date_objects) - 1

        while current_index > 0:
            current_date = date_objects[current_index]
            previous_date = date_objects[current_index - 1]

            if (current_date - previous_date).days == 1:
                streak += 1
                current_index -= 1
            else:
                break

        return streak


def habit_selector(user_obj):
    if not user_obj.habits:
        print("No habits found")
        return None

    print("\nHabits:")

    while True:
        for habit in user_obj.habits:
            print(f"- {habit.name}")
        selected_habit = input("Which habit do you want to select? ")
        for habit in user_obj.habits:
            if selected_habit == habit.name:
                return habit
        print("Invalid habit")


def load_data():
    try:
        with open("habits.json", "r") as file:
            data = json.load(file)

            habits = []

            for habit_data in data["habits"]:
                habit = Habit(habit_data["name"], habit_data["logs"])

                habits.append(habit)

            return User(data["name"], habits)

    except (FileNotFoundError, json.JSONDecodeError):
        return User("Mikey", [])


def save_data(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file)


def validate_option(option):
    valid_options = ["1", "2", "3", "4", "5"]
    return option in valid_options


def option_selector():
    return input(
        "\nWhat do you want to do?\n"
        "1. Create new habit\n"
        "2. List all habits\n"
        "3. See streak\n"
        "4. Log a habit\n"
        "5. Quit\n"
        "Select option: "
    )


def main():
    mikey = load_data()

    while True:
        option = option_selector()

        if option == "5":
            print("Goodbye")
            break

        if not validate_option(option):
            print("Invalid option")
            continue

        if option == "1":
            new_habit = input("Enter new habit name: ")
            new_habit_obj = Habit(
                new_habit,
            )
            if mikey.add_habit(new_habit_obj):
                save_data(mikey.to_dict())

        elif option == "2":
            if not mikey.habits:
                print("No habits found")
            else:
                print("\nHabits:")
                for habit in mikey.habits:
                    print(f"- {habit.name}")

        elif option == "3":
            selected_habit = habit_selector(mikey)

            if selected_habit:
                streak = selected_habit.calculate_streak()
                print(f"Current streak: {streak} days")

        elif option == "4":
            selected_habit = habit_selector(mikey)

            if selected_habit:
                if selected_habit.log_habit():
                    save_data(mikey.to_dict())


if __name__ == "__main__":
    main()
