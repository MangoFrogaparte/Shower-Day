from datetime import date
import datetime
x = date.today()
y = date.weekday(date.fromisoformat(f'{x}'))
if y == 1:
  print("Shower Day")
if y == 3:
  print("Shower Day")
if y == 5:
  print("Shower Day")
if y == 7:
  print("Shower Day")
if y == 2:
  print("No Shower Day")
if y == 4:
  print("No Shower Day")
if y == 6:
  print("No Shower Day")