from datetime import timedelta, datetime
def display_current_datetime():
    current_date = datetime.now()
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

display_current_datetime()

def calculate_future_date():
    days_number =int(input('Enter the number of days to add to the current date: '))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_number)
    print(f'Future date : {future_date.strftime("%Y-%m-%d %H:%M:%S")}')

calculate_future_date()

