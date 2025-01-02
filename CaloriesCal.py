def calculate_calories():

	# Step 1: Get user inputs
	gender = input("Enter gender (M/F): ").strip().upper()
	weight = float(input("Enter weight (kg): "))
	height = float(input("Enter height (cm): "))
	age = int(input("Enter age (years): "))
	
	# Step 2: Get activity level
	print("\nActivity levels:")
	print("1. Sedentary (little or no exercise)")
	print("2. Lightly active (light exercise/sports 1-2 days a week)")
	print("3. Moderately active (moderate exercise/sports 3-5 days a week)")
	print("4. Very active (hard exercise/sports 6-7 days a week)")
	print("5. Super active (very hard exercise, physical job or training)")
	activity_choice = int(input("Choose your activity level (1-5): "))

	#Step 3: Validate gender and activity level
	if gender not in ["M", "F"]:
		raise ValueError("Gender must be M or F.")
	if activity_choice not in [1, 2, 3, 4, 5]:
		raise ValueError("Invalid activity level choice.")

	# Step 4: BMR Calculation
	if gender == "M":
		bmr = 10 * weight + 6.25 * height - 5 * age + 5
	else:
		bmr = 10 * weight + 6.25 * height - 5 * age - 161

	# Step 5: Activity level factors
	activity_factors = {
	1: 1.2,
	2: 1.375,
	3: 1.55,
	4: 1.725,
	5: 1.9
	}

	daily_calories = bmr * activity_factors[activity_choice]
	
	# Step 6: Display results
	print(f"\nYour BMR: {bmr:.2f} calories/day")
	print(f"Calories needed to maintain your weight: {daily_calories:.2f} calories/day.")

if __name__== "__main__":
	print("Welcome to the Calorie Calculator!")

	# Call the function
	calculate_calories()