#Name: Gil-li Ness Grota - 332011865
import random

names_of_the_candidates = []
votes = []

candidates = int(input("how many candidates are there?: "))
while 15 < candidates < 4:
    candidates = int(input("please enter again, you can choose between 4 and 15: "))

for i in range(candidates):
    names_of_the_candidates.append(input(f"what is the name of the candidate {i + 1}?: "))


number_of_voters = int(input("how many voters are there?: "))
while number_of_voters < 9:
    number_of_voters = int(input("please enter again, the number of voters need to be above 9: "))

for i in range(number_of_voters):
    votes.append(random.choice(names_of_the_candidates))
print(votes)



max_vote = 0
winner = ""

for vote in votes:
    if votes.count(vote) > max_vote:
        max_vote = votes.count(vote)
        winner = vote
    if votes.count(vote) == max_vote:
        if vote not in winner:
            winner = winner + ", " + vote


print(f"the winner is: {winner} : {max_vote}")
copy_of_names_of_the_candidates = names_of_the_candidates.copy()

winners = []
if "," in winner:
    print()
    split_winner = winner.split(",")
    for winner in split_winner:
        winner = winner.strip()
        if winner in copy_of_names_of_the_candidates:
            copy_of_names_of_the_candidates.remove(winner)
        while winner in votes:
            for vote in votes:
                if vote == winner:
                    votes.remove(vote)
else:
    while winner in votes:
        for vote in votes:
            if vote == winner:
                votes.remove(vote)



for name in copy_of_names_of_the_candidates:
    if name in votes:
        copy_of_names_of_the_candidates.remove(name)

for i in range(candidates - 1):
    max_vote = 0
    winner = ""

    for vote in votes:
        if votes.count(vote) > max_vote:
            max_vote = votes.count(vote)
            winner = vote
    if max_vote != 0:
        print(f"{winner} : {max_vote}")

    while winner in votes:
        for vote in votes:
            if vote == winner:
                votes.remove(vote)

for name in copy_of_names_of_the_candidates:
    print(f"{name} : 0")




