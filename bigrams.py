# Write a function find_bigrams to take a string and return a list of all bigrams

# Example:
# sentence = 
# Have free hours and love children?
# Drive kids to school, soccer practice
# and other activities.

# def find_bigrams(sentence) ->

#  [('have', 'free'),
#  ('free', 'hours'),
#  ('hours', 'and'),
#  ('and', 'love'),
#  ('love', 'children?'),
#  ('children?', 'drive'),
#  ('drive', 'kids'),
#  ('kids', 'to'),
#  ('to', 'school,'),
#  ('school,', 'soccer'),
#  ('soccer', 'practice'),
#  ('practice', 'and'),
#  ('and', 'other'),
#  ('other', 'activities.')]

# At its core, bigrams are two words that are placed next to each other. Two words versus one 
# in feature engineering for a NLP model gives an interaction effect.

# To actually parse them out of a string, we need to first split the input string. 
# We would use the python function .split() to create a list with each individual word as an input. 
# Create another empty list that will eventually be filled with tuples.

# Then, once we’ve identified each individual word, we need to loop through k-1 times 
# (if k is the amount of words in a sentence) and append the current word and subsequent word 
# to make a tuple. This tuple gets added to a list that we eventually return. 
# Remember to use the python function .lower() to turn all the words into lowercase!

sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."

def find_bigrams(sentence):
    # first split the input string
    input_list = sentence.split()
    # Create another empty list that will eventually be filled with tuples.
    bigram_list = []
    # Then, once we’ve identified each individual word, we need to loop through k-1 times 
    # (if k is the amount of words in a sentence) and append the current word and subsequent word 
    # to make a tuple. 
    # This tuple gets added to the list that we eventually return.
    for i in range(len(input_list)-1):
        bigram_list.append((input_list[i].lower(), input_list[i+1].lower()))

    return bigram_list

print(find_bigrams(sentence))