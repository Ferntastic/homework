import sys
choice_list = [' .^.   1', ' <--   2', ' -->   3', ' <v>   4']
#Lets see if someone can build a crude looking airplane


print ("                               Welcome to Boeing")

print ("The faster you build an airplane the better, but be careful. You only get 2 chances. ;-)")

print ('Choose the nose of the airplane first. You will end with the tail')



for c in choice_list:
    print (c)
    
choice_a= int(input('Pick the number next to the nose '))

while choice_a== 1:
    print('Correct')
    break
    
else:
    print('Try again')
    choice_a= int(input('Pick the number next to the nose '))
    while choice_a== 1:
        print('Correct')
        break
    else:
        print('You Lose')
    sys.exit()
        
    
choice_b= input('Pick the number next to the left wing ')
    
while choice_b== 2:
    print('Correct')
    break
   
else:
    print('Try again')
    choice_b= input('Pick the number next to the left wing ')
    while choice_b== 2:
        print('Correct')
        break
    else:
        print('You Lose')
    sys.exit()
    
    
choice_c= input('Pick the number next to the right wing ')
    
while choice_c== 3:
    print('Correct')
    break
    
else:
    print('Try again')
    choice_c= input('Pick the number next to the right wing ')
    while choice_c== 3:
        print('Correct')
        break
    else:
        print('You Lose')
    sys.exit()
        
choice_d= input('Pick the number next to the tail ')

while choice_d== 4:
    print('Correct')
    break
else:
    print('Try again')
    choice_d= input('Pick the number next to the tail ')
    while choice_d== 4:
        print('Correct')
        break
    else:
        print('You Lose')
print ('  .^.')
print ('<----->')
print ('  <v>')
