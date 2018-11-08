import numpy as np


# zhenya
def text_to_matrix(text, is_normalised):
	pass

# klara
def decode_text(text, cipher):
def decode_text(text, cipher):
    '''Decodes given text with substitution cipher 
        arguments:
            text: string
            cipher: 1-dim numpy array (decoding from index of array to ord(letter in alphabet))
        returns decoded text as string
        '''
    new_text = ''
    alphabet = string.ascii_lowercase
    for char in text:
        if ord('A') <= ord(char) <= ord('Z'):
                i = ord(char) - ord('A') 
                new_text += alphabet[cipher[i]%26] # uppercase letters are substituted with decoded letter
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
	pass
