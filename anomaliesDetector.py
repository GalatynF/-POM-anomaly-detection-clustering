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

# Class cluster : 
    # Skeleton (ex: TCP Job name)
    # DeleteElement (ex: tab[indices des mots])

## LEARNING ##

# Clusteriser : Use Distance function
# INPUT : Many Skeletons
# OUPUT : Clusters of Skeletons 



if __name__ == "__main__":
    # Main
    phrase = "[173.23.43.183] TCP (JOb Name MesCouilles) at /home/yolo/argh and many more"
    print(extract_skeleton(phrase))

    #GetCLuster
    #GetSentence
    #If (distance(newSentence, Cluster.skeleton) < seuil) :
