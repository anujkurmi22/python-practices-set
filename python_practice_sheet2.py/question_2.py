''' WAP to print even number between 1 to 50 '''

def even():
    num = int(input('enter number in 1 to 50 range: '))
    
    if num < 1 or num > 50 :
        print("please enter valid number between range of 1 to 50 : ")
    elif num % 2 == 0:
        print('even')
    else:
        print("odd")

    # for num in range(2,51,2):
    #     print(num)
even()
