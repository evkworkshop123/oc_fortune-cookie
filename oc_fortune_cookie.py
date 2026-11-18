
#import random
import random

def main():
    adj1= get_words_from("adjectives.txt")
    adj2= get_words_from("adjectives.txt")
    noun= get_words_from("nouns.txt")
    object= get_words_from("objects.txt")

    print(f"You will draw a/an: {adj1} {noun} with an {adj2} {object}")
# Will need a text/csv file with the words to be used in the sentence structure. 

# Use the randrange method to fill the variables: adjective, species and attribute. With a corresponding example

def get_words_from(txt_file):
    """Reads a text file and returns a list of words from it

    This function opens up a text file
    :param filename: The name of the text file to get words from
    :type filename: str

    :return: A word from the chosen file
    :rtype: str
    """
    with open (txt_file) as wordfile:
        word_list = list(wordfile)
        picked_word = random.randrange(len(word_list))

    return pick_random(word_list[picked_word])
# this uses the below function to pick from the finished list

def pick_random(words):
    return random.choice(words).strip()

# create and print a simple sentence like print(f"You will draw: An {Adjective} {Species} {Occupation/Attribute})
if __name__ == "__main__":
    main()