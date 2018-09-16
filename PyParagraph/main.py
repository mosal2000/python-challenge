# -*- coding: utf-8 -*-
"""
Created on Sat September ‎14, ‎2018, ‏‎11:54:44 PM

@author: Mohammad Ronosentono
"""
import os
import re

candidate_list = []
candidate_total_data = []

# Path to collect data from the Resources folder
paragraphTXT = os.path.join("raw_data", "paragraph_1.txt")

# Read in the CSV file
with open(paragraphTXT, 'r') as txtfile:
    paragraph = txtfile.read()

# ---------------- Split based on sentences ---------------- 
split_sentences = re.split("(?<=[.!?]) +", paragraph)

total_words = []
number_of_sentences = 0

for sentence in split_sentences:
    words_in_sentence = re.split("(?<=\W)(?=\w)|(?<=\w)(?=\W) +", sentence)
    num_words = len(words_in_sentence)
    total_words.append(num_words)
    number_of_sentences += 1

#Average words per sentence
average_words_count = sum(total_words)/number_of_sentences

# ---------------- Split based on words ---------------- 
split_words = re.split("(?<=\W)(?=\w)|(?<=\w)(?=\W) +", paragraph)

# Average Letters count per word
total_letters = 0
number_of_words = 0
for word in split_words:
    letters = len(word)
    #print(letters)
    total_letters += letters
    number_of_words += 1
    
average_letters_count = total_letters/number_of_words

## ---------------- Print Result ---------------- 
header = "Paragraph Analysis"
dashes = "-------------------------" 

print("\n")
print(header)
print(dashes)
print("Approximate Word Count: " + str(len(split_words)))
print("Approximate Sentence Count: " + str(len(split_sentences)))
print("Average Letter Count: " + str(average_letters_count))
print("Average Sentence Length: " + str(average_words_count))
print("\n\n")

# -------- Write Result to file-------- 
with open("PyParagraph.txt","w") as txtfile:
    txtfile.write(header + "\n") 
    txtfile.write(dashes + "\n") 

    txtfile.write("Approximate Word Count: " + str(len(split_words)) + "\n") 
    txtfile.write("Approximate Sentence Count: " + str(len(split_sentences)) + "\n") 
    txtfile.write("Average Letter Count: " + str(average_letters_count) + "\n") 
    txtfile.write("Average Sentence Length: " + str(average_words_count) + "\n") 
 
    txtfile.close()