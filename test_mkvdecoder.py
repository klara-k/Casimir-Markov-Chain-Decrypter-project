import mkvdecoder
import numpy as np


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

#zhenya
def test_text_to_matrix():
    assert text_to_matrix('A AA h r a f',False)[0,0] == 1
    assert text_to_matrix('A aa h r a f',False)[0,0] == 1
    assert text_to_matrix('A AAA h r a f',False)[0,0] == 2
    assert text_to_matrix('A BAA h r a f',False)[0,0] == 1
    assert text_to_matrix('A BAA h r a f',False)[1,0] == 1
