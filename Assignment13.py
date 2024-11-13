enter_number=int(input('enter a number:'))
for i in range(2,enter_number):
    if enter_number%i==0:
       print(enter_number,"is not a prime number.")
       break
else:
    print(enter_number,"is a prime number.")
    