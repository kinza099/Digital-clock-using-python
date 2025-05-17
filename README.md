# ⏰ Digital Clock with Seven Segment Display

## 📝 Overview

This Python project simulates a digital clock using a seven-segment style text output. The clock displays the current system time in the format HH:MM:SS and updates every second using a custom `sevseg` module for rendering digits.

---

## ✨ Features

- 🕒 Displays the current system time in 12-hour format.
- 🔁 Automatically updates every second.
- 🔢 Uses a custom seven-segment representation for digits.
- ❌ Gracefully exits on Ctrl+C.

---

## 🛠️ Requirements

- 🐍 Python 3.x

Install required modules if not already available:

```bash
pip install sevseg  # If sevseg is a pip-installable module or ensure `sevseg.py` is in the same directory
```

> Note: If `sevseg` is a custom module, make sure the `sevseg.py` file is in the same directory as the script.

---

## 📂 Files

- `digital_clock.py`: The main Python script for the clock.
- `sevseg.py`: A module to generate seven-segment string representations of digits.

---

## 🚀 Usage

Run the script using:

```bash
python digital_clock.py
```

- The console will display the current time using a simulated seven-segment display.
- Press `Ctrl + C` to quit.

---

## 📦 Output Example

![image](https://github.com/user-attachments/assets/7854c984-acf6-41b9-9a67-176a66bdc741)

---

## 👩‍💻 Author

**Code by Kinza**

---

## 📜 License

This project is open-source and free to use.
