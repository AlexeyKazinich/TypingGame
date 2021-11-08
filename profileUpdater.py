#this will update all the saves to a new save to prevent currupted files

import pickle

def updater():
    usernames = pickle.load(open("SAVE_DATA/Game_Data/usernames.txt","rb"))
    temporary = []
    for i in range(0,len(usernames)):
        temporary = pickle.load(open("SAVE_DATA/Users/"+usernames[i]+".txt","rb"))
        temporary[3] = [0,0,0,0,0,0,0,0,0,0]
        temporary[4] = ["","","","","","","","","",""]
        temporary[6] = [0,0,0,0,0,0,0,0,0,0]
        pickle.dump(temporary,open("SAVE_DATA/Users/"+usernames[i]+".txt","wb"))
        print(temporary)

def updater2():
    this = ["","","","","","","","","",""]
    usernames = pickle.load(open("SAVE_DATA/Users/usernames.txt","rb"))
    temporary = []
    for i in range(0,len(usernames)):
        temporary = pickle.load(open("SAVE_DATA/Users/"+usernames[i]+".txt","rb"))
        print(temporary)
        temporary.insert(4,this)
        pickle.dump(temporary,open("SAVE_DATA/Users/"+usernames[i]+".txt","wb"))
        print(temporary)
def updateTester():
    empty = [0,0,0,[0,0,0,0,0,0,0,0,0,0],["","","","","","","","","",""],[0,5000,0]]
    pickle.dump(empty,open("SAVE_DATA/Users/tester.txt","wb"))

def remover():
    temporary = pickle.load(open("SAVE_DATA/Data/MyDictionary.txt","rb"))
    Loc = temporary.index("A")
    del temporary[Loc]
    Loc= temporary.index("s")
    del temporary[Loc]
    Loc= temporary.index("re")
    del temporary[Loc]
    Loc= temporary.index("didn")
    del temporary[Loc]
    Loc= temporary.index("t")
    del temporary[Loc]
    Loc= temporary.index("don")
    del temporary[Loc]
    Loc= temporary.index("aren")
    del temporary[Loc]
    Loc=temporary.index("ll")
    del temporary[Loc]
    Loc= temporary.index("d")
    del temporary[Loc]
    Loc = temporary.index("m")
    del temporary[Loc]
    Loc = temporary.index("ve")
    del temporary[Loc]
    Loc = temporary.index("couldn")
    del temporary[Loc]
    Loc = temporary.index("condom")
    del temporary[Loc]
    pickle.dump(temporary,open("SAVE_DATA/Data/MyDictionary.txt","wb"))
    print(temporary)
print("done")
