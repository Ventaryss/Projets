#############
## IMPORTS ##
#############

import random
import json
import pickle

import nltk
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
from tensorflow.python.framework import ops

import numpy
import tflearn

import Speech as sp
import Games as gm

###########
## CODES ##
###########

stemmer = LancasterStemmer()

with open("../JSON/Intents.json") as file:
    data = json.load(file)

try:
    x
    with open("../Pickle/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("../Pickle/data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    s
    model.load("../Model/model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("../Model/model.tflearn")


########################################################################################################################

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


########################################################################################################################

def deep_learning_Users(tag, pattern):
    with open("../JSON/Intents.json", "r") as file:
        data = json.load(file)

    data.get(tag, {}).get("patterns", []).append(pattern)

    with open("../JSON/Intents.json", 'w') as file:
        json.dump(data, file)


########################################################################################################################

def presentation():
    print("\n\n    ____   __   __    ____")
    print("   / __ \ |  |_|  |  / __ \  ______")
    print("  / /__\ \|  __|  | / /__\ \/   ___|")
    print(" /  ____  \  |_|_ |/______  \____  \ ")
    print("/__/    \__\____/_____/   \__\_____/")
    print("Version Alpha-Test 2.0.0")


########################################################################################################################

def erreur_tag(tags, inp):
    print("Le tag que vous avez sélectionné n'existe pas dans la liste des tags prédéfinis.")
    for tag in tags:
        print("- " + tag)
    print("\n- créer un nouveau tag\n")
    selected_tag = input("Tag sélectionné : ")
    found = False
    for intent in data['intents']:
        if intent['tag'] == selected_tag:
            intent['patterns'].append(inp)
            found = True
            break
    if not found:
        if selected_tag == "créer un nouveau tag":
            new_tag = input("Entrez le nom du nouveau tag : ")
            data['intents'].append({
                "tag": new_tag,
                "patterns": [inp],
                "responses": [],
                "context_set": ""
            })
            with open('../JSON/Intents.json', 'w') as file2:
                json.dump(data, file2, indent=4)
            print("Le nouveau tag", new_tag, "a été créé avec succès.")
            found = True
        if selected_tag == "quit":
            relance_discussion()
        else:
            while not found:
                print("Le tag que vous avez sélectionné n'existe pas dans la liste des tags prédéfinis.")
    else:
        with open('../JSON/Intents.json', 'w') as file3:
            json.dump(data, file3, indent=4)
        print("J'ai ajouté votre question à la liste des questions associées au tag",
              selected_tag + ".")


def relance_discussion():
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            print(random.choice(responses))
        else:
            erreur_tag()


def chat():
    presentation()
    print("\n\nBonjour, mon nom est Atlas, c'est un plaisir de vous aider (écrivez quit pour arrêter)!\n")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    print(random.choice(responses))
                    if tg['tag'] == 'hours':
                        sp.time()
                    if tg['tag'] == 'open':
                        sp.applications()
                    if tg['tag'] == 'cherche':
                        sp.net(inp)
                    if tg['tag'] == 'translate':
                        sp.traducteur(inp)
                    if tg['tag'] == 'games':
                        choice = gm.choix_jeux()
                        if choice == 0:
                            relance_discussion()
                        gm.lancer_jeux(choice)
        else:
            print("Je suis désolé, je ne comprends pas votre question. Mais je cherche toujours à pouvoir m'améliorer !")
            print("Veuillez choisir un tag parmi les suivants :\n")
            tags = [intent['tag'] for intent in data['intents']]
            for tag in tags:
                print("- " + tag)
            print("\n- créer un nouveau tag\n")
            selected_tag = input("Tag sélectionné : ")
            found = False
            for intent in data['intents']:
                if intent['tag'] == selected_tag:
                    intent['patterns'].append(inp)
                    found = True
                    break
            if not found:
                if selected_tag == "créer un nouveau tag":
                    new_tag = input("Entrez le nom du nouveau tag : ")
                    data['intents'].append({
                        "tag": new_tag,
                        "patterns": [inp],
                        "responses": [],
                        "context_set": ""
                    })
                    with open('../JSON/Intents.json', 'w') as file2:
                        json.dump(data, file2, indent=4)
                    print("Le nouveau tag", new_tag, "a été créé avec succès.")
                    found = True
                if selected_tag == "quit":
                    relance_discussion()
                else:
                    while not found:
                        erreur_tag(tags, inp)
            else:
                with open('../JSON/Intents.json', 'w') as file3:
                    json.dump(data, file3, indent=4)
                print("J'ai ajouté votre question à la liste des questions associées au tag", selected_tag + ".")


chat()
