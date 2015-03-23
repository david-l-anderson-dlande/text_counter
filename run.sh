#!/usr/bin/env bash
	

#make sure that my program has the proper permissions
chmod a+x wordcount_and_median.py

# finally execute my program, with the input directory wc_input and output the files in the directory wc_output
python ./wordcount_and_median.py ./wc_input ./wc_output
python wordcount_and_median.py wc_input wc_output
