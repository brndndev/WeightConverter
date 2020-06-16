name = input('What is your name? ')
print('Hi ' + name)

color = input('What is your favorite color? ')
print('I like the color ' + color + ' too! :)')

food = input('What is your favorite food? ')
print(food + ' is disgusting!')

print('Hello ' + name + ' My favorite color is ' +
      color + ' too! I strongly dislike ' +
      food + '!')

birth_year = input('What is your birth year? ')
age = 2020 - int(birth_year)

    if age < 37:
        print(age)
        print('That is pretty young!')

    # elif age == 25:
    #     print('I am 25 too!')

    else:
        print(age)
        print("That's pretty old!")

weight_lbs = input('What is your weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print('That is about ')
print(weight_kg)
print(' in kilograms')



