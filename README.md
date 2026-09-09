# Python Calendar Module

The `calendar` module is a built-in Python module used to work with **calendars, months, weekdays, leap years, and dates**.

No installation is required.

---

## 1. Import Calendar

```python
import calendar
```

---

## 2. Display a Month Calendar

```python
import calendar

print(calendar.month(2026, 9))
```

Output:

```text
   September 2026
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
```

### Syntax

```python
calendar.month(year, month)
```

---

## 3. Display Full Year Calendar

```python
import calendar

print(calendar.calendar(2026))
```

This displays the calendar for the **entire year**.

---

## 4. Check Leap Year

A leap year contains **366 days** instead of 365.

```python
import calendar

print(calendar.isleap(2024))
```

Output:

```text
True
```

Example:

```python
print(calendar.isleap(2025))
```

Output:

```text
False
```

---

## 5. Count Leap Years

```python
import calendar

print(calendar.leapdays(2000, 2025))
```

This counts leap years from the starting year **up to, but not including**, the ending year.

```python
calendar.leapdays(start_year, end_year)
```

---

## 6. Get Weekday

`calendar.weekday()` returns the weekday number.

```python
import calendar

print(calendar.weekday(2026, 9, 9))
```

Weekday numbers:

```text
Monday    = 0
Tuesday   = 1
Wednesday = 2
Thursday  = 3
Friday    = 4
Saturday  = 5
Sunday    = 6
```

---

## 7. Get Month Information

```python
import calendar

print(calendar.monthrange(2026, 9))
```

Output:

```text
(1, 30)
```

The result contains:

```text
(first weekday, number of days)
```

For September 2026:

* `1` → Tuesday
* `30` → 30 days

---

## 8. Get Month Name

```python
import calendar

print(calendar.month_name[9])
```

Output:

```text
September
```

`month_name` contains the full month names.

```python
print(calendar.month_name[1])
print(calendar.month_name[12])
```

Output:

```text
January
December
```

---

## 9. Get Short Month Name

```python
import calendar

print(calendar.month_abbr[9])
```

Output:

```text
Sep
```

Example:

```python
print(calendar.month_abbr[1])
print(calendar.month_abbr[12])
```

Output:

```text
Jan
Dec
```

---

## 10. Get Weekday Names

```python
import calendar

print(calendar.day_name[0])
```

Output:

```text
Monday
```

Example:

```python
for day in calendar.day_name:
    print(day)
```

Output:

```text
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```

---

## 11. Short Weekday Names

```python
import calendar

for day in calendar.day_abbr:
    print(day)
```

Output:

```text
Mon
Tue
Wed
Thu
Fri
Sat
Sun
```

---

## 12. Change First Day of Week

By default, Python's calendar uses Monday as the first day.

You can change it using:

```python
calendar.setfirstweekday(calendar.SUNDAY)
```

Example:

```python
import calendar

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(2026, 9))
```

Now Sunday appears as the first column.

---

## 13. Get Calendar as List

`monthcalendar()` returns the month's calendar as a list of weeks.

```python
import calendar

print(calendar.monthcalendar(2026, 9))
```

Example output:

```text
[[0, 1, 2, 3, 4, 5, 6],
 [7, 8, 9, 10, 11, 12, 13],
 ...]
```

`0` represents a day that belongs to the previous or next month.

---

## 14. Find Number of Sundays

You can use `monthcalendar()` to work with individual weekdays.

```python
import calendar

data = calendar.monthcalendar(2026, 9)

sundays = 0

for week in data:
    if week[6] != 0:
        sundays += 1

print(sundays)
```

Here:

```text
Sunday = index 6
```

---

## 15. Calendar Constants

The module provides constants for weekdays.

```python
calendar.MONDAY
calendar.TUESDAY
calendar.WEDNESDAY
calendar.THURSDAY
calendar.FRIDAY
calendar.SATURDAY
calendar.SUNDAY
```

Example:

```python
import calendar

print(calendar.MONDAY)
print(calendar.SUNDAY)
```

Output:

```text
0
6
```

---

## 16. Print Calendar Using `TextCalendar`

`TextCalendar` allows you to create a calendar object.

```python
import calendar

cal = calendar.TextCalendar()

print(cal.formatmonth(2026, 9))
```

---

## 17. Create Calendar Starting on Sunday

```python
import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)

print(cal.formatmonth(2026, 9))
```

---

## 18. `monthdayscalendar()`

Returns the days of a month arranged into weeks.

```python
import calendar

cal = calendar.Calendar()

print(cal.monthdayscalendar(2026, 9))
```

Difference:

```python
calendar.monthcalendar(2026, 9)
```

is a convenient function.

```python
cal.monthdayscalendar(2026, 9)
```

uses a `Calendar` object.

---

## 19. Simple Birthday Example

```python
import calendar

year = 2005
month = 8

print(calendar.month(year, month))
```

This prints the calendar for August 2005.

---

## 20. User Input Example

```python
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))
```

Example:

```text
Enter year: 2026
Enter month: 9
```

The calendar for September 2026 will be displayed.

---

# Important Calendar Functions

| Function                     | Purpose                              |
| ---------------------------- | ------------------------------------ |
| `calendar.month()`           | Display a month                      |
| `calendar.calendar()`        | Display a complete year              |
| `calendar.isleap()`          | Check leap year                      |
| `calendar.leapdays()`        | Count leap years                     |
| `calendar.weekday()`         | Get weekday number                   |
| `calendar.monthrange()`      | Get first weekday and number of days |
| `calendar.monthcalendar()`   | Get month as weeks                   |
| `calendar.month_name`        | Full month names                     |
| `calendar.month_abbr`        | Short month names                    |
| `calendar.day_name`          | Full weekday names                   |
| `calendar.day_abbr`          | Short weekday names                  |
| `calendar.setfirstweekday()` | Change first weekday                 |
| `calendar.TextCalendar()`    | Create text calendar                 |
| `calendar.Calendar()`        | Create calendar object               |

---

# Weekday Number

```text
Monday    → 0
Tuesday   → 1
Wednesday → 2
Thursday  → 3
Friday    → 4
Saturday  → 5
Sunday    → 6
```

---

# Last-Minute Cheat Sheet

```python
import calendar
```

### Month

```python
calendar.month(2026, 9)
```

### Full Year

```python
calendar.calendar(2026)
```

### Leap Year

```python
calendar.isleap(2024)
```

### Weekday

```python
calendar.weekday(2026, 9, 9)
```

### Month Information

```python
calendar.monthrange(2026, 9)
```

### Month Calendar as List

```python
calendar.monthcalendar(2026, 9)
```

### Month Name

```python
calendar.month_name[9]
```

### Short Month Name

```python
calendar.month_abbr[9]
```

### Day Name

```python
calendar.day_name[0]
```

### Short Day Name

```python
calendar.day_abbr[0]
```

### Change First Day

```python
calendar.setfirstweekday(calendar.SUNDAY)
```

---
