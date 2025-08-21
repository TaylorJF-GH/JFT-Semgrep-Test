# Step1: Prompt for Celsius Input
celsius_input = input("Enter the temperature in Celsius: ")
celsius = int(celsius_input) # Convert input to Integer

# Step 2: Convert to Float
celsius_float = float(celsius)

# Step 3: Calculate Fahrenheit
fahrenheit = (celsius_float * 9/5) + 32

# Step 4: Display Result
print (f"{celsius}° Celsius is {fahrenheit}° Fahrenheit")
