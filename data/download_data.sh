#/bin/bash
echo 'Downing SCOPe Data (1-7)'
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-1.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-2.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-3.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-4.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-5.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-6.tgz
wget https://scop.berkeley.edu/downloads/pdbstyle/pdbstyle-2.07-7.tgz
echo 'Extracting Data (1-7)'
tar -xzf pdbstyle-2.07-1.tgz
tar -xzf pdbstyle-2.07-2.tgz
tar -xzf pdbstyle-2.07-3.tgz
tar -xzf pdbstyle-2.07-4.tgz
tar -xzf pdbstyle-2.07-5.tgz
tar -xzf pdbstyle-2.07-6.tgz
tar -xzf pdbstyle-2.07-7.tgz
echo 'Remove tgz files Data (1-7)'
rm pdbstyle-2.07-1.tgz
rm pdbstyle-2.07-2.tgz
rm pdbstyle-2.07-3.tgz
rm pdbstyle-2.07-4.tgz
rm pdbstyle-2.07-5.tgz
rm pdbstyle-2.07-6.tgz
rm pdbstyle-2.07-7.tgz

echo 'Processing Data'
python3 process_data.py
