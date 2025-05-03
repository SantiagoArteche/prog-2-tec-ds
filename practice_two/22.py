amount_of_candidates = int(input("Insert the amount of candidates: "))

iteration1 = 0

results = {}
while(amount_of_candidates > iteration1):
    candidate_name = input("Insert the name of the candidate: ")
    amount_of_states = int(input("Insert the amount of states: "))
    iteration2 = 0
    while(amount_of_states > iteration2):
        state_name = input("Insert the name of the state: ")
        state_votes = int(input("Insert the amount of votes: "))
        if(candidate_name in results):
            results[candidate_name] = results.get(candidate_name) + [(state_name, state_votes)] 
        else:
            results[candidate_name] = [(state_name, state_votes)]
        iteration2 += 1
    iteration1 += 1

for key, value in results.items():
    val_response = ""
    for val in value:
        val_response += f"Province: {val[0]}, Votes: {val[1]} \n"
    print(f"Candidate name: {key}, {val_response}")
