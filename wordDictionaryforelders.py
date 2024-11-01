word_dict = {
    "lol": "Something really funny",
    "lmao": "something that is REALLY REALLY funny",
    "epic": "Something that is impressive or cool"
}

word_input = input("Enter a word you would love to know").lower()

if word_input in word_dict.keys():
    print(word_dict[word_input])
else:
    print("Word doesn't exist.")
