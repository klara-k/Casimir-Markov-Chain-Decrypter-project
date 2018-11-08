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
	pass
