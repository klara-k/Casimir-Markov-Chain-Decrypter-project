import numpy as np
import string

def random_cipher():
    return np.random.permutation(26)

# zhenya
def text_to_matrix(text, is_normalised):
    """ text_to_matrix calculates the number of times 
        (or frequency, depending on whether it is normalised or not)
         each binary appeares in the text. Stores it in the matrix. The column 
         of the matrix (first index) corresponds to the first letter in the 
         binary.
         
         ============
         Variables: 
         text: string 
         is_normalised: boolean
           
         ============
         Output: np.array of size (26, 26)
    """
    M = np.zeros((26, 26))
    text_lower = text.lower()
    N = 0
    for i in range(len(text_lower)-1):
        if text_lower[i] != ' ' and text_lower[i+1] != ' ':
            N += 1
            M[ord(text_lower[i])-ord('a'),ord(text_lower[i+1])-ord('a')] += 1
    if is_normalised:
        return M/N
    else:
        return M

# klara
def decode_text(text, cipher):
    """Decodes given text with substitution cipher 
    
    Parameters
    ----------
    text : string
    cipher : np.array() of size 26, permutation  
    
    Returns
    -------
    decoded_text : string 
    """
    new_text = ''
    alphabet = string.ascii_lowercase
    Alphabet = string.ascii_uppercase
    for char in text:
        if ord('A') <= ord(char) <= ord('Z'):
                i = ord(char) - ord('A') 
                new_text += Alphabet[cipher[i]%26] # uppercase letters are substituted with decoded letter
        elif ord('a') <= ord(char) <= ord('z'):
                i = ord(char) - ord('a')
                new_text += alphabet[cipher[i]%26]  # lowercase letters are substituted with decoded letter
        else:
            new_text += char  # non-letter characters are added without modification
    return new_text

# stefano
def decode_matrix(encoded_matrix, cipher):
    '''
    takes a transfer matrix ( np.array(26, 26) ), and a cipher ( np.array(26) ),
    returns a transfer matrix, transformed using the cypher
    '''
    return encoded_matrix[cipher,:][:,cipher]

# yaroslav
def fitness(ref_matrix, guess_matrix):
    """Returns the fitness function given the reference matrix and the guess matrix"""
    return(np.exp(np.trace(np.transpose(guess_matrix) .dot (np.log(ref_matrix)) ) ) )

# gal
def metropolis_step(ref_matrix, enc_matrix, cipher):
    '''
    Function that generates a new cipher using the metropolis algorithm!
    
    ----
    Parameters
    ----
    ref_matrix : 2D array_like
    enc_matrix : 2D array_like
    cipher : 1D array_like
    
    Returns
    ----
    Returns the newely generated cipher.
    '''
    exchange=np.random.randint(26,size=2) 
    cipher_try=cipher.copy()
    #Exchanges two elements of the cipher to create a new cipher
    cipher_try[exchange[0]]=cipher[exchange[1]] 
    cipher_try[exchange[1]]=cipher[exchange[0]]
    #Calculates the fitness values for both ciphers
    fitness_value=fitness(ref_matrix, decode_matrix(enc_matrix,cipher))
    fitness_value_try=fitness(ref_matrix, decode_matrix(enc_matrix,cipher_try))
    #Checks if the new fitness value is bigger.
    if fitness_value_try>fitness_value:
        cipher=cipher_try
    else:
    #Creates a weighted coinlip for conditional acceptance if the new fitness value is lower.
        coinflip=np.random.random(1)
        weight_for_transition=1/((fitness_value/fitness_value_try)+1)
        if coinflip<weight_for_transition:
            cipher=cipher_try
    return cipher
            
