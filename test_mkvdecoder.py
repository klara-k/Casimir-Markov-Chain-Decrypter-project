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