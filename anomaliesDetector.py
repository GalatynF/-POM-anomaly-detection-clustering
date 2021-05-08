import re
import math

######### GLOBAL ##########

mu = -1

##################### TOOL ################

def print_matrix(matrics):
    for i in range(len(matrics)):
        print(matrics[i])

#Removes empty items in list
# INPUT : List
# OUTPUT : List
def remove_empty(entryList):
    liste = entryList
    changed = True
    while(changed):
        changed = False
        length = len(liste)
        for i in range (length):
            if liste[i] == '':
                del liste[i]
                changed = True
                break
    return liste


# Skeleton extractor : 
# INPUT : String : 1 sentence 
# OUTPUT : String : Skeleton of this sentence
def extract_skeleton(phrase):
    # Remove digits and points, or suites of slashes followed by characters that are not spaces
    pattern = r'([\d.])|((/[^ ]+)+)'
    return(re.sub(pattern, "", phrase))

# DistanceCalculator (levenshtein distance): 
# INPUT : String, String : 2 sentences skeletons
# OUTPUT : Int : Distance
def calculate_distance(phrase1, phrase2):
    l1 = len(phrase1)
    l2 = len(phrase2)

    if(l1==0 or l2 == 0):
        return max(l1, l2)

    l1 += 1
    l2 += 1
    d = [[0 for x in range(l2)] for i in range(l1)]
    substitutionCost = 0;
    for i in range (l1):
        d[i][0] = i
    for j in range (l2):
        d[0][j] = j
    
    for i in range (1, l1):
        for j  in range(1, l2):
            if(phrase1[i-1] == phrase2[j-1]):
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1]+substitutionCost)
    print_matrix(d)
    indexes = get_indexes(d)
    return [d[l1-1][l2-1], indexes]

# Class cluster : 
    # Skeleton (ex: TCP Job name)
    # DeleteElement (ex: tab[indices des mots])

## LEARNING ##

# Clusteriser : Use Distance function
# INPUT : Many Skeletons
# OUPUT : Clusters of Skeletons 



if __name__ == "__main__":
    # Main
    phrase1 = "I ate a cat today"
    phrase2 = "I ate a cat yesterday"
    '''
    phrase1 = "[173.23.43.183] TCP (Job Name Something) at /home/yolo/argh and many more"
    phrase2 = "[173.23.43.183] TCP (Job Name OtherThing) at /home/yolo/oof and more many"
    '''
    print(calculate_WED(phrase1, phrase2))


    '''
    liste1 = (remove_empty(extract_skeleton(phrase1).split(" ")))
    liste2 = (remove_empty(extract_skeleton(phrase2).split(" ")))
    print(liste1, liste2)
    print(calculate_distance(liste1, liste2))
    '''

    #GetCLuster
    #GetSentence
    #If (distance(newSentence, Cluster.skeleton) < seuil) :
