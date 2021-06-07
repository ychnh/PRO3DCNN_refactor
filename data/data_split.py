#split the dataset into train, test, val where no superfamily is shared
# I'm splitting the superfamilies

import sys 
sys.path.append('../')
import util

X = util.unpickle('./scope_data.pkl') #['nID', 'sID', 'CA', 'SEQ', 'CLS']

from collections import defaultdict
S = defaultdict(lambda: defaultdict(int) )

def FOLD(CLS): return CLS[0] + str(CLS[1])
def SFAM(CLS): return CLS[2]


for x in X:
    CLS = x['CLS']
    fold = FOLD(CLS)
    sfam = SFAM(CLS)
    if fold[0] in 'hijkl': continue
    S[fold][sfam] += 1

TOTAL = 0

sing_sfam = 0
sing_sfam_count = 0

countsfam = 0
for fold in S:
    SFAMS = S[fold]
    fstat = []

    if len(SFAMS)==1: sing_sfam+=1

    for sfam in SFAMS:
        countsfam += 1
        count = SFAMS[sfam]
        fstat.append( (sfam,count) )
        if len(SFAMS)==1: sing_sfam_count+=count
        
        #print(sfam, count)
        TOTAL += count

print( TOTAL, len(X), countsfam, len(S), sing_sfam, sing_sfam_count)

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
