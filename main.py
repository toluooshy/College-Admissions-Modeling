import csv
import random

def generate_applicants(size, sat, gpa):
    applicants = []
    
    index = 0
    while (index < size):
        applicant = dict({'sex': random.choice(["m", "f"]), 'sat': random.randrange(sat[0]/10,sat[1]/10)*10, 'gpa': random.randrange(gpa[0]*10,gpa[1]*10)/10})
        applicants.append(applicant)
        index += 1

    return applicants

def individual_acceptance_probability(applicant):
    sex_prob = .6 if applicant['sex'] == "f" else .4
    sat_prob = applicant['sat']/1600*.7
    gpa_prob = applicant['gpa']/4*.7
    return sex_prob*sat_prob*gpa_prob

def aggregated_acceptance_probability(applicants):
    aggregated_acceptance = 0
    for applicant in applicants:
        aggregated_acceptance += individual_acceptance_probability(applicant)
    return aggregated_acceptance/len(applicants)

def generate_combinations(applicants, size):
    if size == 0:
        return [[]]
     
    combinations = []

    for i in range(0, len(applicants)):
         
        applicant = applicants[i]
        remaining_applicants = applicants[i + 1:]
         
        remaining_applicants_combination = generate_combinations(remaining_applicants, size-1)
        for remaining_applicant in remaining_applicants_combination:
             combinations.append([applicant, *remaining_applicant])
           
    return combinations

def find_ideal_combination(combinations):
    ideal_combination = []
    max_combination_score = 0
    for combination in combinations:
        combination_score = aggregated_acceptance_probability(combination)
        if combination_score > max_combination_score:
            ideal_combination = combination
            max_combination_score = combination_score
            
    return ideal_combination

applicants = generate_applicants(16, [1350, 1600], [3.3, 4.0])
combinations = generate_combinations(applicants, 8)

print(find_ideal_combination(combinations))