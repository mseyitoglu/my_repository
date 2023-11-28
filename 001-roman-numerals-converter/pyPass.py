import random
print("Welcome to the PyPassword Generator!")

numberOfLetters=int(input("How many letters would you like in your password?"))
numberOfSymbols=int(input("How many symbols?"))
numberOfNumbers=int(input("How many numbers"))
letters=["a","b", "c", "d"]
numbers=["1","2","3","4"]
symbols=["?","!", "@","%"]
passwd=[]

for i in range(1, numberOfLetters + 1):
    passwd += random.choice(letters)

for i in range(1, numberOfSymbols + 1):
    passwd += random.choice(symbols)

for i in range(1, numberOfNumbers + 1):
    passwd += random.choice(numbers)

print (passwd)  


random.shuffle(passwd)    

password=""
for char in passwd:
    password += char
    
print (password)

    

