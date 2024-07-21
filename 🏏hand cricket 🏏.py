print(" -------------------------------------------")
print("|               HAND CRICKET                |")
print(" -------------------------------------------")
print("   *   |       🎮    🏏    🎮        |   *  ")
print(" * + * |-----------------------------| * + *")
print("   *   | ✊  👆  🤘  👌  🖖  ✋  👍  |   * ")
print("        -----------------------------")
print("_____________________________________________")
import random
print("                   TOSS               ")
print("                   ----                 ")
print("         Enter ➡  1⃣-head               ") 
print("                  2⃣-tail               ")
toss=int(input("               you choose: "))
tossface=["head","tail"]
toss_face=random.choice(tossface)
print("    -------------------------------------") 
print("   |            coin ➡   {}            |".format(toss_face))  
print("    -------------------------------------") 
print("_____________________________________________")
computerchoice=["batting","bowling"]
def player_bat_bowl():
    computer_score=0
    player_score=0
    print("          PLAYER BATTING / COMPUTER BOWLING")
    print("          ---------------------------------")
    for i in range(1,1000):
         computer=random.randrange(0,7)
         player=int(input("Enter the choice:"))
         if(player==0 and computer==0):
             print("player - ✊ , computer - ✊")
             print("PLAYER OUT")
             break
         elif(player==1 and computer==1):
             print("player - 👆 , computer - 👆")
             print("PLAYER OUT")
             break 
         elif(player==2 and computer==2):
             print("player - 🤘 , computer - 🤘")
             print("PLAYER OUT")
             break  
         elif(player==3 and computer==3):
             print("player - 👌 , computer - 👌")
             print("PLAYER OUT")
             break 
         elif(player==4 and computer==4):
             print("player - 🖖 , computer - 🖖")
             print("PLAYER OUT")
             break   
         elif(player==5 and computer==5):
             print("player - ✋ , computer - ✋")
             print("PLAYER OUT")
             break
         elif(player==6 and computer==6):
             print("player - 👍 , computer - 👍")
             print("PLAYER OUT")
             break 
         elif(player==0 and computer==1):
             print("player - ✊ , computer - 👆")
             player_score=player_score+1
         elif(player==0 and computer==2):
             print("player - ✊ , computer - 🤘")
             player_score=player_score+2
         elif(player==0 and computer==3):
             print("player - ✊ , computer - 👌")
             player_score=player_score+3
         elif(player==0 and computer==4):
             print("player - ✊ , computer - 🖖")
             player_score=player_score+4
         elif(player==0 and computer==5):
             print("player - ✊ , computer - ✋")
             player_score=player_score+5
         elif(player==0 and computer==6):
             print("player - ✊ , computer - 👍")
             player_score=player_score+6  
         elif(player==1 and computer==0):
             print("player - 👆 , computer - ✊")                 
             player_score=player_score+1
         elif(player==1 and computer==2):
             print("player - 👆 , computer - 🤘")
             player_score=player_score+1
         elif(player==1 and computer==3):
             print("player - 👆 , computer - 👌")
             player_score=player_score+1
         elif(player==1 and computer==4):
             print("player - 👆 , computer - 🖖")
             player_score=player_score+1
         elif(player==1 and computer==5):
             print("player - 👆 , computer - ✋")
             player_score=player_score+1
         elif(player==1 and computer==6):
             print("player - 👆 , computer - 👍")
             player_score=player_score+1   
         elif(player==2 and computer==0):
             print("player - 🤘 , computer - ✊")
             player_score=player_score+2    
         elif(player==2 and computer==1):
             print("player - 🤘 , computer - 👆")
             player_score=player_score+2
         elif(player==2 and computer==3):
             print("player - 🤘 , computer - 👌")
             player_score=player_score+2
         elif(player==2 and computer==4):
             print("player - 🤘 , computer - 🖖")
             player_score=player_score+2
         elif(player==2 and computer==5):
             print("player - 🤘 , computer - ✋")
             player_score=player_score+2
         elif(player==2 and computer==6):
             print("player - 🤘 , computer - 👍")
             player_score=player_score+2
         elif(player==3 and computer==0):
             print("player - 👌 , computer - ✊")
             player_score=player_score+3
         elif(player==3 and computer==1):
             print("player - 👌 , computer - 👆")   
             player_score=player_score+3
         elif(player==3 and computer==2):
             print("player - 👌 , computer - 🤘")
             player_score=player_score+3
         elif(player==3 and computer==4):
             print("player - 👌 , computer - 🖖")
             player_score=player_score+3
         elif(player==3 and computer==5):
             print("player - 👌 , computer - ✋")
             player_score=player_score+3
         elif(player==3 and computer==6):
             print("player - 👌 , computer - 👍")
             player_score=player_score+3 
         elif(player==4 and computer==0):
             print("player - 🖖 , computer - ✊")
             player_score=player_score+4
         elif(player==4 and computer==1):
             print("player - 🖖 , computer - 👆")   
             player_score=player_score+4
         elif(player==4 and computer==2):
             print("player - 🖖 , computer - 🤘")
             player_score=player_score+4
         elif(player==4 and computer==3):
             print("player - 🖖 , computer - 👌")
             player_score=player_score+4   
         elif(player==4 and computer==5): 
             print("player - 🖖 , computer - ✋")
             player_score=player_score+4
         elif(player==4 and computer==6):
             print("player - 🖖 , computer - 👍")
             player_score=player_score+4     
         elif(player==5 and computer==0):
             print("player - ✋ , computer - ✊")
             player_score=player_score+5
         elif(player==5 and computer==1):
             print("player - ✋ , computer - 👆")   
             player_score=player_score+5
         elif(player==5 and computer==2):
             print("player - ✋ , computer - 🤘")
             player_score=player_score+5
         elif(player==5 and computer==3):
             print("player - ✋ , computer - 👌")
             player_score=player_score+5    
         elif(player==5 and computer==4):
             print("player - ✋ , computer - 🖖")
             player_score=player_score+5
         elif(player==5 and computer==6):
             print("player - ✋ , computer - 👍")
             player_score=player_score+5
         elif(player==6 and computer==0):
             print("player - 👍 , computer - ✊")
             player_score=player_score+6
         elif(player==6 and computer==1):
             print("player - 👍 , computer - 👆")   
             player_score=player_score+6
         elif(player==6 and computer==2):
             print("player - 👍 , computer - 🤘")
             player_score=player_score+6
         elif(player==6 and computer==3):
             print("player - 👍 , computer - 👌")
             player_score=player_score+6  
         elif(player==6 and computer==4):
             print("player - 👍 , computer - 🖖")
             player_score=player_score+6
         elif(player==6 and computer==5):
             print("player - 👍 , computer - ✋")
             player_score=player_score+6   
    print("Batsman score -  ", player_score) 
    print("player bowling / computer batting")
    print("computer wants {} runs to win".format(player_score+1))
    for i in range(1,1000):
        computer=random.randrange(0,7)
        player=int(input("Enter the choice:"))
        if(computer==0 and player==0):
            print("computer- ✊ , player - ✊")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win") 
                break
        elif(computer==1 and player==1 ):
            print("computer - 👆 , player - 👆")
            print("COMPUTER OUT") 
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break 
        elif(computer==2 and player==2):
            print("computer - 🤘 , player - 🤘")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break  
        elif(computer==3 and player==3):
            print("computer - 👌 , player - 👌")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break 
        elif(computer==4 and player==4):
            print("computer - 🖖, player - 🖖")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break   
        elif(computer==5 and player==5):
            print("computer -✋, player -✋")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break
        elif(computer==6 and player==6):
            print("computer- 👍, player - 👍")
            print("COMPUTER OUT")
            print("computer score -  ", computer_score)
            if(computer_score<player_score):
                print("player win")             
                break 
        elif(computer== 0 and player== 1 ):  
            print("computer-✊   , player -👆 ")
            computer_score=computer_score+1
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins")
                break
        elif(computer== 0 and player== 2):  
            print("computer- ✊  , player -🤘 ")
            computer_score=computer_score+2
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins")
                break
        elif(computer== 0 and player== 3 ):  
            print("computer-  ✊ , player -👌 ")
            computer_score=computer_score+ 3
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins")
                break
        elif(computer== 0 and player== 4 ):  
            print("computer-  ✊ , player - 🖖")
            computer_score=computer_score+4
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins")
                break
        elif(computer== 0 and player== 5 ):  
            print("computer- ✊  , player -✋ ")
            computer_score=computer_score+5
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins")
                break
        elif(computer== 0  and player== 6 ):  
            print("computer-  ✊ , player -👍")
            computer_score=computer_score+ 6 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 1 and player== 0 ):  
            print("computer-👆  , player -✊ ")
            computer_score=computer_score+1
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break  
        elif(computer== 1 and player==2  ):  
            print("computer- 👆  , player - 🤘")
            computer_score=computer_score+1
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 1 and player== 3 ):  
            print("computer-  👆 , player - 👌")
            computer_score=computer_score+ 1 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break     
        elif(computer== 1 and player== 4 ):  
            print("computer- 👆  , player - 🖖")
            computer_score=computer_score+1
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 1 and player==5  ):  
            print("computer-👆  , player - ✋")
            computer_score=computer_score+1
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 1 and player== 6 ):  
            print("computer- 👆  , player - 👍")
            computer_score=computer_score+1 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break         
        elif(computer==2  and player==0  ):  
            print("computer-🤘   , player -✊ ")
            computer_score=computer_score+2 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)                
                print("computer wins") 
                break 
        elif(computer== 2 and player== 1 ):  
            print("computer-🤘   , player - 👆")
            computer_score=computer_score+2
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 2 and player== 3):  
            print("computer- 🤘  , player -👌 ")
            computer_score=computer_score+2  
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break     
        elif(computer== 2 and player== 4): 
            print("computer- 🤘  , player -🖖 ")
            computer_score=computer_score+2
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break        
        elif(computer== 2 and player== 5 ):  
            print("computer-🤘   , player - ✋")
            computer_score=computer_score+2
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 2 and player== 6 ):  
            print("computer- 🤘  , player - 👍")
            computer_score=computer_score+2
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 3 and player==0  ):  
            print("computer- 👌  , player - ✊")
            computer_score=computer_score+3  
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 3 and player== 1 ):  
            print("computer-👌   , player - 👆")
            computer_score=computer_score+3
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 3 and player==2  ):  
            print("computer- 👌  , player - 🤘")
            computer_score=computer_score+3 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break      
        elif(computer== 3 and player==4  ):  
            print("computer-  👌 , player -🖖 ")
            computer_score=computer_score+3
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 3 and player== 5):  
            print("computer-👌   , player -✋ ")
            computer_score=computer_score+3
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 3  and player== 6 ):  
            print("computer- 👌  , player -👍 ")
            computer_score=computer_score+3  
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 4 and player== 0 ):  
            print("computer- 🖖  , player - ✊")
            computer_score=computer_score+4 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break  
        elif(computer== 4 and player== 1 ):  
            print("computer- 🖖  , player -👆 ")
            computer_score=computer_score+4
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 4 and player==2 ):  
            print("computer-🖖   , player -🤘 ")
            computer_score=computer_score+4  
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break     
        elif(computer== 4 and player==  3):  
            print("computer-  🖖 , player -👌 ")
            computer_score=computer_score+4
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 4 and player== 5 ):  
            print("computer- 🖖  , player - ✋")
            computer_score=computer_score+4
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer==4  and player== 6 ):  
            print("computer- 🖖 , player -👍 ") 
            computer_score=computer_score+4
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 5 and player==0  ):  
            print("computer- ✋  , player -✊ ")
            computer_score=computer_score+5 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break  
        elif(computer==5  and player== 1 ):  
            print("computer- ✋  , player - 👆")
            computer_score=computer_score+5
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 5 and player== 2 ):  
            print("computer- ✋  , player -🤘 ")
            computer_score=computer_score+5  
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break     
        elif(computer==5  and player== 3 ):  
            print("computer- ✋  , player - 👌")
            computer_score=computer_score+5
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 5 and player== 4 ):  
            print("computer- ✋  , player -🖖 ")
            computer_score=computer_score+5
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 5 and player== 6 ):  
            print("computer- ✋ , player - 👍")
            computer_score=computer_score+5 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 6 and player== 0 ):  
            print("computer- 👍  , player -✊ ")
            computer_score=computer_score+6 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break  
        elif(computer== 6 and player== 1 ):  
            print("computer- 👍  , player -👆 ")
            computer_score=computer_score+6
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 6 and player== 2 ):  
            print("computer- 👍  , player - 🤘")
            computer_score=computer_score+6 
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break      
        elif(computer== 6 and player== 3 ):  
            print("computer-  👍 , player -👌 ")
            computer_score=computer_score+6
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 6 and player== 4 ):  
            print("computer-  👍 , player -🖖 ")
            computer_score=computer_score+6
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break
        elif(computer== 6 and player== 5 ):  
            print("computer- 👍  , player - ✋")
            computer_score=computer_score+6
            if(computer_score>player_score):
                print("computer score -  ", computer_score)
                print("computer wins") 
                break        
