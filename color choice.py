print("                               NUMBER MATCH CHALLANGE")
print("                               ---------------------")
print("                    you have only 2 hints to chech the number ")
print("                              enter 'h'- hint")
print("                Enter numbers from 1-6 with space between each number")
print("                                  eg:Enter the number: 1 5 4 3 2 6")
print("                               ---------------------")
import random as rd
number=['1','2','3','4','5','6']
player=[]
rd.shuffle(number)
hint=2
while True:
    match=0
    player=input("Enter the number: ").split(" ")
    if player[0]=="h":
        if hint!=0:
            x=rd.choice(number)
            number_index=number.index(x)
            print("HINT- number:",x,"placed in: ",number_index+1)
            hint-=1
        else:
            print("Hint over")
    else:
        print(player)
        for i,j in zip(number,player):
            if i==j:
                match+=1
        print("matched colour: ",match)
        if match==6:
            break
print("-------------------------------------------------------")   
print("Congratulations! You have matched all colors correctly!")
print("-------------------------------------------------------")  
