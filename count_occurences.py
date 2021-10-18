from string import punctuation
from typing import List, Dict

def add_word(word_list: List[str], word: str) -> List[str]:
    # # adds the word to the correct position sorted alphabetically
    insert_index = 0
    while insert_index < len(word_list) and word > word_list[insert_index]:
        insert_index += 1
    word_list.insert(insert_index, word)
    return word_list
    
def clean_input(words: str) -> List[str]:
    # clean input of leading and trailing punctuation
    word_list = [word.strip(punctuation) for word in words.split()]
    return word_list

def count_instances(word_list: List[str]) -> Dict[str, int]:
    # count words
    word_tracker = {}
    for word in word_list:
        if word in word_tracker:
            word_tracker[word] += 1
        else:
            word_tracker[word] = 1
    return word_tracker

def sort_by_frequency(words_and_frequency: Dict[str, int]) -> Dict[int, str]:
    # add lists alphabetically for each frequency level
    freq_tracker = {}
    for word in list(words_and_frequency.keys()):
        frequency = words_and_frequency[word]
        # if the frequency already exists, add the new word alphabetically sorted
        if frequency in freq_tracker:
            freq_tracker[frequency] = add_word(freq_tracker[frequency], word)
        else:
            freq_tracker[frequency] = [word]
    return freq_tracker

def print_results(frequency_and_words: Dict[int, str]) -> None:
    # print results by frequency
    reverse_sort = dict(sorted(frequency_and_words.items(),key=lambda x:x[0],reverse = True))
    for freq in reverse_sort:
        for word in frequency_and_words[freq]:
            print("{} {}".format(word, freq))

def run(sentence: str) -> None:
    '''
    Step 1: get the actual words by themselves in a list
    Step 2: count how often each word occurs and store this information as key-value pairs in a dict
    Step 3: group words in alphabetical order by their frequencies
    Step 4: print
    '''
    cleaned_sentence = clean_input(sentence)
    words_and_frequency = count_instances(cleaned_sentence)
    frequency_and_words = sort_by_frequency(words_and_frequency)
    print_results(frequency_and_words)

words = "From the moment the first immigrants arrived on these shores, generations of parents have worked hard and sacrificed whatever is necessary so that their children could have the same chances they had; or the chances they never had. Because while we could never ensure that our children would be rich or successful; while we could never be positive that they would do better than their parents, America is about making it possible to give them the chance. To give every child the opportunity to try. Education is still the foundation of this opportunity. And the most basic building block that holds that foundation together is still reading. At the dawn of the 21st century, in a world where knowledge truly is power and literacy is the skill that unlocks the gates of opportunity and success, we all have a responsibility as parents and librarians, educators and citizens, to instill in our children a love of reading so that we can give them the chance to fulfill their dreams."
run(words)

"""
OUTPUT:

$ python3 count_occurences.py 

the 13
that 7
is 6
and 5
of 5
to 4
we 4
a 3
children 3
could 3
give 3
have 3
never 3
opportunity 3
parents 3
their 3
they 3
be 2
chance 2
chances 2
foundation 2
had 2
in 2
or 2
our 2
reading 2
so 2
still 2
them 2
while 2
would 2
21st 1
America 1
And 1
At 1
Because 1
Education 1
From 1
To 1
about 1
all 1
arrived 1
as 1
basic 1
better 1
block 1
building 1
can 1
century 1
child 1
citizens 1
dawn 1
do 1
dreams 1
educators 1
ensure 1
every 1
first 1
fulfill 1
gates 1
generations 1
hard 1
holds 1
immigrants 1
instill 1
it 1
knowledge 1
librarians 1
literacy 1
love 1
making 1
moment 1
most 1
necessary 1
on 1
positive 1
possible 1
power 1
responsibility 1
rich 1
sacrificed 1
same 1
shores 1
skill 1
success 1
successful 1
than 1
these 1
this 1
together 1
truly 1
try 1
unlocks 1
whatever 1
where 1
worked 1
world 1
"""