def player_bowl_bat():
    print("          PLAYER BOWLING / COMPUTER BATTING")
    print("          ---------------------------------")
    computer_score=0
    player_score=0
    for i in range(1,1000):
        computer=random.randrange(0,7)
        player=int(input("Enter the choice:"))
        if(computer==0 and player==0):
            print("computer-✊, player - ✊")
            print("COMPUTER OUT")
            break
        elif(computer==1 and player==1 ):
            print("computer - 👆 , player - 👆")
            print("COMPUTER OUT") 
            break 
        elif(computer==2 and player==2):
            print("computer - 🤘 , player - 🤘")
            print("COMPUTER OUT")
            break  
        elif(computer==3 and player==3):
            print("computer - 👌 , player - 👌")
            print("COMPUTER OUT")
            break 
        elif(computer==4 and player==4):
            print("computer - 🖖, player - 🖖")
            print("COMPUTER OUT")
            break   
        elif(computer==5 and player==5):
            print("computer -✋, player -✋")
            print("COMPUTER OUT")
            break
        elif(computer==6 and player==6):
            print("computer- 👍, player - 👍")
            print("COMPUTER OUT")
            break 
        elif(computer== 0 and player== 1 ):
            print("computer-✊   , player -👆 ")
            computer_score=computer_score+1
        elif(computer== 0 and player== 2):  
            print("computer- ✊  , player -🤘 ")
            computer_score=computer_score+2
        elif(computer== 0 and player== 3 ):  
            print("computer-  ✊ , player -👌 ")
            computer_score=computer_score+ 3
        elif(computer== 0 and player== 4 ):  
            print("computer-  ✊ , player - 🖖")
            computer_score=computer_score+4
        elif(computer== 0 and player== 5 ):  
            print("computer- ✊  , player -✋ ")
            computer_score=computer_score+5
        elif(computer== 0  and player== 6 ):  
            print("computer-  ✊ , player -👍")
            computer_score=computer_score+ 6 
        elif(computer== 1 and player== 0 ):  
            print("computer-👆  , player -✊ ")
            computer_score=computer_score+1
        elif(computer== 1 and player==2  ):  
            print("computer- 👆  , player - 🤘")
            computer_score=computer_score+1
        elif(computer== 1 and player== 3 ):  
            print("computer-  👆 , player - 👌")
            computer_score=computer_score+ 1 
        elif(computer== 1 and player== 4 ):  
            print("computer- 👆  , player - 🖖")
            computer_score=computer_score+1
        elif(computer== 1 and player==5  ):  
            print("computer-👆  , player - ✋")
            computer_score=computer_score+1
        elif(computer== 1 and player== 6 ):  
            print("computer- 👆  , player - 👍")
            computer_score=computer_score+1 
        elif(computer==2  and player==0  ):  
            print("computer-🤘   , player -✊ ")
            computer_score=computer_score+2 
        elif(computer== 2 and player== 1 ):  
            print("computer-🤘   , player - 👆")
            computer_score=computer_score+2
        elif(computer== 2 and player== 3):  
            print("computer- 🤘  , player -👌 ")
            computer_score=computer_score+2  
        elif(computer== 2 and player== 4): 
            print("computer- 🤘  , player -🖖 ")
            computer_score=computer_score+2
        elif(computer== 2 and player== 5 ):  
            print("computer-🤘   , player - ✋")
            computer_score=computer_score+2
        elif(computer== 2 and player== 6 ):  
            print("computer- 🤘  , player - 👍")
            computer_score=computer_score+2
        elif(computer== 3 and player==0  ):  
            print("computer- 👌  , player - ✊")
            computer_score=computer_score+3  
        elif(computer== 3 and player== 1 ):  
            print("computer-👌   , player - 👆")
            computer_score=computer_score+3
        elif(computer== 3 and player==2  ):  
            print("computer- 👌  , player - 🤘")
            computer_score=computer_score+3 
        elif(computer== 3 and player==4  ):  
            print("computer-  👌 , player -🖖 ")
            computer_score=computer_score+3
        elif(computer== 3 and player== 5):  
            print("computer-👌   , player -✋ ")
            computer_score=computer_score+3
        elif(computer== 3  and player== 6 ):  
            print("computer- 👌  , player -👍 ") 
            computer_score=computer_score+3  
        elif(computer== 4 and player== 0 ):  
            print("computer- 🖖  , player - ✊")
            computer_score=computer_score+4 
        elif(computer== 4 and player== 1 ):  
            print("computer- 🖖  , player -👆 ")
            computer_score=computer_score+4
        elif(computer== 4 and player==2 ):  
            print("computer-🖖   , player -🤘 ")
            computer_score=computer_score+4  
        elif(computer== 4 and player==  3):  
            print("computer-  🖖 , player -👌 ")
            computer_score=computer_score+4
        elif(computer== 4 and player== 5 ):  
            print("computer- 🖖  , player - ✋")
            computer_score=computer_score+4
        elif(computer==4  and player== 6 ):  
            print("computer- 🖖 , player -👍 ")
            computer_score=computer_score+4
        elif(computer== 5 and player==0  ):  
            print("computer- ✋  , player -✊ ")
            computer_score=computer_score+5 
        elif(computer==5  and player== 1 ):  
            print("computer- ✋  , player - 👆")
            computer_score=computer_score+5
        elif(computer== 5 and player== 2 ):  
            print("computer- ✋  , player -🤘 ")
            computer_score=computer_score+5  
        elif(computer==5  and player== 3 ):  
            print("computer- ✋  , player - 👌")
            computer_score=computer_score+5
        elif(computer== 5 and player== 4 ):  
            print("computer- ✋  , player -🖖 ")
            computer_score=computer_score+5
        elif(computer== 5 and player== 6 ):  
            print("computer- ✋ , player - 👍")
            computer_score=computer_score+5 
        elif(computer== 6 and player== 0 ):  
            print("computer- 👍  , player -✊ ")
            computer_score=computer_score+6 
        elif(computer== 6 and player== 1 ):  
            print("computer- 👍  , player -👆 ")
            computer_score=computer_score+6
        elif(computer== 6 and player== 2 ):  
            print("computer- 👍  , player - 🤘")
            computer_score=computer_score+6 
        elif(computer== 6 and player== 3 ):  
            print("computer-  👍 , player -👌 ")
            computer_score=computer_score+6
        elif(computer== 6 and player== 4 ):  
            print("computer-  👍 , player -🖖 ")
            computer_score=computer_score+6
        elif(computer== 6 and player== 5 ):  
            print("computer- 👍  , player - ✋")
            computer_score=computer_score+6
    print("Batsman score -  ", computer_score) 
    print("player batting / computer bowling")
    print("player wants {} runs to win".format(computer_score+1))    
    for i in range(1,1000):
        player=int(input("Enter the choice:"))
        computer=random.randrange(0,7)
        if(player==0 and computer==0):
            print("player-✊, computer - ✊")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==1 and computer==1):
            print("player-👆, computer -👆 ")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==2 and computer==2):
            print("player-🤘, computer -🤘 ")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==3 and computer==3):
            print("player-👌, computer - 👌")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==4 and computer==4):
            print("player-🖖, computer -🖖 ")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==5 and computer==5):
            print("player-✋, computer -✋ ")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break
        elif(player==6 and computer==6):
            print("player-👍, computer -👍 ")
            print("PLAYER OUT")
            print("Player score -  ",player_score)
            if(player_score<computer_score):
                print("computer win") 
                break  
        elif(player== 0 and computer== 1 ):
            print("player- ✊ , computer - 👆")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 0 and computer== 2 ):  
            print("player-✊  , computer -🤘 ")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 0 and computer== 3 ):  
            print("player- ✊ , computer -👌 ")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score - ", player_score)
                print("player wins")
                break 
        elif(player==0  and computer== 4 ):  
            print("player- ✊ , computer - 🖖")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==0  and computer== 5 ):  
            print("player- ✊ , computer - ✋")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 0 and computer== 6 ):  
            print("player- ✊ , computer -👍 ")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score) 
                print("player wins")
                break 
        elif(player== 1 and computer== 0 ):  
            print("player- 👆 , computer -✊ ")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 1 and computer== 2 ):  
            print("player- 👆 , computer - 🤘")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 1 and computer== 3 ):  
            print("player- 👆 , computer 👌 ")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break
        elif(player== 1 and computer== 4 ):  
            print("player- 👆 , computer - 🖖")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 1 and computer==5  ):  
            print("player-👆  , computer -✋ ")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 1 and computer==6  ):  
            print("player- 👆 , computer -✋ ")
            player_score=player_score+1
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break   
        elif(player==2  and computer== 0 ):  
            print("player-🤘  , computer - ✊")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 2 and computer== 1 ):  
            print("player-🤘  , computer - 👆")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break
        elif(player== 2 and computer==3  ):  
            print("player- 🤘 , computer - 👌")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 2 and computer==4  ):  
            print("player- 🤘 , computer - 🖖")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 2 and computer==5  ):  
            print("player- 🤘 , computer - ✋")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==2  and computer==6  ):  
            print("player- 🤘 , computer - 👍")
            player_score=player_score+2
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break  
        elif(player==3  and computer==0  ):  
            print("player- 👌 , computer -✊ ")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 3 and computer== 1 ):  
            print("player- 👌 , computer - 👆")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 3 and computer==2  ):  
            print("player- 👌 , computer - 🤘")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==3  and computer==4  ):  
            print("player-  👌, computer -🖖 ")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 3 and computer== 5 ):  
            print("player- 👌 , computer - ✋")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==3  and computer== 6 ):  
            print("player- 👌 , computer -👍 ")
            player_score=player_score+3
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break     
        elif(player==4  and computer==0  ):  
            print("player-  🖖, computer - ✊")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 4 and computer== 1 ):  
            print("player- 🖖 , computer - 👆")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 4 and computer== 2 ):  
            print("player- 🖖 , computer - 🤘")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==4  and computer== 3 ):  
            print("player- 🖖 , computer - 👌")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player==4  and computer== 5 ):  
            print("player- 🖖 , computer - ✋")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 4 and computer== 6 ):  
            print("player- 🖖 , computer - 👍")
            player_score=player_score+4
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break  
        elif(player== 5 and computer== 0 ):  
            print("player- ✋ , computer -✊ ")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 5 and computer== 1 ):  
            print("player- ✋ , computer - 👆")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 5 and computer== 2 ):  
            print("player- ✋ , computer - 🤘")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)               
                print("player wins")
                break 
        elif(player== 5 and computer==3  ):  
            print("player- ✋ , computer - 👌")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 5 and computer==4  ):  
            print("player-✋  , computer - 🖖")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 5 and computer== 6 ):  
            print("player-✋  , computer - 👍")
            player_score=player_score+5
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break    
        elif(player==6  and computer== 0 ):  
            print("player- 👍 , computer - ✊")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 6 and computer==1  ):  
            print("player- 👍 , computer - 👆")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 6 and computer== 2 ):  
            print("player- 👍 , computer - 🤘")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 6 and computer== 3 ):  
            print("player- 👍 , computer - 👌")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 6 and computer== 4 ):  
            print("player- 👍 , computer - 🖖")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break 
        elif(player== 6 and computer== 5 ):  
            print("player- 👍 , computer - ✋")
            player_score=player_score+6
            if(player_score>computer_score):
                print("player score -  ", player_score)
                print("player wins")
                break                     
