import calendar

def print_calendar(year, month):
  """Prints the calendar for the given year and month.

  Args:
    year: The year.
    month: The month.
  """

  print(calendar.month(year, month))

if __name__ == '__main__':
  year = int(input("Enter a year: "))
  month = int(input("Enter a month: "))

  print_calendar(year, month)
