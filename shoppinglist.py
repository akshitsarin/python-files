# Shopping app
def show():
    print "This Is Your Current List : ", thelist

def help():
    print "DONE --> To Stop Entering New Items\nSHOW --> To Show Current Items In The List "

print "Welcome To The Shopping App\nType HELP for help."
thelist = []
while True :
    elements = raw_input ("Enter The Item : ")
    if elements.lower() == "done":
        break
    elif elements.lower() == "show":
        show()
    elif elements.lower() == "help":
        help()
    else :
        thelist.append(elements)

print "The Items In Your Shopping List Are : ", ", ".join(thelist)
