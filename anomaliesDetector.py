import re

# Skeleton extractor : 
# INPUT : 1 sentence 
# OUTPUT : Skeleton of this sentence
def extract_skeleton(phrase):
    # Remove digits and points, or suites of slashes followed by characters that are not spaces
    pattern = r'([\d.])|((/[^ ]+)+)'
    return(re.sub(pattern, "", phrase))

# DistanceCalculator : 
# INPUT : 2 sentences
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
