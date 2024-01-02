import random
import game_data
import art


def print_format(celebrity):
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}."


def answer_checker(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == 'A'
    else:
        return guess == 'B'


def pick_celebrity():
    return random.choice(game_data.data)


def game():
    game_over = False
    score = 0
    print(art.logo)

    celebrity_1 = pick_celebrity()
    celebrity_2 = pick_celebrity()

    if celebrity_1 == celibrity_2:
        celebrity_2 = pick_celebrity()
    
    while not game_over:
        print("Compare A:" + print_format(celebrity_1) + art.vs + "B: " + print_format(celebrity_2))

        users_answer = input("Who has more followers? 'A' or 'B': ").upper()
        result = answer_checker(users_answer, celebrity_1['follower_count'], celebrity_2['follower_count'])
        if result:
            score += 1
            celebrity_1 = celebrity_2
            celebrity_2 = pick_celebrity()
            print(f"You got it right! Your current score is {score}")
        else:
            print(result)
            print(f"You were wrong! Your final score is {score} points.")
            game_over = True


game()
