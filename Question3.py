def day_of_year_to_date(day_number, year):
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    month = 0
    while day_number > days_in_months[month]:
        day_number -= days_in_months[month]
        month += 1
    return f"{day_number} {month_names[month]}, {year}"
user_input = input("Enter the day number and year separated by a comma: ")
day_number, year = map(int, user_input.split(','))
result = day_of_year_to_date(day_number, year)
print(result)
