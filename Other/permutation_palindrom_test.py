#check if any  permutation of a word can be a palindrom
string = ["test", "civic", "ivicc"]


def test_palindrom(word):
    #test if there is at max one odd numbered amount of letters
    unique_chars = set()

    for char in word:
        if char in unique_chars:
            unique_chars.remove(char)
        else:
            unique_chars.add(char)

    return len(unique_chars) <= 1


for i in string:
    print i, test_palindrom(i)