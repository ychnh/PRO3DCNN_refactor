#!/bin/bash
rm -r tmp
mmseqs createdb ./query.fasta queryDB
mmseqs createdb ./blank.fasta targetDB
mmseqs createindex targetDB tmp
rm -r resultDB.*
#mmseqs search queryDB targetDB resultDB tmp
mmseqs search queryDB targetDB resultDB tmp --min-seq-id 0.3
mmseqs convertalis queryDB targetDB resultDB resultDB.m8
cat resultsDB.m8
