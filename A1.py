import random
op = ["rock" , "paper", "scissors"]
u = input(" Choose between rock, paper or scissors:")
c = random.choice(op)
print("User selected", u)
print("Computer selected", c)

if u == c:
    print("Its a draw")
elif u == "rock" and c == "scissors":
    print("The user wins because rock beats scissors")
elif u == "paper" and c == "rock":
    print("The user wins because paper beats rock")
elif u == "scissors" and c == "paper":
    print("The user wins because scissors beats paper")
else:
    print("You lost")