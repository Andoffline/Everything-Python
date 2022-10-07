#Exercise 1
classroom = ['john', 'maria', 'maria', 'ahmet', 'eleni', 'rho', 'john', 'maria', 'jules']
#Function used to count number of times name is mentioned in the list
def count(list,name):
    count=0
    i=0
    while i in range(0,len(list)):
        if list[i]==name:
            count+=1
            i+=1
        else:
            i+=1
    return count
name=input('Enter name of student:')
print(count(classroom,name))



    