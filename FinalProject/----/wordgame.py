# coding=utf-8
import random

LEXICON_FILE = "Lexicon.txt"


def play_game(secret_word):
    lenth=len(secret_word)-1
    INITIAL_GUESSES = 8
    word=""
    for i in range(lenth):
        word+='-'
    print("The word now looks like this: "+ word)
    print("You have "+ str(INITIAL_GUESSES)+" guesses left")
    while INITIAL_GUESSES>0:
        ip=input("Type a single letter here, then press enter: ")
        upper_ip=ip.upper()
        if upper_ip in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i]==upper_ip:
                   if i+1==lenth:
                     word=word[:i] + upper_ip
                   else:
                     word=word[:i] + upper_ip + word[i+1:]
            print("That guess is correct.")
            print("The word now looks like this: "+ word)
            print("You have "+ str(INITIAL_GUESSES)+" guesses left")
        if upper_ip not in secret_word:
            if INITIAL_GUESSES!=1:
             INITIAL_GUESSES-=1
             print("There are no "+ip.upper()+"'s in the word")
             print("The word now looks like this: "+ word)
             print("You have "+ str(INITIAL_GUESSES)+" guesses left")
            else:
              INITIAL_GUESSES-=1
              print("There are no "+ip.upper()+"'s in the word")
        if '-' not in word:
            print("Congratulations, the word is: "+str(word))
            break
    if '-' in word:
        print("Sorry, you lost. The secret word was: "+ str(secret_word))

def get_word():
    file=open(LEXICON_FILE,encoding="UTF-8")
    l=[]
    for line in file:
        l.append(line)
    ans=random.choice(l)
    return ans


def main():
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()