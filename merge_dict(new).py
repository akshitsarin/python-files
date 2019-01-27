# Write a Python program to combine two dictionary adding values for common keys.
# Ignore the keys which are not common in both the dictionaries.

dict_1 = {}
elem_1 = input("Enter The Number Of Elements In First Dictionary  : ")
for i in range (0,elem_1):
    keys = raw_input("Enter The Key : ")
    val = raw_input("Enter The Value : ")
    dict_1[keys]=val

dict_2 = {}
elem_2 = input("Enter The Number Of Elements In Second Dictionary : ")
for j in range (0,elem_2):
    key = raw_input("Enter The Key : ")
    val = raw_input("Enter The Value : ")
    dict_2[keys]=val

print "First Dictionary Is : ", dict_1 ,"\n","Second Dictionary Is : ", dict_2

for ke,va in dict_1 :
    for keyy,vall in dict_2:
        if dict_1[keys]==dict_2[keys]:
            va = va + vall
        else :
            dict_1[keyy]=vall

print "New Dictionary Is ", dict_1
