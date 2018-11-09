import mkvdecoder
import numpy as np

'''
# stefano
def test_decode_matrix():
    em = np.array([['aa','ab','ac'],
                   ['ba','bb','bc'],
                   ['ca','cb','cc']])
    dm = np.array([['cc','cb','ca'],
                   ['bc','bb','ba'],
                   ['ac','ab','aa']])

    assert((mkvdecoder.decode_matrix(em, [0, 1, 2]) == em).all())
    assert((mkvdecoder.decode_matrix(em, [2, 1, 0]) == dm).all())    
'''

#yaroslav

def test_fitness():
    
    refm = mkvdecoder.ref_matrix_regularize(
            np.array([[0,0.2,0],
                     [0,0,0.1],
                     [0.7,0,0]]) )
#     refmreg=np.array([[0.1,0.2,0.1],
#                      [0.1,0.1,0.1],
#                      [0.7,0.1,0.1]])
    eps=0.0000000000000000001
    refmreg=np.array([[eps,0.2,eps],
                     [eps,eps,0.1],
                     [0.7,eps,eps]])    
    guessm1 = np.array([[0,0,0],
                     [0,0,1],
                     [1,0,0]])
    guessm2 = np.array([[0,1,0],
                     [0,0,1],
                     [0,0,0]])
    guessm3 = np.array([[2,0,0],
                     [0,0,1],
                     [1,0,0]])
    
    #checking if regularization procedure went as expected
    
    assert((refm==refmreg).all())
    
    #checking the fitness computation 
    #computation procedure gives some numerical errors, so we allow them -- if they're bound by 10^-8 %

    assert(np.abs(mkvdecoder.fitness(refm,guessm1)-0.07)/0.07<0.0000000001)
    assert(np.abs(mkvdecoder.fitness(refm,guessm2)-0.02)/0.02<0.0000000001)
    
    #checking the fitness ratio computation

    assert(np.abs(mkvdecoder.fitness(refm,guessm1)/mkvdecoder.fitness(refm,guessm2)-3.5)/3.5<0.0000000001)


#zhenya
def test_text_to_matrix():
    assert mkvdecoder.text_to_matrix('A AA\n h r a f',False)[0,0] == 1
    assert mkvdecoder.text_to_matrix('A aa h r a f',False)[0,0] == 1
    assert mkvdecoder.text_to_matrix('A AAA h r a f',False)[0,0] == 2
    assert mkvdecoder.text_to_matrix('A BAA\n h.: r? a f',False)[0,0] == 1
    assert mkvdecoder.text_to_matrix('A BAA h r a f',False)[1,0] == 1

