fizzBuzzList=[]

for number in range (1, 101):
    if number % 3 == 0:
        fizzBuzzList.append("Fizz")
    if number % 5 == 0:
        fizzBuzzList.append("Buzz")
    if number % 3*5 == 0:
        fizzBuzzList.append("FizzBuzz")
    else:
        fizzBuzzList.append(number)
print(fizzBuzzList)
    
