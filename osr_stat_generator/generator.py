

""" 
OSR (LOTFP) stat generator. 
"""

import random

def d(num_sides):
    """ 
    Represents rolling a die of size 'num_sides'. 
    Returns random number from that size die
    """
    return random.randint(1, num_sides)


def xdy(num_dice, num_sides):
    """ represents rolling num_dice of size num_sides.
    Returns random number from that many dice being 'rolled'. 
    """
    return sum(d(num_sides) for i in range(num_dice))


class LotFP_Stat (object):

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

    @property
    def bonus(self): return self._bonus

    @property
    def name(self): return self._name

    @property
    def value(self): return self._value

    def __str__(self):
        return (f"%s : %s(%s)" % (self.name, self.value, self.bonus))

    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._bonus = LotFP_Stat._get_bonus(value)


class Stat_Set(object):
    """ 
    Define a package of OSR/DnD stats 
    """

    _Stat_Name = ["CON", "DEX", "INT", "WIS", "STR", "CHA"]

    @property
    def stats(self)->list:
        return self._stats

    def sum(self)->int:
        # get a summed value for all stats in this set
        ssum = 0
        for s in self.stats:
            ssum += s.value 
        return ssum

    @property
    def is_hopeless(self)->bool:
        """ Determine if the character is so poorly stated they have
        bonus sum less than 1.
        """
        bonuses = [s.bonus for s in self._stats]
        if sum(bonuses) < 1:
            return True
        return False
        
    def __str__(self)->str:
        string = ""
        for stat in stats:
            string = string + " " + str(stat.value) + " ("+str(stat.bonus) + ")" 
        return string

    def __init__(self, stats):
        self._stats = []

        for i in range(0,len(stats)):
            self._stats.append(LotFP_Stat(Stat_Set._Stat_Name[i], stats[i]))


def generate_stats (nrof_sets:int=1, no_hopeless_char:bool=True)->list:
    """ Generate stats for a character.
    """

    stat_sets = []
    while (nrof_sets > 0):
        stats = []
        for i in range (0, 6):
            stats.append(xdy(3,6))

        stat_set = Stat_Set(stats)

        # no "hopeless" characters
        if no_hopeless_char and stat_set.is_hopeless:
            continue

        stat_sets.append(stat_set)

        nrof_sets -= 1

    return stat_sets

