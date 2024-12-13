# Eric Corbett
# 10/27/2024
# P3HW2
# Caculating employees hours and rate of pay 

# Prompt user for input
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize overtime variables
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
else:
    regular_hours = hours_worked
    overtime_hours = 0

# Calculate pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime is 1.5 times the pay rate
gross_pay = regular_pay + overtime_pay

# Display results
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
