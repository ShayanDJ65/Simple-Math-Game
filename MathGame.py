import random,time 
x = random.randint(0,50)
y = random.randint(0,50)
z = 0 
def new_num(): #Making a random number
    global y 
    global x
    x = random.randint(0,50)
    y = random.randint(0,50)
# Plus
def jam():
    global y 
    global x 
    global z
    z = x+y
    return z
# substraction
def tafrigh():
    global x
    global y 
    global z
    z = x - y 
    return z
# mulitpling
def zarb():
    global x 
    global y 
    global z
    z=x*y
    return z
#Dividing
def taghsim():
    global x 
    global y 
    global z
    z= x/y
    return z
score= 0 
user_answer = 0
name = input("Welcome to the math game! Please enter your name: ")
print("Well {} ! Let's begin...".format(name))
time.sleep(1.8) 
for i in range(11): # 10 chances 
    option = input("\nPlease choose one option:\n1.Add\n2.Substract\n3.Multiplying\n4.Dividing\n")
    if option =="1":
        user_answer =int(input("{} + {} = ? ".format(x,y)))
        jam()
        if user_answer==z:
            score+=1
            print("Well done! You've gained one score!")
            new_num()
        else:
            score-=1
            print("Oops! You' lost one score!") 
            new_num()
    if option == "2":
        user_answer =int(input("{} - {} = ? ".format(x,y)))
        tafrigh()
        if user_answer==z:
            score+=1
            print("Well done! You've gained one score!")
            new_num()
        else:
            score-=1
            print("Oops! You' lost one score!")
            new_num()
    if option == "3":
        user_answer =int(input("{} * {} = ? ".format(x,y)))
        zarb()
        if user_answer==z:
            score+=1
            print("Well done! You've gained one score!")
            new_num()
        else:
            score-=1
            print("Oops! You' lost one score!")
            new_num()
    if option == "4":
        user_answer =int(input("{} / {} = ? ".format(x,y)))
        taghsim()
        if user_answer==z:
            score+=1
            print("Well done! You've gained one score!")
            new_num()
        else:
            score-=1
            print("Oops! You' lost one score!")
            new_num()        
    if i==10:
        time.sleep(0.5)
        print("The game is over!, Calculationg your score...")
        time.sleep(2)
        print("Your Score is {}".format(score))