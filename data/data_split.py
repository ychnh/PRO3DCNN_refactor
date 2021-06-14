import random
import sys 
sys.path.append('../')
import util
from collections import defaultdict

def FOLD(CLS): return CLS[0] + str(CLS[1])
def FAM(CLS): return str(CLS[2]) + '.' + str(CLS[3])

def process(DATA):
    '''
    * DATA: array of scope data with #['nID', 'sID', 'CA', 'SEQ', 'CLS', 'SRC', 'REGION']
    * returns: processed data where (classes hijkl) and (folds with only 1 family) are removed. 
    '''

    cnt_family2fold = defaultdict(lambda: defaultdict(int) )

    for x in DATA:
        fold,fam = FOLD(x['CLS']),FAM(x['CLS'])
        
        cnt_family = cnt_family2fold[fold]
        cnt_family[fam] += 1


    # parse DATA
    parsed_DATA = []
    for x in DATA:
        fold,fam = FOLD(x['CLS']),FAM(x['CLS'])

        if fold not in cnt_family2fold: continue
        cnt_family = cnt_family2fold[fold]
        if len(cnt_family)==1: 
            cnt_family2fold.pop(fold)
            continue #only one family in fold

        parsed_DATA.append(x)
        

    return parsed_DATA, cnt_family2fold


from sklearn.model_selection import GroupShuffleSplit
def split_groups(group_cnt_pairs, random_state=32):
    '''
    * group_cnt_pairs: a list of (fam,cnt) for a fold
    * returns: the train, test splits of family names
    '''

    groups = []
    for g, (fam_name, cnt) in enumerate(group_cnt_pairs):
        groups += cnt*[g]
    L = len(groups)
    
    X,Y = L*[None], L*[None]
    gss = GroupShuffleSplit(n_splits=1, train_size=.85, random_state=random_state)
    for train_idx, test_idx in gss.split(X,Y,groups):
        train_group = set([groups[i] for i in train_idx])
        train = [ group_cnt_pairs[i][0] for i in train_group ]

        test_group = set([groups[i] for i in test_idx])
        test = [ group_cnt_pairs[i][0] for i in test_group ]

    return train, test


def split(DATA, cnt_family2fold, random_state=32):
    '''
    returns: array of train, and test families
    '''

    TRAIN = []
    TEST = []

    trainFams2fold = {}
    testFams2fold = {}

    for fold, cnt_family in cnt_family2fold.items():


        family_cnt_pairs = [ (family,cnt) for family,cnt in cnt_family.items()]
        train, test = split_groups(family_cnt_pairs, random_state=random_state)
        trainFams2fold[fold] = train
        testFams2fold[fold] = test

    train, test = [],[]
    for x in DATA:
         
        fold,fam = FOLD(x['CLS']),FAM(x['CLS'])

        if fam in trainFams2fold[fold]: 
            train.append(x)
        elif fam in testFams2fold[fold]:
            test.append(x)
        else:
            print('reallybad')
    return train,test


#print(len(train), len(test), len(test)/(len(test)+len(train)) )
def out_to_fasta(data, save_path):

    def fasta_name(x):
        fold,fam = FOLD(x['CLS']),FAM(x['CLS'])
        #return ' '.join( ['>'+ str(x['nID']), x['sID'], fold, fam] )
        return ' '.join( ['>'+ x['sID'], fold, fam] )

    write = []
    for x in data:
        write.append( fasta_name(x) )
        write.append( x['SEQ'] )

    util.file_list(write, save_path)


def seq_ident_intersection(A,B):
    '''
    * A: typically the larger of the 2 input params
    * B: subset of DATA
    '''
    out_to_fasta(A, './mmseqs/train.fasta')
    out_to_fasta(B, './mmseqs/test.fasta')

    import os
    os.system('cd mmseqs; ./mmseqs_job.sh; cd ..')

    FILE = util.list_file('mmseqs/resultDB.m8')
    cnt2sID = defaultdict(int)
    for l in FILE:
        sID = l.split()[0]
        cnt2sID[sID] += 1

    return list( cnt2sID.keys() )


# L = binned distance of epsilong
# start end a b
# LxN




''' Ordered print
def order(fold):
    C = 'abcdefghijkl'
    MAX = 10000
    c,f = fold[0], int( fold[1:] )
    c = C.find(c)
    return c*MAX + f
print( sorted( S.keys(), key=order) )
'''


# DATA -> cnt_family2fold
# Split DATA into train, test for each fold: split into train,test
# Save into train, test fasta. Remove seq ident 30%

''' workflow '''
DATA = util.unpickle('./scope_data.pkl') #['nID', 'sID', 'CA', 'SEQ', 'CLS']
DATA, cnt_family2fold = process(DATA)
for i in range(5):
    train, test = split(DATA, cnt_family2fold, random_state=random.randint(0,10000) )
    intersection = seq_ident_intersection(train, test)
    test = [t for t in test if t['sID'] not in intersection]
    util.pickle( {'train':train, 'test':test}, 'data_'+str(i)+'.pkl')

# pair-wise distance
# overall distance
'''
train_test = [ split(DATA, cnt_family2fold, random_state=random.randint(0,10000) ) for _ in range(5) ]
for train, test in train_test:
    print( len(train), len(test) )

def dataset_dist(A,B):
    A = set( [ a['nID'] for a in A] )
    B = set( [ b['nID'] for b in B] )
    C = A.intersection(B)
    return len(C)/( min(len(A), len(B)) )

L = len(train_test)

for i in range(L):
    for j in range(L):
        i_tr,_ = train_test[i]
        j_tr,_ = train_test[j]
        print( dataset_dist(i_tr, j_tr) )
'''




#print(intersection)

''' workflow '''
