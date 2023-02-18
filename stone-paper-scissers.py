import random as r

print("WELCOME TO THE STONE, PAPER , SCISSORS.....")
print("LET'S START THE GAME...")

choices = ["stone", "scissors", "paper"]

user = input("ENTER YOUR CHOICES TO START THE GAME: ")
#suppose the user given the wrong input...
while user not in choices:
    user = input(f"Your choice {user} is not valid Please select stone,paper,scissors: ")

sys = r.choice(choices)


print(f"user: {user}")
print(f"system: {sys}")

#to check wheather the user's choice and the system choice is similar or different
#if user"choice and the system's choice is same then the game is tie
#if user's choice is rock and sys choice is paper then you lose and vice versa then


if user == sys:
    print("TIE....GAME OVER...")
elif ((user == "paper" and sys == "scissors") or (user == "stone" and sys == "paper") or (user == "scissors" and sys == "stone")):
    print("OOPS!!..YOU LOSE :(")
elif ((user == "scissors" and sys == "paper") or (user == "paper" and sys == "stone") or (user == "stone" and sys == "scissors")):
    print("HURRAY!!...YOU WON THE GAME OVER :)") 
else : 
    print("SOMETHING WENT WRONG.....")