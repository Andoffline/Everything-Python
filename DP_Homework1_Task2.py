#Exercise2
import math
def isStrong(num):
    if num==(math.factorial(num%10000))+(math.factorial(num%1000))+(math.factorial(num%100))+(math.factorial(num%10)):
        return True
    else:
        return False


    