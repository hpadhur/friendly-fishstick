from datetime import datetime

def print_day_month_sum() -> None:
    """
    Retrieves the current date, extracts the day and month, adds them,
    and prints the values along with their sum.

    For more details, see KAN-1: https://jira.example.com/browse/KAN-1
    """
    now = datetime.now()
    day, month = now.day, now.month
    result = day + month
    print(f"Day: {day}, Month: {month}, Sum: {result}")

print_day_month_sum()