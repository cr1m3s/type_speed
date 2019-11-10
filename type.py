import random
import time
import os

def words_generator(length):
    words_file = open('words.txt', 'r')
    words_list = []
    for line in words_file:
        word = line.strip()
        if length == 10:
            if len(word) < 6:
                words_list.append(word)
        if length == 40:
            if len(word) > 9:
                words_list.append(word)
        elif length != 10 and length != 40:
            words_list.append(word)
    random.shuffle(words_list)

    return words_list[:length]


def game(difficulty):
    os.system('clear')
    session_list = words_generator(difficulty)
     
    score = 0
    failures = 0
    start = time.time()

    while len(session_list) > 0:    
       
        random.shuffle(session_list)
    
        for i in session_list:
            print('\033[92m' + i + '\033[0m', end=" * ")

        user_word = input('\033[94m' + "\nYour input:\n>>> " + '\033[0m')

        if user_word in session_list:
            session_list.remove(user_word)
            score += len(user_word)
            os.system('clear')
        else:
            print('\033[91m' + "You missed! Try again" + '\033[0m')
            failures += 1

    end = time.time()
    print("Congrat! You've finished your chalange!")
    print("Your score: " + '\033[92m' + f"{score / (end - start) :2.5} "
          + '\033[0m' + "chars/sec "
          + ",failures: " + '\033[91m' + f"{failures}." + '\033[0m')
    print('\033[94m' + '~*' * 20 + '\033[0m')


if __name__ == '__main__':
    command = ''
    while command != 'Stop':
        print("You can:" + '\033[93m' +
              "\n1)Walk\n2)Fight\n3)Suffer\n4)Stop" + '\033[0m')
        command = input("Chose your destiny: ")
        commands = ['Walk', 'Fight', 'Suffer', 'Stop']
        if command == "Walk":
            game(10)
        elif command == "Fight":
            game(20)
        elif command == "Suffer":
            game(40)
        elif command not in commands:
            print('\033[91m' + "Wrong choise, try again" + '\033[0m')
