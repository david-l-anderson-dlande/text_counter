import os
from statistics import median
from collections import Counter
import re


def wc_m_main(input_folder = 'wc_input', output_folder = 'wc_output',\
              med_out_file = 'med_result.txt', wc_out_file = 'wc_result.txt'):
    linelengths, fulldict, files_list = initializer(input_folder)
    linelengths, fulldict = file_reader(linelengths, fulldict,\
                                        files_list, input_folder)
    count_writer(output_folder, wc_out_file, fulldict)
    median_writer(output_folder, med_out_file, linelengths)



def initializer(input_folder_i):
    line_length_list = [];
    dictionary_initializer = Counter();
    input_files_list = os.listdir(input_folder_i)
    input_files_list.sort()
    return line_length_list, dictionary_initializer, input_files_list


def file_reader(linelengths_fr, fulldict_fr, files_list_fr, input_folder_fr):
    for file in files_list_fr:
        with open(input_folder_fr+'/'+file, 'r') as f:
            for line in f:
                line_list = cleaner_lister(line)
                linelengths_fr.append( len(line_list) )
                linedict = Counter(line_list)
                fulldict_fr = fulldict_fr + linedict
            f.closed
    return linelengths_fr, fulldict_fr

def cleaner_lister(incoming_string):
    incoming_string = re.sub('[-\'_]', '', incoming_string);
    #removes hyphens and apostrophes
    incoming_string = re.sub('[^a-zA-Z0-9_]', ' ', incoming_string)
    #replaces all other nonalphanumeric characters with spaces
    incoming_string = incoming_string.lower()
    outgoing_list = incoming_string.split()
    return outgoing_list

     

def count_writer(output_folder, wc_out_file, fulldict_cw):
    with open(output_folder+'/'+wc_out_file, 'w') as d:
        for item in sorted( fulldict_cw.keys() ):
            out_line = str(item)+'\t'+str( fulldict_cw[item] )+'\n'
            d.write(out_line)
        d.closed

def median_writer(output_folder, med_out_file, linelengths_mw):
    with open(output_folder+'/'+med_out_file, 'w') as m:
        for item in range( len(linelengths_mw) ):
            m.write('{0:.1f}\n'.format( median(linelengths_mw[:item+1]) ) )
        m.closed



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        wc_m_main( str(sys.argv[1]), str(sys.argv[2]) )
    elif len(sys.argv) == 2:
        wc_m_main( str(sys.argv[1]) )
    else:
        wc_m_main()
 




