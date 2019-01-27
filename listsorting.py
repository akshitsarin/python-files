# List Sorting By Elements At Any Place :

i = 0
oglist = []
ind_list = []
number = input ("Enter number of lists : ")
numelem = input ("Enter number of elements per list : ")

for x in range (0,number):
    while i<numelem :
        print "Enter element at place :",i
        element = input()
        ind_list.append(element)
        i+=1
    if i == numelem :
        i=0
        oglist.append(ind_list)
        ind_list = []
        print "Enter Elements Of New List"
print oglist

from operator import itemgetter

y = input ("Sort by element at place : ")
print sorted(oglist ,key = itemgetter(y))