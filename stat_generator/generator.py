

""" OSR (LOTFP) stat generator. """

import dice

class Stat_Set(object):

    @property
    def bonuses(self):
        return self._bonuses

    @property
    def stats(self):
        return self._stats
        
    def __str__(self):
        string = ""
        for i in range(0, len(self._stats)): 
            string = string + " " + str(self.stats[i]) + " ("+str(self.bonuses[i]) + ")" 
        return string

    def __init__(self, stats, bonuses):
        self._stats = stats
        self._bonuses = bonuses

def _get_bonus(attribute):

    if attribute <= 3:
        return -3
    if attribute >= 4 and attribute <= 5:
        return -2
    if attribute >= 6 and attribute <= 8:
        return -1
    if attribute >= 13 and attribute <= 15:
        return 1
    if attribute >= 16 and attribute <= 17:
        return 2
    if attribute >= 18:
        return 3
    # the default
    return 0

def generate_stats(nrof_sets=1):

    stat_sets = [] 
    while (nrof_sets > 0):
        stats = []
        for i in range (0, 6):
            stats.append(dice.xdy(3,6))

        bonuses = [_get_bonus(s) for s in stats]

        # no "hopeless" characters
        if sum(bonuses) < 1:
            continue

        stat_sets.append(Stat_Set(stats, bonuses))

        nrof_sets -= 1

    return stat_sets

Stat_Name = ["CON", "DEX", "INT", "WIS", "STR", "CHA"]

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
    for stat_nr in range (0, 6):
        row_str = Stat_Name[stat_nr] + " | " 
        for stat_set in stat_sets:
            stat = stat_set.stats[stat_nr]
            pad_stat = ""
            if stat < 10: pad_stat = " "
            row_str += pad_stat + str(stat) + " | "

        print (row_str)

    print (_horizontal_line_str(nrof_sets))

    if with_average:
        row_str = "AVG  " 
        for stat_set in stat_sets:
            row_str += '%3.1f' % (float(sum(stat_set.stats)) / len(stat_set.stats)) + " " 
        print row_str
        print (_horizontal_line_str(nrof_sets))

if __name__ == '__main__':
    # print a page of these
    for i in range(0,4):
        print_stats(6, with_average=True)

