# check if a number is prime or not

num = input("Enter The Number : ")
isPrime = True
if num<=1:
    print "Not Prime"
else:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            isPrime = False
            print "Not Prime"
            break
if isPrime==True:
    print "Prime"