if(toss==1):
    if(toss_face=="head"):
        print("player won the toss")
        print("Enter       1⃣-batting ") 
        print("            2⃣-bowling :")
        player_choice=int(input("           you choose: "))
        print("_____________________________________________") 
        if(player_choice==1):  
            player_bat_bowl() 
        elif(player_choice==2):
            player_bowl_bat() 
        else:
            print("Enter only 1 or 2 !")   
    else:
        print("computer won the toss") 
        computer_choice=random.choice(computerchoice)
        print("computer choosed ",computer_choice)
        print("_____________________________________________")
        if(computer_choice=="batting"):  
           player_bowl_bat()                
        else:
            player_bat_bowl()
elif(toss==2):
    if(toss_face=="tail"):
        print("player won the toss")
        print("Enter       1⃣-batting ") 
        print("            2⃣-bowling ")
        player_choice=int(input("           you choose: ")) 
        print("_____________________________________________")
        if(player_choice==1):  
            player_bat_bowl() 
        elif(player_choice==2):
            player_bowl_bat() 
        else:
            print("Enter only 1 or 2 !")   
    else:
        print("computer won the toss") 
        computer_choice=random.choice(computerchoice)
        print("computer choosed ",computer_choice)
        print("_____________________________________________")
        if(computer_choice=="batting"):  
           player_bowl_bat()                
        else:
            player_bat_bowl()
else:
    print("Enter only 1 or 2 !")
                
                    
                  
    