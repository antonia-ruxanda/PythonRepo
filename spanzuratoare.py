import random
from random_word import list_of_random_words
word = random.choice(list_of_random_words)
word_list = []
unique_letter = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())

word_length = len(unique_letter) - 2
print(" ".join(word_list))
count_nr = 1
list_already_checked = []
new_word = " ".join(word_list)
while count_nr <= word_length:
    user_letter = input("Choose a letter: ").lower()
    if user_letter == "":
        print("Enter a letter")
        continue
    if user_letter in word_list:
        print("Letter already on the screen")
    elif user_letter in list_already_checked:
        print(f"Letter was tried, letters already checked are: {''.join(list_already_checked)}")
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))
        else:
            count_nr += 1
        if '_' not in "".join(word_list):
            print("You won!")
            break
        elif count_nr > word_length:
            print(f"You lost! The word was {word}")
        list_already_checked.append(user_letter)