#little rep: while vs for loop

#for loop is used when we know the number of iterations 
for num in range(1,11):
    print(num)

#while loop is used when we do not know the number of iterations but know the stopping condition
while True:
    name = input('enter the name: ')
    if name.isalpha():
        print('name:', name)
        break
    else:
        print('name cannot be an integer')
        continue