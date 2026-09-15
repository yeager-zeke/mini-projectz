import random
import time
user=input("enter your name to start the game :")
time.sleep(3)
print("WELCOME !",user, " its good to see you ")
time.sleep(2)
while True:
    cho=int(input("what level of difficulty do you want \nenter 1 for easy \nenter 2 for moderate \nenter 3 for hard "))
    if cho==1:
        print("you have chosen the easy level. \nIn this level the system will pick a number between 0 and 50, and you have to guess the number correctly \n(ONLY 5 ATTEMPTS ALLOWED) ")
        a=random.randint(0,50)
        p=0
        while p!=5:
            ch=int(input("guess the number :"))    
            if ch==a:
                print("CORRECT GUESS !!")
                break        
            else:
                p+=1
                if ch>a:
                    print("try a smaller number....")
                else:
                    print("try a larger number")
                print("you have only",5-p,"attempts left" )
    if cho==2:
        print("you have chosen the moderate level. \nIn this level the system will pick a number between 0 and 100, and you have to guess the number correctly \n(ONLY 10 ATTEMPTS ALLOWED) ")
        a=random.randint(0,100)
        p=0
        while p!=10:
            ch=int(input("guess the number :"))    
            if ch==a:
                print("CORRECT GUESS !!")
                break        
            else:
                p+=1
                if ch>a:
                    print("try a smaller number....")
                else:
                    print("try a larger number")
                print("you have only",10-p,"attempts left" )
    if cho==3:
        print("you have chosen the hard level. \nIn this level the system will pick a number between 0 and 500, and you have to guess the number correctly \n(ONLY 15 ATTEMPTS ALLOWED) ")
        a=random.randint(0,500)
        p=0
        while p!=15:
            ch=int(input("guess the number :"))    
            if ch==a:
                print("CORRECT GUESS !!")
                break        
            else:
                p+=1
                if ch>a:
                    print("try a smaller number....")
                else:
                    print("try a larger number")
                print("you have only",15-p,"attempts left" )
    rep=input("DO YOU WANT TO REPLAY THE GAME ?? (Y/N)")
    if rep.lower()=="n":
        print("WE ARE SORRY TO SEE YOU GOING..")
        break
time.sleep(4) 

#==============================================SCRIPT_END=============================================






            
    



    
   
        




