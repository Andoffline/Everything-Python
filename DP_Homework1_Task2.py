#Exercise2
import math
num=int(input())
def isStrong(num):
    num1=num
    sum=0
    while num!=0:
        temp=num%10
        sum+=math.factorial(temp)
        num=num//10
        temp=0

    if num1==sum:
        return True
    else:
        return False

print(isStrong(num))

def findStrongs(tuple):
    list=[]
    j=1
    i=0
    for i in range(tuple[0],tuple[1]):
        if(isStrong(i)==True):
            list[j]=i
            j+=1
        i+=1
    return list

range_s=int(input('Enter starting range:'))
range_e=int(input('Enter ending range:'))
tuple(range_s,range_e)
print(findStrongs(tuple(0),tuple(1)))
    