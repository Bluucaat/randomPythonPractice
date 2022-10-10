import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1.lower() == 'rock'.lower():
        if u2.lower() == 'scissors'.lower():
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1.lower() == 'scissors'.lower():
        if u2.lower() == 'paper'.lower():
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1.lower() == 'paper'.lower():
        if u2.lower() == 'rock'.lower():
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))