try :
    num1 = input("Enter A Number : ")
    num2 = input("Enter Another Number : ")
    print "Sum is " ,num1 + num2

except ValueError :
    print "Both The Inputs Must Be Numbers (ValueError)"
except TypeError:
    print "Both The Inputs Must Be Numbers (TypeError)"
except NameError:
    print "Enter a number not a word (NameError)"
except :
    print "Enter a number (Other)"
else :
    print "The sum has been successfully printed"

finally :
    print  "Thanks For Using "
