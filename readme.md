# SCOPe 2.07 data processing
* Download the extracted data of SCOPe coordinates from https://drive.google.com/file/d/12tnHkJHMRHN6GPI5LTZ8b0eOUD6Wtmua/view?usp=sharing
* Unpickle and use the extracted data as follows. Extracted data is in numpy format.
``` python3
  import util
  X = util.unpickle('scope_data.pkl')
  print( 'length of list is ', len(x))
  print( 'keys of each element is', X[0].keys() )

  numerical_id = X[0]['nID']
  scope_id = X[0]['nID']
  sequence = X[0]['SEQ']
  class = X[0]['CLS']
  backbone_chain = X[0]['CA']
  dist_matrix = util.distm( X[0]['CA'] )

```
