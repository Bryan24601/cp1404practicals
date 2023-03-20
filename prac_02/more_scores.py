import random
def main():
    results_file = open("results", "w")
    random_scores_list = generate_scores()
    for current_random_score in random_scores_list:
        if current_random_score < 0:
            status = "Invalid Score"
        elif current_random_score < 50:
            status = "Bad"
        elif current_random_score < 90:
            status = "Passable"
        else:
            status = "Excellent"
        print(f"{current_random_score} is {status}")
        results_file.write(f"{current_random_score} is {status}\n")



def generate_scores():
    random_scores_list = []
    number_of_random_scores = int(input("Number of random scores: "))
    for current_number in range(1, number_of_random_scores + 1):
        new_score = random.randint(1, 101)
        random_scores_list.append(new_score)
    return random_scores_list

main()