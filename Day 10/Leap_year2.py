def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year.")
                return True
            else:
                # print("Not leap year.")
                return False
        else:
            # print("Leap year.")
            return True
    else:
        # print("Not leap year.")
        return False


months = "";
smonth = "";

def days_in_month(year, month):
    if year < 1:
      return "Invalid year"
    if month > 12 or month < 1:
      return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if is_leap(year) and month == 2:
        return 29
    smonth = (months[month-1])
    # print(smonth)
    print(f"You picked the month of: {smonth}, in the year {year}.")
    return month_days[month - 1]
    






#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"It has {days} days")


# print(smonth)
# print(f"You picked the year: {year} and the {smonth} has {days} days.")