#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

CONST_VOTES = 100000
CONST_MEDIAN = CONST_VOTES/2
CONST_CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

CONST_MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, CONST_VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################

# Function that takes as input a list of votes.
# Returns a dictionary containing the result of the candidates
def results_hash(listOfVotes):
    candidates_results = {
        # Initialization of a table that will contain the results of votes by mention
        candidate: [0] * len(CONST_MENTIONS)
        for candidate in CONST_CANDIDATES.keys()
    }
    # We go through each vote and add 1 when a candidate receives a mention
    for vote in listOfVotes:
        for candidate, mention in vote.items():
            candidates_results[candidate][mention] += 1
    return candidates_results

# Function Calculate the median grade of each candidate
# Return median mention of the candidates 
def majoritary_mentions_hash(candidates_results):
    # initialisation of result
    resultMajoritaryMention = {}

    # loop on the candidate
    for candidate, candidate_result in candidates_results.items():
        cumulated_votes = 0

        # we loop on the result of the current candidate
        for mention, vote_count in enumerate(candidate_result): # enumerate : loop over something and have an automatic counter
            cumulated_votes += vote_count

            # if the votes exceeds the median
            if CONST_MEDIAN < cumulated_votes:
                
                # add a key in a dictionary
                resultMajoritaryMention[candidate] = {
                    "mention": mention,
                    "score": cumulated_votes
                }
                break
    return resultMajoritaryMention

# Funtion Sort the candidates by mention (tri à bulle)
# Retun array
def sort_candidates_by_mentions(mentions):
    unsorted = [(key, (mention["mention"], mention["score"])) for key, mention in mentions.items()]
    swapped = True

    while swapped:
        swapped = False
        for j in range(0, len(unsorted) - 1):
            if unsorted[j + 1][1] > unsorted[j][1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
                swapped = True
    
    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1],
        }
        for candidate in unsorted
    ]

##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    # Creat votes
    votes = create_votes()
    # get a dictionary containing the vote result of the candidates
    results = results_hash(votes)
    # get the majoritatry mention of the candidats
    majoritary_mentions = majoritary_mentions_hash(results)
    # Sort the candidates by mention
    sorted_candidates = sort_candidates_by_mentions(majoritary_mentions)

if __name__ == '__main__':
    main()