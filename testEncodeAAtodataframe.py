"""
Creator: David Sjöberg
Date: July 2022
Function: takes aminacidprofile string and encodes it to integers and stores in
pd.DataFrame as a column called sequence

"""

import pandas as pd



#Just a test sequence lol
test = 'HRCSMLEHWHFAEMIDTDSMHQWTRHPKTPSWTKVFMLTRIIHQLNGQVCWPQIHRMCWR'


 
#Inputs a protein aminoacidprofile, output encoded panda dataframe with sequence
#as column
def encode_AA(aminoacid):
    #Encoding keys and values
    AMINO_ACID_TO_ID = {'-': 0,'X': 0,'B': 0,'Z': 0,'A': 1,'C': 2,'D': 3,'E': 4,'F': 5,
                   'G': 6,'H': 7,'I': 8,'K': 9,'L': 10,'M': 11,'N': 12,'P': 13,
                   'Q': 14,'R': 15,'S': 16, 'T': 17,'V': 18,'W': 19,'Y': 20}
    
    #Splits input string into each letter as a string
    seqsplit = list(aminoacid)
    encoded_AA = []
    
    #Iterates over each letter, matches it to a key and then adds the 
    #value of that key to encoded_AA
    for i in seqsplit:
        i = seqsplit.index(i)
        for key, value in AMINO_ACID_TO_ID.items():
        
            if key in seqsplit[i]:
                encoded_AA.append(value)


            
    #Creates a dict with encoded aminoacids
    DICT = { 'sequence': encoded_AA}            


    #Creates a pandas dataframe from the dictonary with sequence as column
    sq_df = pd.DataFrame(DICT)
    return sq_df