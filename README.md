# Habit Tracker CLI

A simple command-line habit tracker built with Python.  
Track daily habits, maintain streaks, and persist data locally using JSON.

---

## Features

- Create new habits
- Log daily habit completions
- Calculate current streaks
- Persistent local storage with JSON
- Simple and lightweight CLI interface
- Clean modular Python codebase

---

## Project Structure

```bash
habit-tracker/
│
├── main.py          # Main application
├── habits.json      # Habit data storage
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Harsha0Sree/Habit-Tracker.git
```

### 2. Navigate into the project directory

```bash
cd habit-tracker
```

### 3. Run the application

```bash
python main.py
```

---

## Sample `habits.json`

```json
{
    "Workout": [
        "08/05/2026",
        "09/05/2026",
        "10/05/2026"
    ],
    "Read 10 Pages": [
        "07/05/2026",
        "08/05/2026"
    ],
    "Meditation": [],
    "Drink Water": [
        "10/05/2026"
    ]
}
```

---

## Menu Options

```text
1. Create new habit
2. List all habits
3. View streak
4. Log a habit
5. Quit
```

---

## Example Usage

```bash
Habit Tracker
--------------
1. Create new habit
2. List all habits
3. View streak
4. Log a habit
5. Quit

Select an option: 1

Enter new habit name: Workout
Habit 'Workout' created successfully.
```

---

## Tech Stack

- Python 3
- JSON for local data persistence
- Standard Library only

---

## Future Improvements

- Delete habits
- Weekly/monthly analytics
- SQLite database support
- Better CLI styling with Rich/Typer
- Export reports to CSV
- Unit testing with pytest
- Docker support
- GitHub Actions CI/CD


---

## Author

Built by Mikey.
