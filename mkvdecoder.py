import numpy as np
import string

#zhenya
def convergence(fitnesses, error):
    """ a condition for the end of the algorithm
        
        Parameters
	----------
	fitnesses: np array that contain last N fitnesses
        error: number-like

        Returns
	----------
	boolean: is the algorithm done?
      """
    fitnesses_diff = np.abs(np.diff(fitnesses))
    if np.mean(fitnesses_diff)<=error:
        return True
    else:
        return False

def random_cipher():
    """ -1 for Stefano from MASTER"""
    return np.random.permutation(26)

# zhenya
import string
def text_to_matrix(text, is_normalised):
    """ text_to_matrix calculates the number of times 
        (or frequency, depending on whether it is normalised or not)
         each binary appeares in the text. Stores it in the matrix. The column 
         of the matrix (first index) corresponds to the first letter in the 
         binary.
         
         Parameters
         ----------
	 text: string 
         is_normalised: boolean
         
   	 Returns
	 ----------
         np.array of size (26, 26)
    """
    M = np.zeros((26, 26))
    text_lower = text.lower()
    text_no_punctuation = ''.join(ch for ch in text_lower if (
        ord('a')<=ord(ch)<=ord('z') or ch==' '
    ) )
    N = 0
    for i in range(len(text_no_punctuation)-1):
        if text_no_punctuation[i] != ' ' and text_no_punctuation[i+1] != ' ':
            N += 1
            M[ord(text_no_punctuation[i])-ord('a'),ord(text_no_punctuation[i+1])-ord('a')] += 1
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
    ----------
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
def ref_matrix_regularize(ref_matrix):
    """Regularizes the reference matrix to allow for an efficient fitness computation
    -----------------------------------------------
    
    Returns a copy of a ref_matrix, with its zero elements replaced by the value of a smallest nonzero element"""
    
    #creates a matrix which has 1 on all positions where ref_matrix has exactly 0, and has 0 on all the other positions: 
    
    indicator=1-np.sign(ref_matrix)
    
    #finds smallest nonzero element in the matrix (option 0 is removed by adding indicator before passing to amin), adds this value to every zero in the matrix, returns the result:
    
    return(np.amin(indicator+ref_matrix)*indicator+ref_matrix)
    
    
    
def fitness(ref_matrix, guess_matrix):
    """Returns the value of the fitness function.
    
    The input is the reference matrix and the guess matrix. The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    #Convertion from the product to an exponential of a sum is being used; transpose is needed to compute M_ij log(N_ij) and not M_ij log(N_ji)
    
    return(np.exp(np.trace(np.transpose(guess_matrix) .dot (np.log(ref_matrix) ) ) ))

# gal
def metropolis_step(ref_matrix, enc_matrix, cipher):
    '''
    Function that generates a new cipher using the metropolis algorithm!
    
    Parameters
    ----------
    ref_matrix : 2D array_like
    enc_matrix : 2D array_like
    cipher : 1D array_like
    
    Returns
    ----------
    Returns the newely generated cipher.
    '''
    exchange=np.random.randint(26,size=2) 
    cipher_try=cipher.copy()
    #Exchanges two elements of the cipher to create a new cipher
    cipher_try[exchange[0]]=cipher[exchange[1]] 
    cipher_try[exchange[1]]=cipher[exchange[0]]
    # old code:
	'''
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
	'''
    # Calculates the fitness ratio between the two ciphers (old/new)
    fitness_ratio = mkvdecoder.fitness_ratio(ref_matrix, decode_matrix(enc_matrix,cipher), decode_matrix(enc_matrix,cipher_try))	
    # checks if the new cipher has higher fitness than the old, in which case the new cipher is returned
    if fitness_ratio < 1
    	return cipher
    # Creates a coinflip weighted by the fitness ratio, to decide whether the old cipher is kept or the new one is returned
    coinflip=np.random.random(1)
    weight_for_transition=1/(fitness_ratio+1)
    if coinflip<weight_for_transition:
        return cipher_try
    else
	return cipher
