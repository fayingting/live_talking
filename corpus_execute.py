# -*- coding: utf-8 -*-
"""语料处理脚本"""
import sys,os
import math
import re
import codecs
import math
import json
from datetime import datetime
from collections import defaultdict
from collections import Counter 
from tqdm import tqdm
import numpy as np
import distance
from sklearn.feature_extraction.text import CountVectorizer

def get_corpus(num):
    wf = open('华熙生物/%s.txt' % num, 'w')
    a = set()
    with open('华熙生物/%s.json' % num, 'r') as f:
        data = json.load(f)
        for row in data:
            ed = row['ed']
            if ed in a:
                continue
            r = row['onebest']
            r = r.lower()
            a.add(ed)
            if len(r) == 1:
                continue
            wf.write('%s\n' % r)
    print('finished')


def union_sentence(f):
    """将句子合并成段落"""

    corpus = []
    for ln in codecs.open('华熙生物/%s.txt' % f, 'r', encoding='utf8'):
        for item in list(ln.strip()):
            corpus.append(item)
    
    end_flag = -1
    para = []
    new_f = '华熙生物/%s_filter.txt' % f 
    wf = codecs.open(new_f, 'w', encoding='utf8')
    for idx, char in enumerate(corpus):
        if char not in ['。', '！', '？'] and (end_flag == -1 or idx > end_flag):
            para.append(char)

        if char in ['。', '！', '？']:
            end_flag = idx
            para.append(char)
            wf.write('%s\n' % ''.join(para))
            para = []
    print('[%s]finished' % f)

def run():
    need_word = [ln.strip() for ln in codecs.open('data/need_word', 'r', encoding='utf8')]
    for ln in tqdm(codecs.open('corpus', 'r',  encoding='utf8')):
        ln = ln.strip()
        for item in need_word:
            if ln.find(item) != -1:
                print(ln)
                break

    print('finished')


def edit_distance(s1, s2):
    """编辑距离"""
    return distance.levenshtein(s1, s2)

def jaccard_sim_get():
    corpus_dict = {}
    idx_corpus = {}
    for idx, ln in enumerate(codecs.open('corpus', 'r', encoding='utf8')):
        ln = ln.strip()
        r = Counter() 
        idx_corpus[idx] = ln
        for char in list(ln):
            if not re.search(r'[\u4e00-\u9fa5]', char):
                continue
            r[char] += 1
        corpus_dict[idx] = r
    
    res = defaultdict(dict)
    for _idx in corpus_dict:
        _dict1 = corpus_dict[_idx]
        char_set1 = set(_dict1.keys())
        for _idx2 in corpus_dict:
            if _idx2 == _idx:
                continue
            _dict2 = corpus_dict[_idx2]
            char_set2 = set(_dict2.keys())
            j = len(char_set1 & char_set2)
            b = len(char_set1 | char_set2)
            if b == 0:
                value = 0
            else:
                value = float(j) / b
            res[_idx][_idx2] = value


    for idx in res:
        _dict = res[idx]
        _l = sorted(_dict.items(), key=lambda x:x[1], reverse=True)
        idx2 = _l[0][0]
        sim = _l[0][1]
        _str = idx_corpus[idx]
        _str2 = idx_corpus[idx2]
        print('[%s]最相似的段落为:\t[%s]\t,相似度为:[%s]' % (_str, _str2, sim))

        




if __name__ == "__main__":
    for i in range(1, 10):
        union_sentence(i)
    #get_corpus(sys.argv[1])
    #jaccard_sim_get()
    #run()
