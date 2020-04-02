from textgenrnn import textgenrnn

from pathlib import Path

file = Path('E:\Docs\Lebla\Scripts\HOBot\\trump_weights.hdf5')

def textgen(train = False):

    if file.exists():
        print("using trump")
        t = textgenrnn("trump_weights.hdf5",vocab_path="./trump_vocab.json",config_path="./trump_config.json")
    else:
        print("using standard")
        t = textgenrnn()
    if train:
        t.train_from_file('E:\Docs\Lebla\Scripts\HOBot\\ai\\trump.txt', num_epochs=1)

    generation = (t.generate(1, temperature=0.5, return_as_list=True,)[0])
    return generation
