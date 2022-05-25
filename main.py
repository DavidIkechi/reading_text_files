# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

def read_file_content(filename):
    # open the file for readding
    get_file = open(filename, "r")
    # read the file
    read_file = get_file.read()
    # close the file
    get_file.close()
        
    return read_file


def count_words():
    
    # This function cleans a word by replacing all punctuation with an empty string
    def clean_word(word_to_clean):
        return word_to_clean.translate(str.maketrans("","", string.punctuation))
    
    text = read_file_content("./story.txt")
    # create an empty dictionary to hold the count word
    count_dict = {}
    
    # remove trailing spaces at the beginning and end of the string
    text = text.strip()
    # convert characters to lowercase, we assume we don't need the characters to be case sensitive
    text = text.lower()
    # breaking words in the text into a list of words
    text = text.split()
    
    # iterate through every word in the splitted text
    for word in text:
        # remove any punctuation if present.
        new_word = clean_word(word)
        # check if the new word is already in the dictionary, if yes, increment its count by 1
        if new_word in count_dict:
            count_dict[new_word] += 1
        else:
            count_dict[new_word] = 1
            
    # return the count dictionary
    return count_dict


print(count_words())
    
    
