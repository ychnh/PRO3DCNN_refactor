import util
X = util.unpickle('data/scope_data.pkl')

try:
    for d in X:
        nID, sID, CA, SEQ, CLS = d['nID'], d['sID'], d['CA'], d['SEQ'], d['CLS']
        assert( len(CA)==len(SEQ) )
except:
    print(nID,sID, len(CA), len(SEQ)  )
    print(d)
