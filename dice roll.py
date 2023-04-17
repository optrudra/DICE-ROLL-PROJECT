import random
while True :
    user_input=input('Enter r to roll the dice and another char to exit ')
    rand_num=random.randint(1,6)
    if(user_input=='r'):
        print(rand_num)
    else:
        print('bye')
        break