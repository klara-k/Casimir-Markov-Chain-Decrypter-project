import numpy as np


# zhenya
def text_to_matrix(text, is_normalised):
	pass

# klara
def decode_text(text, cipher):
	pass

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
    Input
    ----
    ref_matrix : 2D array_like
    enc_matrix : 2D array_like
    cipher : 1D array_like
    ----
    Return
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
        weight_for_remaining=1/((fitness_value/fitness_value_try)+1)
        if coinflip<weight_for_remaining:
            cipher=cipher_try
    return cipher
            
