a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
newlist=[a,b,c]
print(newlist)
def listyboi():
    listyboiv2=(a, b)
    for x in listyboiv2:
        for y in x:
            print(y)
listyboi()
t=0
print("")
def sum_of_column():
    sum = 0
    for x in newlist:
        sum += x[2]
    print(sum)
sum_of_column()
print("")
def sum_of_row():
    sum1 = 0
    y1=0
    for y1 in newlist[0]:
        sum1 += y1
    print(sum1)
sum_of_row()
print("")
def highest_check(newlist):
    highlist=(max(newlist))
    list.sort(highlist)
    print(highlist[2])
highest_check(newlist)