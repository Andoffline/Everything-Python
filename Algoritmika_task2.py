# Task to determine discount and to show the summary of the product
kat=0 
while kat!='off': 
    kat=input('Category (press off to finish):') 
    if kat=='off': 
        break 
    else: 
        sum=int(input('Sum:')) 
        if kat == 'milk products': 
            print('Discount 10%. Final sum:',sum-(sum*0.1)) 
        elif kat == 'bakery': 
            print('Discount 30%. Final sum:',sum-(sum*0.3)) 
        else: print('Final sum:',sum) 
print('Shift ended.') 