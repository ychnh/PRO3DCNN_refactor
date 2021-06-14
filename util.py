from collections import defaultdict
import numpy as np
import pickle as pick

def unpickle(filename):
    with open(filename, 'rb') as fo:
        data = pick.load(fo, encoding='bytes')
    return data

def pickle(data,filename):
    f = open(filename,"wb")
    pick.dump(data,f,protocol=2)
    f.close()

def file_list(writeList,filename):
    with open(filename, 'w') as f:
        for item in writeList:
            f.write("%s\n" % item)

def list_file(filename):
    returnList = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip('\n')
            returnList.append(line)
    return returnList


def distm(chain):
    ''' chain: a coordinate object of BxLx3
    '''
    L = chain.shape[-2]
    a = np.stack(L*[chain])

    b = np.stack(L*[chain], axis=1)

    x = ( (a-b)**2 ).sum(-1)
    x = np.sqrt(x)
    return x

DICT = { 'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D', 'CYS':'C', 'GLN':'Q', 'GLU':'E', 'GLY':'G', 'HIS':'H',
         'ILE':'I', 'LEU':'L', 'LYS':'K', 'MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S', 'THR':'T', 'TRP':'W',
         'TYR':'Y', 'VAL':'V',  'ASX':'N', 'GLX':'Q', 'UNK':'G', 'HSD':'H' }

def parse_scope(scopfile):
    scope_db = {}
    fr=open(pdbfile)
    lines=fr.readlines()
    for line in lines:
        if line.startswith('>'):
            name,cls= line[1:].split(' ')[:2]
            scope[name] = cls.split('.')

'REMARK  99 ASTRAL SCOPe-sccs:'# a.1.1.1
'REMARK  99 ASTRAL Source-PDB:'# 1dlw

def parse_pdb(pdbfile):
    dict_pdb=defaultdict(list)
    fr=open(pdbfile)
    lines=fr.readlines()
    for line in lines:
        if line.startswith('REMARK  99 ASTRAL SCOPe-sccs:'):# a.1.1.1
            cls = line.split()[4]
            cls = cls.split('.')
            cls = [ cls[0], int(cls[1]), int(cls[2]), int(cls[3]) ]
        if line.startswith('REMARK  99 ASTRAL Source-PDB:'):# 1dlw
            src = line.split()[4]
        if line.startswith('REMARK  99 ASTRAL Region:' ):
            region = line[24:]
        if line.startswith('ATOM'):
            chain=line[21]
            dict_pdb[chain].append(line)
    #chains=list(dict_pdb.keys())
    #key=chains[chain_number-1]
    #return (dict_pdb[key])

    return dict_pdb,cls,src,region

def get_xyz(pdb):
    SLINES = []
    target=['N','CA','CB','C']
    dict_xyz_all=defaultdict(dict)
    for line in pdb:
        sline = line.split()
        SLINES.append( [line[30:38], line[38:46], line[46:54]] )
        #residue = line[17:20].strip()
        residue = sline[3]
        ####remove nonstandard amino acid
        if DICT.get(residue):

            #atomname = line[12:16].strip()
            atomname = sline[2]
            if atomname in target:
                res_no=line[22:26].strip()
                #res_no=sline[1]
                coords_str=[line[30:38], line[38:46], line[46:54]]
                #coords_str=[ sline[6],sline[7],sline[8] ] 
                coords=[float(k) for k in coords_str]
                dict_xyz_all[res_no][atomname]=coords
                dict_xyz_all[res_no]['SEQ'] = DICT.get(residue)
    #essential=['N','CA','C', 'SEQ']
    essential=['CA', 'SEQ']
    dict_xyz={}
    for key in dict_xyz_all:
        item=dict_xyz_all[key]
        atom_set=item.keys()
        if set(essential).issubset(set(atom_set)):
            dict_xyz[int(key)]=item


    return (dict_xyz), dict_xyz_all

