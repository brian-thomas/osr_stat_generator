

""" 
Program to generate stats on command line to STDOUT.
"""

from osr_stat_generator.generator import generate_stats

def _horizontal_line_str (nrof_sets):
    hstring = "-----"
    for i in range(0,nrof_sets):
         hstring = hstring + "-----"
    return hstring

def _header_str (nrof_sets):
    hstring = "SET"
    for i in range(1,nrof_sets+1):
         hstring = hstring + "   #"+str(i) 
    return hstring + " |"

def print_stats(nrof_sets, with_average=False):

    print (_horizontal_line_str(nrof_sets))
    print (_header_str(nrof_sets))
    print (_horizontal_line_str(nrof_sets))
    stat_sets = generate_stats(nrof_sets)

    # set up the first row
    for stat_nr in range (0, 6):
        row_str = stat_sets[0]._Stat_Name[stat_nr] + " | " 
        for stat_set in stat_sets:
            stat = stat_set.stats[stat_nr]
            pad_stat = ""
            if stat.value < 10: pad_stat = " "
            row_str += pad_stat + str(stat.value) + " | "

        print (row_str)

    print (_horizontal_line_str(nrof_sets))

    if with_average:
        row_str = "AVG  " 
        for stat_set in stat_sets:
            row_str += '%3.1f' % (float(stat_set.sum()) / len(stat_set.stats)) + " " 
        print (row_str) 
        print (_horizontal_line_str(nrof_sets))

if __name__ == '__main__':
    # print a page of these
    for i in range(0,4):
        print_stats(6, with_average=True)

