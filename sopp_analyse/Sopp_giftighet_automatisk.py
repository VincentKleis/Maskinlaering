from pickle import load
from pandas import read_csv, DataFrame, get_dummies, from_dummies
from time import sleep
from sklearn.model_selection import train_test_split
from sys import exit
from platform import system

# detects what system you are running and choses the appropriate console command for clearing console based on the result
sys = system()
if sys == "Linux" or sys == "Darwin":
    clear = 'clear'
else:
    clear = 'cls'

# load a pretrained model from the "mushrooms" directory
clf = load(open("mushrooms/model.sav", "rb"))

while True:
    i = input("Would you like to type a path? type p, do a default test? t, or quit? q\n:")

    data = None

    match i.lower().strip():
        case "p":
            try:
                data = read_csv(input("path to csv file\n:"))
            except:
                print("invalid path")
            sleep(7)

        case "t":
            data = read_csv("agaricus-lepiota.csv")

        case "q":
            exit()

    if type(data) == DataFrame:
        # prepare the data so that it looks the same as the training data
        data.rename(columns = {
            'p':'Edible',
            'x':'Cap Shape',
            's':'Cap Surface',
            'n':'Cap Color',
            't':'Bruices',
            'p.1':'Odor',
            'f':'Gill Attatchment',
            'c':'Gill Spacing',
            'n.1':'Gill Size',
            'k':'Gill Color',
            'e':'Stalk Shape',
            'e.1':'Stalk Root',
            's.1':'Stalk Surface Above Ring',
            's.2':'Stalk Surface Below Ring',
            'w':'Stalk Color Above Ring',
            'w.1':'Stalk Color Below Ring',
            'p.2':'Veil Type',
            'w.2':'Veil Color',
            'o':'Ring Number',
            'p.3':'Ring Type',
            'k.1':'Spore Print Color',
            's.3':'Population',
            'u':'Habitat',
        }, inplace = True)

        data = data.drop(['Edible'],axis=1)

        data = get_dummies(data)

        prediction = clf.predict(data)

        data = from_dummies(data, sep='_')

        data.insert(0, "Edible", prediction)

        data.to_csv("result.csv")
        

        i = None
        #keeps the terminal active so that windows doesn't close it when used as executable
        while i == None:
            i = input("press enter to go back to prompt")
