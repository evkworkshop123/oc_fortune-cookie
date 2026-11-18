
#import random
import random

def main():
    adj1= get_words_from("adjectives.txt")
    adj2= get_words_from("adjectives.txt")
    noun= get_words_from("nouns.txt")
    item= get_words_from("items.txt")

    print(f"You will draw {a_or_an(adj1)} {noun} with {a_or_an(adj2)} {item}")
# Will need a text/csv file with the words to be used in the sentence structure. 

# Use the randrange method to fill the variables: adjective, species and attribute. With a corresponding example

def a_or_an(word):
    """Looks at the first letter in a word and judges whether or not to put a or an in front of it.
    
    :param word: The word to look at
    :type word: str
    
    :return: a, or an
    :rtype: str """
    if word[0].lower() in "aeiou":
        return f"an {word}"
    else:
        return f"a {word}"

def get_words_from(txt_file):
    """Reads a text file and returns a list of words from it

    :param txt_file: The name of the text file to get words from
    :type txt_file: str

    :return: A word from the chosen file
    :rtype: str
    """
    with open (txt_file) as wordfile:
        word_list = list(wordfile)
        picked_word = random.randrange(len(word_list))

    return pick_random(word_list)
# this uses the below function to pick from the finished list

def pick_random(words):
    return random.choice(words).strip()

# create and print a simple sentence like print(f"You will draw: An {Adjective} {Species} {Occupation/Attribute})
if __name__ == "__main__":
    main()