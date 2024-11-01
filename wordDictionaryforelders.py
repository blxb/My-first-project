import random

word_dict = {
    "lol": "Something really funny",
    "lmao": "something that is REALLY REALLY funny",
    "epic": "Something that is impressive or cool",
    "cringe": "Something that is pretty disappointing",
    "bff"; "It means best friends forever",
    "gf"; "It means girlfriend",
    "tbh"; "That is to be honest.",
    "gyatt"; "a person, usually a woman, with large buttocks and sometimes an hourglass figure",
    "skibidi toilet"; "A toilet that has a head sticking out of it, basically brain rotting trend.",
    "boomer"; "An elder person or homeless man",
    "bussin"; "Tastes good",
    "firee"; "This is super good",
    "shook"; "emotionally or physically disturbed",
    "sigma"; "A guy that is most respected one",
    "aura"; "Those are points for each respect or good thing you do",
    "mf"; "Basically a motherfucker",
    "womp womp"; "used as an expression of mock disappointment, often for humorous effect.",
    "pov"; "That means point of view",
    "body count"; "that means the number of people killed",
    "fein"; "FEIN is an acronym for federal employer identification number."
}

greetings = ["Hello!", "Good day, sir!", "How are you?", ":)"]

print(random.choice(greetings)
word_input = input("Enter a word you would love to know").lower()

if word_input in word_dict.keys():
    print(word_dict[word_input])
else:
    print("Word doesn't exist.")
