#!/usr/bin/python
print("Content-Type: text/html\n\n")

nouns = ['dress', 'elephant', 'battery', 'raincoat', 'bed', 'carpet', 'night', 'rose', 'plastic', 'crayon', 'room', 'whale', 'ghost', 'gas', 'manchester', 'pillow', 'potato', 'glass', 'dream', 'kite', 'kitchen', 'nail', 'stone', 'honey', 'breakfast', 'needle', 'banana', 'match', 'insurance', 'forest', 'traffic', 'tomato', 'telephone', 'house', 'boy', 'planet', 'train', 'sugar', 'river', 'yacht', 'magician', 'juice', 'umbrella', 'answer', 'monkey', 'beard', 'candle', 'shampoo', 'oil', 'sandwich', 'family', 'teacher'] 
verbs = ['listen', 'edit', 'jump', 'study', 'exit', 'draw', 'write', 'coach', 'act', 'build', 'sneeze', 'plan', 'play', 'approve', 'enter', 'eat', 'walk', 'cough', 'run', 'replace', 'shout', 'paint', 'imitate', 'invent', 'dance', 'see', 'sing', 'color', 'zip', 'yank', 'complete', 'shop', 'lie', 'teach', 'touch', 'skip', 'break', 'sleep', 'scream', 'turn', 'laugh', 'win', 'describe', 'answer', 'whistle', 'read', 'buy', 'arrange', 'cry', 'create', 'drink', 'solve'] 
adjectives = ['perfect', 'grieving', 'proud', 'wild', 'different', 'clever', 'graceful', 'fine', 'ill', 'amused', 'important', 'gentle', 'defeated', 'gorgeous', 'bad', 'combative', 'silly', 'repulsive', 'horrible', 'smoggy', 'grotesque', 'talented', 'elegant', 'comfortable', 'healthy', 'poor', 'annoying', 'upse ive', 'mushy', 'tasty', 'embarrassed', 'naughty', 'thoughtless', 'clean', 'ashamed', 'strange', 'outstanding', 'evil', 'lively', 'weary', 'excited', 'depressed', 'kind', 'zealous', 'spotless', 'motionless', 'crowded', 'sleepy', 'precious', 'curious', 'nice'] 
names = ['Bill', 'Francis', 'Louis', 'Zoey', 'Coach', 'Ellis', 'Nick', 'Rochelle', 'Jim', 'Nathan']

import random

def counter(text, replace):
    y = 0
    c = 0
    while y < len(text)-len(replace):
        if text[y:y+len(replace)] == replace:
            c += 1
        y += 1
    return c

def replaceWords(text,nounList,verbList,adjectiveList):
    test1 = ['{ADJECTIVE}', '{VERB}', '{NOUN}']
    test3 = [adjectiveList, verbList, nounList]
    new = 0
    y = 0
    z = 0
    while z < 3:
        new = counter(text, test1[z])
        while y < new:
            text = text.replace(test1[z], random.choice(test3[z]), 1)
            y += 1
        y = 0
        z += 1
    return text

def replaceNames(text,name):
    i = ['{NAME1}', '{NAME2}', '{NAME3}', '{NAME4}', '{NAME5}', '{NAME6}', '{NAME7}', '{NAME8}', '{NAME9}']
    i2 = []
    temp = ''
    y = 0
    z = 0
    while y < len(i):
        temp = random.choice(name)
        if temp in i2:
            continue
        i2.append(temp)
        y += 1
    y = 0
    while y < len(i):
        temp = counter(text, i[y])
        while z < temp:
            text = text.replace(i[y], i2[y], 1)
            z += 1
        z = 0
        y += 1
    return text

text4 ='''
At that time {NAME1} had a {ADJECTIVE} dream, which gave him great
{ADJECTIVE} of heart. He dreamed that the whole land was full of many
{ADJECTIVE} {NOUN} and {NAME3}s, which burnt and {VERB} the people everywhere;
and then that he himself {VERB} with them, and that they did him mighty
injuries, and wounded him nigh to death, but that at last he overcame and
{VERB} them all. When {NAME1} woke, he sat in great {ADJECTIVE} of spirit and
pensiveness, thinking what this dream might signify, but by-and-by, when
he could by no means {VERB} himself what it might mean, to rid himself of
all his thoughts of it, he made ready with a great {NOUN} to ride out
hunting. As soon as {NAME2} was in the forest, {NAME1} saw a {ADJECTIVE} hart before him, and
spurred his {NOUN}, and {VERB} long eagerly after it, and chased until his
{NOUN} lost breath and fell down dead from under him. Then, seeing the hart
escaped and {NAME2} dead, he sat down by a {NOUN}, and {VERB} into deep
thought again. And as {NAME1} sat there alone, he thought he {VERB} the noise of
{NOUN}, as it were some thirty couple in number, and looking up he saw
coming towards him the {ADJECTIVE} beast that ever he had seen or heard tell
of, which ran towards the {NOUN} and {VERB} of the water. Its head was
like a {NAME3}'s, with a {ADJECTIVE} {NOUN}'s body and a {ADJECTIVE} {NOUN}'s tail, and it was
footed like a {ADJECTIVE} {NOUN}; and the noise was in its belly, as it were the baying
or questing of thirty couple of hounds. While it {VERB} there was no noise
within it; but presently, having finished, it {VERB} with a greater
sound than ever.
'''

html = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>
            Madlibs Assignment
        </title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1> Madlibs Assignment: The Legends Of King Arthur And His Knights </h1>
        <p>
        ''' + replaceNames(replaceWords(text4,nouns,verbs,adjectives), names) + '''
        </p>
        <img src="cover.png" alt="The book cover">
    </body>
</html>
'''
print(html)