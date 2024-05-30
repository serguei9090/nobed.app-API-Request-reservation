from datetime import date, timedelta

def calculate_future_date(days=7):
  """
  This function calculates a date a specified number of days in the future.

  Args:
      days (int, optional): The number of days to add to the current date. Defaults to 7.

  Returns:
      date: The date that is `days` days in the future.
  """

  start_date = date.today()
  future_date = start_date + timedelta(days=days)
  return future_date