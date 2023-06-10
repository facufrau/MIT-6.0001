# Starting data
portion_down_payment = 0.25
r = 0.04
current_savings = 0.0

# Ask for user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Calculations
monthly_salary = annual_salary / 12
months = 0
down_payment = portion_down_payment * total_cost
while current_savings < down_payment:
    current_savings += current_savings * (r/12)
    current_savings += (monthly_salary * portion_saved) 
    months += 1
print(f"Number of months: {months}")

