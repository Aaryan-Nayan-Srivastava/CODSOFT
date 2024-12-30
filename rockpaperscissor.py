import random
"""
Basic matrix of snake water gun
         R(0)  P(1) S(2)
    R(0)   D   L   W
    P(1)   W   D   L
    S(2)   L   W   D
    d=0
    w=1
    l=-1
"""

print('_'*100,'\n')
print("Welcome to Rock Paper Scissor Game\n")
print('_'*100,'\n')
name=input("what is your name:\n")
print('_'*100,'\n')
print(f"Hello {name}\n")
print('_'*100,'\n')
score=0
while True:
    print("Choices:\nrock\npaper\nscissor\n")
    user=input("Enter your choice:")
    user.lower()
    ch=['rock','paper','scissor']
    comp=random.choice(ch)
    print('_'*100,'\n')
    print(f"Your choice:{user}\n")
    print(f"Computer's choice:{comp}\n")
    print('_'*100,'\n')
    if(user==comp):
        print("Draw!!")
        score=score +0
    elif(user=='rock'):
        if(comp=='scissor'):
            print("You won!!")
            score=score +1
        else:
            print("You lost!!") 
            score=score -1   
    elif(user=='paper'):
        if(comp=='rock'):
            print("You won!!")
            score=score +1
        else:
            print("You lost!!")
            score=score -1     
    elif(user=='scissor'):
        if(comp=='paper'):
            print("You won!!")
            score=score +1
        else:
            print("You lost!!")
            score=score -1
    print("\n")
    print('_'*100,'\n')
    print(f"Your score:{score}\n")
    play_again=input("Play Again?(y/n)\n")  
    if(play_again=='n'):
        print("Thanks for playing!!\n")
        break
    print('_'*100,'\n')
