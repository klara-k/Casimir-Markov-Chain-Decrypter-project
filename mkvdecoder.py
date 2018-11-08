import numpy as np


# zhenya
def text_to_matrix(text, is_normalised):
    M = np.zeros((26,26))
    text_lower = text.lower()
    N = 0
    for i in range(len(text_lower)-1):
        if text_lower[i] != ' ' and text_lower[i+1] != ' ':
            N += 1
            M[ord(text_lower[i])-97,ord(text_lower[i+1])-97] += 1
    if is_normalised:
        return M/N
    else:
        return M

# klara
def decode_text(text, cipher):
	pass

# stefano
def decode_matrix(encoded_matrix, cipher):
	pass

# yaroslav
def fitness(ref_matrix, guess_matrix):
	pass

# gal
def metropolis_step(ref_matrix, enc_matrix, cipher):
	pass
