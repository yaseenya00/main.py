import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' ,'q', 'r', 's','t', 'q', 'r', 's', 't','U', 'v', 'w', 'x','y','z']
symbol = ['@','#','$','%','&','(']
numbers= ['7','6','5','4','3','2','1','0','8','9',]

nrl_letter= int(input("how many letters u want:"))
nrl_symbol= int(input("how many symobls u want"))
nrl_numbers=int(input(" how many numbers u want"))

'''for char in range(1,nrl_letter+1):
    password+=random.choice(letter)
for char in range(1,nrl_symbol+1):
    password+=random.choice(symbol)
for char in range(1,nrl_numbers+1):
    password+=random.choice(numbers)
    print(password)'''
password_list = []
for char in range(1,nrl_letter+1):
    password_list.append(random.choice(letter))
for char in range(1,nrl_symbol+1):
    password_list+=random.choice(symbol)
for char in range(1,nrl_numbers+1):
    password_list+=random.choice(numbers)

    #print(password_list)#
    random.shuffle(password_list)
  #  print(password_list)#

    password="".join(password_list)

    print(f"ur password is {password}")


   # print(password)#



