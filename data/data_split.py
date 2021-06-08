#split the dataset into train, test, val where no superfamily is shared
# I'm splitting the superfamilies

import sys 
sys.path.append('../')
import util

X = util.unpickle('./scope_data.pkl') #['nID', 'sID', 'CA', 'SEQ', 'CLS']

from collections import defaultdict


def FOLD(CLS): return CLS[0] + str(CLS[1])
def FAM(CLS): return str(CLS[2]) + '.' + str(CLS[3])


cnt_family2fold = defaultdict(lambda: defaultdict(int) )

for x in X:
    fold,fam = FOLD(x['CLS']),FAM(x['CLS'])

    if fold[0] in 'hijkl': continue
    
    cnt_family = cnt_family2fold[fold]
    cnt_family[fam] += 1


''' STATISTICS
total_cnt = 0
single_family_count = 0
single_family_fold = []
for fold, cnt_family in cnt_family2fold.items():

    for family,cnt in cnt_family.items():
        print(fold, family, cnt)
        if len(cnt_family)==1: single_family_count += cnt
        total_cnt += cnt

    if len(cnt_family)==1: single_family_fold.append( (fold,cnt) )


if len(cnt_family)==1: single_family_fold.append( (fold,cnt) )
#print( sorted( single_family_fold, key=lambda x: x[1]) )
#print( 'No. single family folds:', len(single_family_fold) )
#print( 'Number of proteins that have belong in single family folds:', single_family_count, '/', total_cnt )
'''


# TODO Time to split algorithm
for fold, cnt_family in cnt_family2fold.items():

    if len(cnt_family)==1: continue
    x = [ (family,cnt) for family,cnt in cnt_family.items()]
    print(fold,x)




''' Ordered print
def order(fold):
    C = 'abcdefghijkl'
    MAX = 10000
    c,f = fold[0], int( fold[1:] )
    c = C.find(c)
    return c*MAX + f
print( sorted( S.keys(), key=order) )
'''



#print(S)




# for each fold, build a list of superfamily and it's size


# Get the list of numbers we need for each fold
# partition in half, partition in half





#While we split the super families, we need to be mindful they belong to a fold
#We need to distribute folds evenly


# create 2 fastas util.file_list()
# run msseqs_job
