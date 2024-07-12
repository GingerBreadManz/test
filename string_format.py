weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight//height**2
msg="This is your BMI"
x = 'looked'
# format method
print("{} Your BMI: {}".format(msg,BMI))
# f-string (formatted string literals)
print(f'{msg} see it here{BMI}')
# using % operator.
print("Misha %s and %s around" % ('walked', x))
# It allows you to insert values into a string using placeholders.
# "format string" % (value1, value2, ...)

