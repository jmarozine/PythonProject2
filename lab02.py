name = "Jordan,Marozine"
age = 34
height = 6.0
favorite_color = "blue"
print(f"Hello, {name} I am {age} years old I am {height} feet tall and {favorite_color} is my favorite color.")
print(f""""
name: {name}
age: {34}
height: {6.0}
favorite color: {favorite_color}
""")
import math
radius = 5
circle_area = math.pi * (radius ** 2)
print(f"{circle_area:.1f}")
import math
sqrt_age = math.sqrt(age)
print(f"The square root of age ({age}) is: {sqrt_age}")
sin_height = math.sin(height)
cos_height = math.cos(height)
print(f"The sine of height ({height}) is: {sin_height}")
print(f"The cosine of height ({height}) is: {cos_height}")
age = 34
height = 6.0
sum_result = age + 5
difference_result = height - 4
product_result = age * height
quotient_result = height / 2
remainder_result = age % 3
power_result = age ** 2
print(f"The sum of age and 5 is: {sum_result}")
print(f"The difference between height and 4 is: {difference_result}")
print(f"The product of age and height is: {product_result}")
print(f"The quotient of height and 2 is: {quotient_result}")
print(f"The remainder of age divided by 3 is: {remainder_result}")
print(f"age raised to the power of 2 is: {power_result}")
unit = input("Is this temperature in celcius or farenheit? (C/F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((9*temp) / 5 + 32, 1)
    print(f"the temperature in farenheit is: {temp}C")
elif unit == "F":
    temp = round((temp -32) * 5/9, 1)
    print(f"the temperature in celcius is: {temp}")
else:
    print(f"{unit} is an invalid measurement")





