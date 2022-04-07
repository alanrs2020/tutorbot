import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from time import ctime
import colorama

colorama.init()
from colorama import Fore, Style, Back

import random
import main as bot
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat(message):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    #
    # while True:
    #     print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    #     inp = input()
    #     if inp.lower() == "quit":
    #         break

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([message]),
                                                                 truncating='post', maxlen=max_len))

    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if tag == ['questions']:
            return bot.getMessage(message)
        elif tag == ["time"]:
            return ctime()
        elif i['tag'] == tag:
           # print(tag)
           return np.random.choice(i['responses'])


        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))
