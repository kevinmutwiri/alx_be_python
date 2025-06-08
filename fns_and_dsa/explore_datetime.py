from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_future_date():
    while True:
        try:
            num_days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    current_date = datetime.now()
    future_date = current_date + timedelta(days=num_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    # Display the Current Date and Time
    display_current_datetime()

    # Calculate a Future Date
    calculate_future_date()


if __name__ == "__main__":
    main()
