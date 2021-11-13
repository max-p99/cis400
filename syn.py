import nltk
nltk.download("all")
from nltk.corpus import wordnet
def syn(words):
    ret = []
    synonyms = []
    h_nym = []
    # antonyms = []
    # words = input()
    for word in words.split():
        syn_list = []
        for syn in wordnet.synsets(word):
            for hypernym in syn.hypernyms():
                # print (hypernym)
                h_nym.append(hypernym)
            for l in syn.lemmas():
                syn_list.append(l.name())
                # if l.antonyms():
                #     antonyms.append(l.antonyms()[0].name())


        synonyms.append(syn_list)
    for l in synonyms:
        ret += l
    print((ret))
    return ret
# syn("cat")
# lookup(synonyms)

# print(set(antonyms))
#python3 syn.py apple banana cat mouse dog
#[]

# text file
# fd -> tags
# csv of all imgs -> tags
# read in
# data struct

# img_01.jpg cat woman

#python3 syn.py lady
#kitten

#ret fd

#rec to tatto artist
# map places -> things they good at  NLP

#
