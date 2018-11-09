import numpy as np
import string

#Zhenya
def convergence(fitnesses, error):
    """ a simple condition which tests when it is reasonable
        to  end of the algorithm. This ondition just takes latest several 
        fitnesses and calculates the differences between them. If the
        average difference is smaller than the error, we suppose
        that the algorythm convereged.
        
        Parameters
	    ----------
	    fitnesses: np array that contain last N fitnesses
        error: number-like

        Returns
	    ----------
	    boolean: is the algorithm done?
    """
    fitnesses_diff = np.abs(np.diff(fitnesses)) #array of absolute differences between fitnesses
    if np.mean(fitnesses_diff)<=error:  #condition of convergence
        return True
    else:
        return False

#Stefano
def random_cipher():
    """ returns a random permutation of array with numbers 0-25"""
    return np.random.permutation(26)

#Zhenya
def text_to_matrix(text, normalize_and_regularize):
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
        np.array of size (27, 27)
    """
    #initialise matrix with zeros
    M = np.zeros((27, 27)) 
    
    #text_good is a converted string that has all the letters in the lower case and no punctuation signs
    text_good = ''.join(ch for ch in text.lower() if (ord('a')<=ord(ch)<=ord('z') or ch==' ')) 
    
    #this variable counts how many binaries there are in the text
    number_of_binaries = 0 
        
    #we go along the text and count binaries
    for i in range(len(text_good)-1): 
        #this checks if we have a binary or just the ending/beginning of a word
        if text_good[i] != ' ' and text_good[i+1] != ' ': 
            number_of_binaries += 1 
            #add 1 in the corresponding element of the matrix when we find the binary
            M[ord(text_good[i])-ord('a'),ord(text_good[i+1])-ord('a')] += 1 
        # checks if this is the beginning of a word eg. ' c'    
        elif text_good[i] == ' ' and text_good[i+1] != ' ': 
            number_of_binaries += 1 
            M[26,ord(text_good[i+1])-ord('a')] += 1 
        # checks if this is the end of a word eg. 'c '      
        elif text_good[i] != ' ' and text_good[i+1] == ' ': 
            number_of_binaries += 1 
            M[ord(text_good[i])-ord('a'),26] += 1 
   
    #here we normalise and regularize matrix if needed
    if normalize_and_regularize: 
        return ref_matrix_regularize((M/np.amax(M))/number_of_binaries)
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
    takes a transfer matrix ( np.array(27, 27) ), and a cipher ( np.array(26) ),
    returns a transfer matrix, transformed using the cypher
    '''
    cipher_with_space=np.append(cipher,[26])
    return encoded_matrix[cipher_with_space,:][:,cipher_with_space]

# yaroslav
def ref_matrix_regularize(ref_matrix):
    """Regularizes the reference matrix to allow for an efficient fitness computation
    -----------------------------------------------
    
    Returns a copy of a ref_matrix, with its zero elements replaced by the value of a smallest nonzero element"""
    
    #creates a matrix which has 1 on all positions where ref_matrix has exactly 0, and has 0 on all the other positions: 
    
    indicator=1-np.sign(ref_matrix)
    eps=0.0000000000000000001
    #finds smallest nonzero element in the matrix (option 0 is removed by adding indicator before passing to amin), adds this value to every zero in the matrix, returns the result:
    
#     return(np.amin(indicator+ref_matrix)*indicator+ref_matrix)
    return(eps*indicator+ref_matrix)

def fitness(ref_matrix, guess_matrix):
    """Returns the value of the fitness function.
    
    The input is the reference matrix and the guess matrix. 
    The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    logf=0.
    
    for i in range (len(ref_matrix)):
        for j in range (len(ref_matrix)):
            logf=logf+(np.log(ref_matrix[i,j])*int(guess_matrix[i,j]))
    
    # Convertion from the product to an exponential of a sum is being used
    # transpose is needed to compute M_ij log(N_ij) and not M_ij log(N_ji)
    
#     return(np.exp(np.trace(np.transpose(guess_matrix) .dot (np.log(ref_matrix) ) ) ))
    return(np.exp(logf))

def sumfitness(ref_matrix, guess_matrix):
    """Returns the value of the fitness function.
    
    The input is the reference matrix and the guess matrix. 
    The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    f=0
    
    for i in range (len(ref_matrix)):
        for j in range (len(ref_matrix)):
            f=f+ref_matrix[i,j]*int(guess_matrix[i,j])
    
    # Convertion from the product to an exponential of a sum is being used
    # transpose is needed to compute M_ij log(N_ij) and not M_ij log(N_ji)
    
#     return(np.exp(np.trace(np.transpose(guess_matrix) .dot (np.log(ref_matrix) ) ) ))
    return(np.exp(logf))

def logfitness(ref_matrix, guess_matrix):
    """Returns the value of the fitness function.
    
    The input is the reference matrix and the guess matrix. The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    logf=0.
    
    for i in range (len(ref_matrix)):
        for j in range (len(ref_matrix)):
            logf=logf+(np.log(ref_matrix[i,j])*int(guess_matrix[i,j]))
    
    # Convertion from the product to an exponential of a sum is being used
    # transpose is needed to compute M_ij log(N_ij) and not M_ij log(N_ji)
    
#     return(np.exp(np.trace(np.transpose(guess_matrix) .dot (np.log(ref_matrix) ) ) ))
    return(logf)

def fitness_ratio(ref_matrix, guess_matrix_old, guess_matrix_new):
    """Returns the ratio of the old and the new fitness functions (old over new).
    
    The input is the reference matrix and the guess matrices -- old and new. The function returns the ratio of corresponding fitness functions. The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    #exponential in the fitness function is linear in guess_matrix, so it's enough to take the difference
    
    return(fitness(ref_matrix,guess_matrix_old-guess_matrix_new))

def sumfitness_ratio(ref_matrix, guess_matrix_old, guess_matrix_new):
    """Returns the ratio of the old and the new fitness functions (old over new).
    
    The input is the reference matrix and the guess matrices -- old and new. The function returns the ratio of corresponding fitness functions. The reference matrix is assumed to be regularized (to contain no zero elements)"""
    
    #exponential in the fitness function is linear in guess_matrix, so it's enough to take the difference
    
    return(sumfitness(ref_matrix,guess_matrix_old)/sumfitness(ref_matrix,guess_matrix_new))

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
    fitness_ratio_val = fitness_ratio(ref_matrix, 
                                      decode_matrix(enc_matrix,cipher),
                                      decode_matrix(enc_matrix,cipher_try))
    # checks if the new cipher has higher fitness than the old, in which case the new cipher is returned
    if fitness_ratio_val < 1:
        return cipher_try
    # Creates a coinflip weighted by the fitness ratio, to decide whether the old cipher is kept or the new one is returned
    coinflip=np.random.random(1)
    weight_for_transition=1/(fitness_ratio_val+1)
    if coinflip<weight_for_transition:
        return cipher_try
    else:
        return cipher
