import sys
import random
import os
import math 

class logs:
    '''Logs contient la phrase et sa fréquence d'apparition'''

    def __init__(self, skeleton, variance, freq = 0):
        self.skeleton = skeleton
        self.variance = variance
        self.freq = freq
        self.random()

    def random(self): 
        '''Rempli les trous du squelette avec les variances fournies'''
        list_of_word = self.skeleton.split()
        nb_hole = 0
        for i in range(len(list_of_word)):
            if list_of_word[i] == "____": 
                nb_hole += 1

        if nb_hole != len(self.variance): 
            print("Le nombre de trou du squelette ne correspond pas au nombre de variance possible")
            exit()

        filling_skeleton = self.skeleton
        for i in range(len(self.variance)):
            rand = random.randrange(0, len(self.variance[i]))
            filling_skeleton = filling_skeleton.replace("____", self.variance[i][rand], i+1)
        self.sentence = filling_skeleton


def filling(path, f_size):

    if os.path.exists(path):
        f = open(path, 'w')

        s = 0
        while s < f_size : 
            msg = "ok"+"\n" # TODO : generate rand log 
            f.write(msg)
            s += len(msg)

        f.close()
    else : 
        print("Error file %d doesn't exist", path)






if __name__ == "__main__":
    
    global_size = int(sys.argv[1])     # sys.argv[1] = quantité de log généré en Mo
    nb_file = int(sys.argv[2])           # sys.argv[2] = nombre de fichiers différents

    # firstLog = logs("____ Jambon ____", [["le", "la"],["est bon", "n'est pas bon"]], 12)
    # print(firstLog.skeleton)
    # print(firstLog.sentence)
    # print("///////////////")

    # tab = []
    
    # vari = [["[192.168.45.12]","[192.168.75.8]","[192.174.32.154]"],["update()","upgrade()","upload()","createaAccount()","login()","logout()"]]

    # for i in range(10): 
    #    tab.append(logs("____ TCP job name ____", vari, 10))
    #    print(tab[i].sentence)


    # Directory generation
    if not os.path.isdir("generated"):
        os.makedirs("generated")

    files_size = (global_size)/nb_file
    
    while nb_file > 0:
        path = './generated/logs_'+str(nb_file)
        
        if not os.path.exists(path):
            with open(path, 'w'): pass

        filling(path, files_size)

        nb_file -= 1
