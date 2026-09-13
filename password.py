#====================defining the functions used in the script============

def stronger_password():
    import random
    import time
    lth=int(input("enter the length of the password required:"))
    pasw=""
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{};:',.<>/?"
    for i in range(lth):
        pasw=pasw+random.choice(a)
    print("generating your password.......")
    time.sleep(4)
    print("generated password is:",pasw)


#============beginning of the main script=============================


pas = input("Enter your password to check the strength of the password: ")    
ch = "abcdefghijklmnopqrstuvwxyz"
num="1234567890"
special = "!@#$%^&*()-_=+[]{};:',.<>/?"
caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
st = 0
value_found=False
#==================checking for alphabets=======================
for i in pas:
    if i in ch:
        value_found=True 
if value_found:
    st+=1
    value_found=False
#==================checking for numbers==========================
for i in pas:
    if i in num:
        value_found=True
if value_found:
    st+=1
    value_found=False
#==============checking for special characters====================
for i in pas:
    if i in special:
        value_found=True
if value_found:
    st+=1
    value_found=False
#===============checking the length of the password================
if len(pas)>=8:
    st+=1
if len(pas)==0:
    print("THE PASSWORD CANNOT BE EMPTY")
if len(pas) < 8 and len(pas) > 0:
    print("THE PASSWORD SHOULD BE ATLEAST 8 CHARACTERS")
#=================CHECKING FOR CAPS APLPHABETS=====================
for i in pas:
    if i in caps:
        value_found=True
if value_found:
    st+=1 

#=================defining the strength============================
if st==1:
    print("THIS PASSWORD IS VERY WEAK")
    ch=input("do you want the system to provide a stronger password ? (Y/N)")
    if ch.lower()=="y":
        stronger_password()
    elif ch.lower()=="n":
        print("THEN MAKE A STRONGER PASSWORD YOURSELF")
if st==2:
    print("TRY A STRONGER PASSWORD")
if st==3:
    print("THE PASSWORD COULD HAVE BEEN MORE STRONGER")
if st==4:
    print("THE PASSWORD IS GOOD ENOUGH ")
if st==5:
    print("PERFECT PASSWORD")

#=====================END OF THE PROGRAM================================  




