# ⏰ Clock Project

A customizable command-line clock application with alarm functionality, time format switching, and pause/resume capabilities. Built with Python using a clean modular architecture without global variables.

## 📋 Features

- **Real-time clock** - Continuously running clock display
- **Manual time adjustment** - Set any custom time
- **Alarm system** - Set alarms that ring at specific times
- **Format switching** - Toggle between 24-hour and 12-hour formats
- **Pause/Resume** - Freeze and unfreeze the clock
- **Time reset** - Reset to system time instantly
- **Input validation** - Prevents invalid time entries
- **Clean terminal UI** - ANSI codes for smooth display updates
- **Modular architecture** - Separated into display, logic, and main files
- **No global variables** - Uses parameters and return values for clean code

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Clone the repository

```bash
git clone https://github.com/mahira-manico/clock_project.git
cd clock_project
```

### Install dependencies

```bash
pip install keyboard
```

> **Note:** The `keyboard` library requires administrator/root privileges on some systems.

## 💻 Usage

### Run the program

```bash
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| **A** | Change the current time manually |
| **B** | Set an alarm |
| **C** | Reset to system time |
| **D** | Toggle between 24h and 12h format |
| **E** | Pause/Resume the clock |
| **Ctrl+C** | Exit the program |

### Setting the Time

1. Press `A`
2. Enter hour (0-23)
3. Enter minutes (0-59)
4. Enter seconds (0-59)
5. The clock updates immediately

### Setting an Alarm

1. Press `B`
2. Enter alarm hour (0-23)
3. Enter alarm minutes (0-59)
4. Enter alarm seconds (0-59)
5. The alarm will ring when the time matches

## 📁 Project Structure

```
Clock-project/
│
├── main.py          # Main program entry point and orchestration
├── function.py      # Core clock logic (time management, validation)
├── display.py       # Terminal display functions (ANSI codes)
└── README.md        # Project documentation
```

### File Descriptions

#### `main.py`
- Program entry point
- Contains the main menu loop
- Handles keyboard input detection
- Manages local variables (no globals!)
- Coordinates display and function modules

#### `function.py`
- Time manipulation functions
- Alarm logic
- Input validation
- Format conversion
- All business logic without display concerns

#### `display.py`
- Terminal control (cursor, screen clearing)
- ANSI escape codes for positioning
- Time formatting for display
- Menu rendering

## 🛠️ Technical Details

### Architecture Principles

**No Global Variables**
- All state is managed through function parameters and return values
- Variables are local to the `menu()` function
- Functions receive data as parameters and return modified values

**Separation of Concerns**
- **Display layer** (`display.py`) - Handles all visual output
- **Business logic** (`function.py`) - Handles time calculations and validation
- **Orchestration** (`main.py`) - Coordinates the application flow

### How the Clock Works

The clock advances without threading by checking elapsed time:

```python
now = time.time()
if now - last_update >= 1:
    current_time = running_hour(current_time, is_paused)
    last_update = now
```

Every loop iteration checks if 1 second has passed. If yes, increment the time.

### ANSI Escape Codes Used

- `\033[?25l` - Hide cursor
- `\033[?25h` - Show cursor
- `\033[2J\033[H` - Clear screen
- `\033[2K` - Clear entire line
- `\033[{row};{col}H` - Move cursor to position

### Input Validation Strategy

All user inputs are validated in a loop:
1. Try to convert input to integer
2. Check if value is in valid range
3. If invalid, display error and retry
4. Return only validated values

## 🔧 Code Examples

### Adding 1 Second to Time

```python
def running_hour(current_time, is_paused):
    if not is_paused:
        return current_time + timedelta(seconds=1)
    return current_time
```

### Checking Alarm

```python
def check_time_alarm(current_time, set_time_alarm):
    if set_time_alarm is None:
        return False
    
    h, m, s = set_time_alarm
    if (current_time.hour, current_time.minute, current_time.second) == (h, m, s):
        return True
    return False
```

### Toggling Format

```python
def change_time(time_format):
    if time_format == "24h":
        return "12h"
    elif time_format == "12h":
        return "24h"
```

## ⚠️ Known Limitations

- Requires administrator privileges for keyboard detection on some systems
- Terminal must support ANSI escape codes
- Clock precision depends on loop speed (approximately 1 second accuracy)
- Only one alarm can be set at a time

## 🐛 Troubleshooting

### "Permission denied" error

Run with administrator privileges:

**Windows (Command Prompt as Admin):**
```bash
python main.py
```

**Linux/Mac:**
```bash
sudo python3 main.py
```

### Keyboard library not detecting keys

Ensure you have the latest version:
```bash
pip install keyboard --upgrade
```

### Display issues

Make sure your terminal supports ANSI escape codes:
- ✅ Windows: Command Prompt, PowerShell, Windows Terminal
- ✅ Linux/Mac: All standard terminals
- ❌ Some IDE integrated terminals may not work properly

## 📚 Learning Objectives

This project demonstrates:
- **Modular programming** - Separating code into logical files
- **Parameter passing** - Avoiding global variables
- **Return values** - Functions that compute and return results
- **Input validation** - Ensuring data integrity
- **Time manipulation** - Working with datetime objects
- **Terminal control** - Using ANSI escape codes
- **Error handling** - Try/except for user inputs
- **Event detection** - Keyboard input handling

## 🔮 Future Improvements

- [ ] Multiple alarm support
- [ ] Alarm sound notification
- [ ] Save/load alarms to file
- [ ] Countdown timer feature
- [ ] Stopwatch functionality
- [ ] Color themes
- [ ] GUI version with tkinter
- [ ] Configuration file for settings
- [ ] Alarm labels/names
- [ ] Snooze functionality

## 👤 Author

**Mahira Manico**

- GitHub: [@mahira-manico](https://github.com/mahira-manico)
- Project Link: [https://github.com/mahira-manico/clock_project](https://github.com/mahira-manico/clock_project)

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built as a learning project to practice Python programming fundamentals
- Special focus on clean code architecture and avoiding global variables
- Demonstrates separation of concerns and modular design principles

---

⭐ **Star this repository if you found it helpful!**

## 📸 Screenshots

### Main Menu
```
Clock menu
18:30:45 (24h)
1. Change time/tap a
2. Set an alarm/tap b
3. Reset time/tap c
4. change format/tap d
5. Pause/tap e
6. Ctrl+C to quit
```

### With Pause Active
```
Clock menu
18:30:45 (24h) [PAUSED]
1. Change time/tap a
2. Set an alarm/tap b
3. Reset time/tap c
4. change format/tap d
5. Pause/tap e
6. Ctrl+C to quit
```

### 12-Hour Format
```
Clock menu
06:30:45 PM (12h)
1. Change time/tap a
2. Set an alarm/tap b
3. Reset time/tap c
4. change format/tap d
5. Pause/tap e
6. Ctrl+C to quit
```

---

Made with ❤️ for learning Python programming
