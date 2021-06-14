#!/bin/bash
rm -r tmp
mkdir tmp
mmseqs createdb ./test.fasta queryDB
mmseqs createdb ./train.fasta targetDB
mmseqs createindex targetDB tmp
rm -r resultDB.*
mmseqs search queryDB targetDB resultDB tmp --min-seq-id 0.3
mmseqs convertalis queryDB targetDB resultDB resultDB.m8
#cat resultDB.m8
