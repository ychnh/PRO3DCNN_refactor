# There maybe potential errors/corrupted data
import traceback
import numpy as np
import sys 
sys.path.append('../')
import util
import os
from tqdm import tqdm

a = 0
error = []
data = []
START = 3558
START = 0
#IGNORE = ['d2r4qa2', 'd4zjpa2', 'd3o3de2', 'd3o3db2','d2brxa2']
IGNORE = []

dirp = 0;D = os.listdir('./pdbstyle-2.07')
try:
    for root, dirs, files in os.walk('./pdbstyle-2.07', topdown=True):
        dirp += 1; print(dirp,'/', len(D))
        for f in files:
            if f[-4:] == '.ent':
                sID = f[:-4]
                nID = len(data)

                if sID in IGNORE:continue
                if a<START: a+=1;continue

                pdb,CLS,SRC = util.parse_pdb(root+'/'+f)
                if len(pdb)==0: IGNORE.append(sID);continue
                key = list(pdb.keys())[0]
                x,s = util.get_xyz(pdb[key]) # 1339 out of 276230 have more than 1 key. I am not sure why. Investigate later

                CA = [x[i]['CA'] for i in x]
                if len(CA)==0: IGNORE.append(sID); continue
                CA  = np.stack( CA )
                SEQ = ''.join( [x[i]['SEQ'] for i in x] ) 
                data.append( {'nID':nID, 'sID':sID, 'CA':CA, 'SEQ':SEQ, 'CLS':CLS, 'SEQ':SEQ} )
                a+=1
except:
    #print(pdb.keys())
    #print(s)
    #print([i for i in x])
    print(pdb)
    print('----------------------------------')
    print(a,CLS, SRC, sID, nID, root,f)
    #print(sys.exc_info())
    traceback.print_exc()


util.file_list(IGNORE, 'ignore_list')
util.pickle(data,'scope_data.pkl')
