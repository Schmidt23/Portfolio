from textgenrnn import textgenrnn
import os
from pathlib import Path

file = Path(f'{os.path.curdir}\trump_weights.hdf5')

def textgen(train = False):

    if file.exists():
        print("using trump")
        t = textgenrnn("trump_weights.hdf5",vocab_path="./trump_vocab.json",config_path="./trump_config.json")
    else:
        print("using standard")
        t = textgenrnn()
    if train:
        t.train_from_file(f'{os.path.curdir}\\ai\\trump.txt', num_epochs=2)

    generation = (t.generate(1, temperature=0.5, return_as_list=True,)[0])
    return generation
