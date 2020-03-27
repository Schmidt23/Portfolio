
import textblob
from textblob import Word
import random
import nltk

#nltk.download('wordnet')
#nltk.download('punkt')

test = "Geht das auch mit langen Satzen? Wenn man schön viele Nebensätze, wie hier zum Beispiel, aneinanderhängt, auch wenn mir etwas die Ideen ausgehen?"


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

def hann_sent(text):
    blob = textblob.TextBlob(text)
    out = []
    for sentence in blob.sentences:
        punc = sentence.tokenize()
        words = punc[:-1]
        random.shuffle(words)
        last_word =words[-1]+" "+punc[-1]
        out.append(" ".join(words[:-1]))
        out.append(last_word)
    return " ".join(out)

#print((hann_sent(test)))