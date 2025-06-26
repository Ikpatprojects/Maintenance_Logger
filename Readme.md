# 🛠️ Maintenance Logger (Python)

A simple command-line Python program that allows users to track and update the maintenance status of components.

---

## 📌 Project Goal

- Collect components that require maintenance
- Allow the user to mark components as serviced
- Update and display both serviced and unserviced lists
- Save the result to a file (`Maintenance_Log.txt`)
- Show the full path to the saved log

---

## 💻 Features

- Accepts any number of components from the user
- Uses `.title()` and `.lower()` for clean formatting
- Prevents duplicate maintenance entries
- Outputs results both to screen and to a text file
- Provides clear feedback for all actions

---

## 🧠 Concepts Practiced

- Lists and loops
- Conditional logic (`if`, `elif`, `else`)
- `while True` and `enumerate()`
- File handling with `open()`
- OS path management with `os.path.abspath()`

---

## 🏁 Sample Output
Enter components that require maintenance. [Enter x to exit] :

1.Pump

2.Sensor

3.Cable

4.x

All components entered:

1.Pump

2.Sensor

3.Cable

Has maintenance been done for any component? yes/no: yes
Enter the component(s) that have been maintained. [Enter x to exit]

1.Pump

2.Cable

1.x

All entries have been maintained

List Updated Successfully

The Maintained components are:

1.Pump

2.Cable

Component(s) that still require maintenance:

1.Sensor


---

## 📂 Output File Structure

```plaintext
The following components were serviced:
1. Pump
2. Cable

The following components were not serviced:
1. Sensor

```
🔖 Author
Peter Ikpat
A project from Week 1 of my Python learning journey

