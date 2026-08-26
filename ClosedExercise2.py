#Name: Gil-li Ness Grota - 332011865
import math

national_elections = {"Toronto" : [2800000, 38],
                      "Montreal" : [2000000 , 29],
                      "Jasper" : [4700 , 64],
                      "Vancouver" : [660000 , 87],
                      "Calgary" : [1300000 , 46],
                      "Ottawa" : [880000 , 30]}


national_elections_for_mominim = {}

for city, votes in national_elections.items():
    national_elections_for_mominim[city] = math.floor((votes[0] * votes[1]) / 100)

sum_votes_for_mominim = 0
for vote in national_elections_for_mominim.values():
    sum_votes_for_mominim += vote

print(f'The total number of votes in the country is: {sum_votes_for_mominim}')

all_votes_in_country = 0
for city, vote in national_elections.items():
       all_votes_in_country += national_elections[city][0]
print(all_votes_in_country)

print(f'The precent that votedto the Mominim is: { math.floor((sum_votes_for_mominim * 100) / all_votes_in_country) }%')


max_vote_city = 0
max_votes = 0
for city, votes in national_elections_for_mominim.items():
    if votes > max_votes:
        max_vote_city = city
        max_votes = votes

print(f"The city that voted the most for the Mominim is: {max_vote_city}")