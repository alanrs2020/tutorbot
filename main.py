from newspaper import Article
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia as wiki
from googlesearch import search
import warnings

warnings.filterwarnings('ignore')

nltk.download("punkt", quiet=True)


def greeting_response(text):
    text = text.lower()

    bot_greetings = ['Hi', 'Hello how can I help you', 'Hey', 'Hi, how can i help you']

    user_greetings = ['hi', 'hello', 'hey', 'hy', 'halo']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var

    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


def bot_reply(message, sentence_list):
    message = message.lower()
    # print("bot:", message)
    sentence_list.append(message)
    bot_reply = ' '
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_score = cosine_similarity(cm[-1], cm)
    similarity_score_list = similarity_score.flatten()
    index = index_sort(similarity_score_list)
    index = index[1:]
    reply_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_score_list[index[i]] > 0.0:
            bot_reply = bot_reply + " " + sentence_list[index[i]]
            reply_flag = 1
            j = j + 1

        if j > 2:
            break

    if reply_flag == 0:
            bot_reply = bot_reply + " " + "Sorry, I don't have an answer"
    sentence_list.remove(message)
    return bot_reply


def getText(message):
    i = 0
    response = search(message)
    token_list1 = []
    token_list2 = []
    for link in response:

        try:
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            sentence_list = article.text
            token_list1 = nltk.sent_tokenize(sentence_list)
        except Exception:
            i = i + 1
        finally:
            i = i + 1
            if i > 1:
                break
    try:
        sentence_list = wiki.summary(message)
        sentence = nltk.sent_tokenize(sentence_list)
        if sentence is not None:
            token_list2 = sentence
    except wiki.PageError:
        print("Error occurred")
    finally:

        return token_list1 + token_list2


# print("Tutor Bot: How can I help you ?")

close_chat = ['bye', 'quit', 'see you', 'exit']


def getMessage(message):
    if message.lower() in close_chat:
        # print("Tutor bot: See you later, bye !!")
        return "Tutor bot: See you later, bye !!"

    else:
        if greeting_response(message) is not None:
            # print("Tutor Bot: ", greeting_response(message))
            return greeting_response(message)
        elif any(map(str.isdigit, message)):
            # print(eval(message))
            return eval(message)
        else:
            sentence = getText(message)
            reply = bot_reply(message=message, sentence_list=sentence)
            return reply

# while True:
#   message = input()
#  if getMessage(message) == "Tutor bot: See you later, bye !!":
#     break
