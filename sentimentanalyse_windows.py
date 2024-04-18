import pickle
from sentimentanalyse.sentimentanalyse_funcs import lemmatizer
from os import system, getcwd
import nb_core_news_md

nlp = nb_core_news_md.load()

current = getcwd()

pipe = pickle.load(open(f".\_internal\language_model.sav", 'rb'))
sent = ''
result = None

# the loop
while True:
    system('cls')
    if result != None:
        print(f"the sentence is {result[0]}")

    sent = [input("Type 'stop' to stop \nType a sentence in norwegian:")]
    
    if sent[0].lower() == 'stop':
        break

    sent = lemmatizer(sent, nlp, True)
    result = pipe.predict(sent)