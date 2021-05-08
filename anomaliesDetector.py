import re

## TOOL ##

#Removes empty items in list
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
# INPUT : 2 sentences skeletons (strings)
# OUTPUT : Distance
def calculate_distance(phrase1, phrase2):
    l1 = len(phrase1)
    l2 = len(phrase2)

    d = [[0 for x in range(l2)] for i in range(l1)]
    substitutionCost = 0;
    for i in range (l1):
        d[i][0] = i
    for j in range (l2):
        d[0][j] = j
    
    for i in range (1, l1):
        for j  in range(1, l2):
            if(phrase1[i] == phrase2[j]):
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1]+substitutionCost)
    return d[l1-1][l2-1]

# Class cluster : 
    # Skeleton (ex: TCP Job name)
    # DeleteElement (ex: tab[indices des mots])

## LEARNING ##

# Clusteriser : Use Distance function
# INPUT : Many Skeletons
# OUPUT : Clusters of Skeletons 



if __name__ == "__main__":
    # Main
    phrase1 = "[173.23.43.183] TCP (JOb Name Something) at /home/yolo/argh and many more"
    phrase2 = "[173.23.43.183] TCP (Job Name OtherThing) at /home/yolo/oof and many others more"
    liste1 = (remove_empty(extract_skeleton(phrase1).split(" ")))
    liste2 = (remove_empty(extract_skeleton(phrase2).split(" ")))
    print(calculate_distance(liste1, liste2))

    #GetCLuster
    #GetSentence
    #If (distance(newSentence, Cluster.skeleton) < seuil) :
