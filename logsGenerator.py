import sys
import random
import os
import math 
import json

class logs:
    '''Logs contient la phrase et sa fréquence d'apparition'''

    def __init__(self, skeleton, variance):
        self.skeleton = skeleton
        self.variance = variance
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


def choose_skeleton(data):
    while True : 
        rand = str(random.randrange(1, len(data)+1))
        freq = data['sk_'+rand]['freq']
        rand_test = random.randrange(0, 100)
        if rand_test < freq: 
            break
    skeleton = data['sk_'+rand]['sk']
    vari = data['sk_'+rand]['variance']
    log = logs(skeleton, vari)
    return log.sentence


def filling(path, f_size):

    if os.path.exists(path):
        f = open(path, 'w')

        json_file = open("./skeletons.json", 'r')
        data = json.load(json_file)

        s = 0
        while s < f_size : 
            msg = choose_skeleton(data)+'\n'
            f.write(msg)
            s += len(msg)

        f.close()
    else : 
        print("Error file %d doesn't exist", path)






if __name__ == "__main__":
    
    global_size = int(sys.argv[1])     # sys.argv[1] = quantité de log généré en octets

    if len(sys.argv) == 2 :
        nb_file = 1
    else : 
        nb_file = int(sys.argv[2])           # sys.argv[2] = nombre de fichiers différents

    ## Example usage ##

    #skeleton = "____ Skeleton exemple ____" # ____ will be replace by one element in the variance
    # variance = [
    #     ["Fisrt", "Second", "Third"],
    #     ["is good.", "is bad."]
    # ]

    # firstLog = logs(skeleton, variance)
    # print(firstLog.sentence)


    ###################

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
