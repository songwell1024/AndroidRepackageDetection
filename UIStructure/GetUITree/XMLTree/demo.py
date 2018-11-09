#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: demo.py
@time: 2018/11/9/009 10:53
@desc:
'''

from datasketch import MinHash, MinHashLSH

def getMinHash():
    set1 = 'minhashisaprobabilisticdatastructurefor'
    set2 = 'minhashisaprobabilitydatastructureforqwert',
    set3 = 'minhashisprobability'

    m1 = MinHash(num_perm=128)
    m2 = MinHash(num_perm=128)
    m3 = MinHash(num_perm=128)
    for d in set1:
        m1.update(d.encode('utf8'))
    for d in set2:
        m2.update(d.encode('utf8'))
    for d in set3:
        m3.update(d.encode('utf8'))

    # Create LSH index
    lsh = MinHashLSH(threshold=0.5, num_perm=128)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with Jaccard similarity > 0.5", result)


if __name__ == '__main__':
    getMinHash()