weight = float(input('Enter your weight(kg): '))
height = float(input('Enter your height(m): '))

BMI = weight / (height * height)

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI <= 24.9:
    print('Normal')
elif BMI >= 25 and BMI <= 29.9:
    print('Overweight')
elif BMI >= 30 and BMI <= 34.9:
    print('Obese')
elif BMI == 35:
    print('Extremely Obese')
else:
    print('Undefined')