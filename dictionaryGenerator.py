#this is to make a dictionary full of wards
from random import randint
import pickle
import re
dictionary = []
try:
    dictionary = pickle.load(open("SAVE_DATA/Data/MyDictionary.txt","rb"))
    print(dictionary)

except FileNotFoundError:
    pickle.dump(dictionary,open("SAVE_DATA/Data/MyDictionary.txt","wb"))
    print(dictionary)

string = input("type string")
s = re.findall(r'\w+', string)

for i in range(0,len(s)):
    dictionary.append(s[i])
dictionary = list(dict.fromkeys(dictionary)) #removes repeated words

pickle.dump(dictionary,open("SAVE_DATA/Data/MyDictionary.txt","wb"))

#website used 
#https://www.keyhero.com/quotes/
