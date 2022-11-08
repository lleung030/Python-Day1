#Exercise #1 
#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

for i in range(1,n):
    a = (i**3)
    print (a)
    if a==1000:
         break
     

#Exercise #2 
#Get first prime numbers up to 100

for num in range(2,101):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            
#xercise 3 
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input("What is your age: "))
if age<18:
    print(' you are a kid')
elif age>=18 and age<=65:
    print('you are an adult')
else:
    print('you are a senior')