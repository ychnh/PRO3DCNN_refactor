import sys 
sys.path.append('../')
import util

data = util.unpickle('./data_0.pkl')
test = data['test']
import random

FILE = []
for x in list(random.sample(test, 50)):
    FILE.append( '> '+ x['sID'])
    FILE.append('Source:     ' + x['SRC'] + '    Chain:   ' +x['REGION'])
    FILE.append( x['SEQ'])

util.file_list(FILE, 'structures_to_predict.txt')
