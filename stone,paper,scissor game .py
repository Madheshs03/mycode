import random 
print("         |  STONE , PAPER , SCISSOR  |")
print("         |   🎮     GAME      🎮     |")
print("          ---------------------------")
print("               | 🪨 , 📄 , ✂ |     ")
print("               --------------      ") 
print("_____________________________________________")
print("Enter:")
print("                1️⃣ ➡ stone   🪨 ") 
print("                2️⃣ ➡ paper   📄  ")
print("                3️⃣ ➡ scissor ✂  ")
print("_____________________________________________")
print("<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>") 
a=int(input("Enter no.of rounds: "))
print("<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>")
print()
b=a+1
score1=0
score2=0
for i in range(1,b):
   com=random.randrange(1,4)
   pla=int(input("enter the choice:"))
   if(pla==1 and com==1):
       score1=score1+0
       score2=score2+0
       print("                      you= 🪨,computer= 🪨 ")
   elif(pla==1 and com==2):
       score1=score1+0
       score2=score2+1
       print("                      you= 🪨,computer= 📄")
   elif(pla==1 and com==3):
       score1=score1+1
       score2=score2+0
       print("                      you= 🪨,computer= ✂")
   elif(pla==2 and com==1):
       score1=score1+1
       score2=score2+0
       print("                      you= 📄 ,computer= 🪨")
   elif(pla==2 and com==2):
       score1=score1+0
       score2=score2+0
       print("                      you= 📄,computer= 📄")
   elif(pla==2 and com==3):
       score1=score1+0
       score2=score2+1
       print("                      you= 📄 ,computer= ✂")
   elif(pla==3 and com==1):
       score1=score1+0
       score2=score2+1
       print("                      you= ✂,computer= 🪨")
   elif(pla==3 and com==2):
       score1=score1+1
       score2=score2+0
       print("                      you= ✂,computer= 📄")
   elif(pla==3 and com==3):
       score1=score1+0
       score2=score2+0
       print("                      you= ✂,computer= ✂ ")
   else:
       print("Enter 1, 2 or 3 only!")    
   print("______________________")  
print() 
print("_____________________________________________")  
print()
print("        ----------------------")
print("       |  player score   = {}  |".format(score1)) 
print("       |  computer score = {}  |".format(score2))
print("        ----------------------")
if(score1>score2):
    print("       |      PLAYER WINS     |")     
    print("        ----------------------")
elif(score2>score1):
    print("       |     COMPUTER WINS    |")     
    print("        ----------------------") 
else:
    print("       |         DRAW         |")     
    print("        ----------------------")    
print("_____________________________________________")    
                   