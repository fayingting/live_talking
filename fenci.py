# -*- coding: utf-8 -*-
import sys,os
import math
import re
import codecs
import json
from datetime import datetime
from collections import defaultdict
from collections import Counter 
from tqdm import tqdm

currDir = os.path.normpath(os.path.dirname(__file__))
SEGMENT = os.path.normpath(os.path.join(currDir, '../segment/'))
sys.path.insert(0, SEGMENT)

from segment import Segment



def seg_run():
    segment = Segment(mode='lac')
    wf = open('fenci', 'w')
    for ln in tqdm(open('corpus', 'r')):
        title = ln.strip()
        r = segment.do_segment(title)
        if not r:
            continue
        wf.write('%s\n' % ' '.join(r))

    print('finished')

if __name__ == "__main__":
    seg_run()

