
import textblob
from textblob import Word
import random
import nltk

#nltk.download('wordnet')

test = "this is a really hard thing to do and \n only works in english too"


def synonymize(text):
    words = text.split(" ")
    output = list()
    for word_str in words:
        word_obj = Word(word_str)
        if len(word_str) > 3 and len(word_obj.synsets) > 0:
            random_synset = random.choice(word_obj.synsets)
            random_lemma = random.choice(random_synset.lemma_names())
            output.append(random_lemma.replace('_', ' '))
        else:
            output.append(word_str)
    return (" ".join(output))

def trans_to_ger(text):
    blob = textblob.TextBlob(text)
    trans = blob.translate(to="de")
    return trans
