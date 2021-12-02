# -*- coding: utf-8 -*-
import sys,os
import math
import re
import codecs
import math
from datetime import datetime
from collections import defaultdict
from collections import Counter 
from tqdm import tqdm


def test():
    corpus = []
    for ln in tqdm(open('1.txt', 'r')):
        ln = ln.strip()
        corpus.append(ln)


    for idx, row in enumerate(corpus):
        m = re.search(r'第(\d|一|二|三|四)(个|大|个大)功能', row)
        if m:
            print(row)


if __name__ == "__main__":
    test()
