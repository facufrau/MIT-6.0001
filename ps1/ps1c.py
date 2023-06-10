# Starting data
portion_down_payment = 0.25
r = 0.04
current_savings = 0.0
semi_annual_raise = 0.07
months = 36
total_cost = 1000000.0

# Ask for user input
annual_salary = float(input("Enter the starting salary: "))

# Calculations
monthly_salary = annual_salary / 12
steps = 0
max_rate = 10000
min_rate = 0
error = 100
down_payment = portion_down_payment * total_cost

while abs(current_savings - down_payment) > 100:
    # Reset variables used to 0 before each iteration
    rate = (max_rate + min_rate) // 2
    portion_saved = rate / 10000
    current_savings = 0.0
    annual_salary_calc = annual_salary
    monthly_salary = annual_salary_calc / 12

    # Calculate savings with the rate proposed
    for m in range(months):
        if (m % 6 == 0) and m > 0:
            annual_salary_calc *= (1 + semi_annual_raise)
            monthly_salary = annual_salary_calc / 12
        current_savings += current_savings * (r/12)
        current_savings += (monthly_salary * portion_saved)

    # Adjust the rates according to the savings - payment
    if current_savings > down_payment:
        max_rate = (max_rate + min_rate) // 2
    elif current_savings < down_payment:
        min_rate = (min_rate + max_rate) // 2

    # Track iterations required
    steps += 1

    # Control the exit condition if salary if is not enough for saving
    if steps == 50:
        break

# Final results
if steps < 50:
    print(f"Best savings rate: {rate/10000:.4f}")
    print(f"Steps in bisection search: {steps}")
else:
    print(f"It is not possible to pay the down payment in three years.")
