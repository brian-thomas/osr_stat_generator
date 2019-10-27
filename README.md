# OSR Random Stat Generator

## About
Project to quickly generate stat-blocks for OSR (Old School Roleplaying) games. I use it to create sheets of random stats which my players may use to quickly get started creating their LoTFP (and other retro-clone D&D game) characters.

## Install
Should run without any additional libraries with python 3.7+. Possibly might run with Python 2 (untested, but hey, you should should upgrade!)

## Use
```bash
> python bin/generator.py
```
will product output which looks like:

```bash
-----------------------------------
SET   #1   #2   #3   #4   #5   #6 |
-----------------------------------
CON | 15 | 14 | 12 | 14 |  4 | 16 | 
DEX |  7 | 14 |  9 | 11 | 12 |  6 | 
INT | 13 | 12 | 16 | 12 | 10 | 14 | 
WIS | 13 |  8 | 13 | 12 | 17 | 12 | 
STR |  8 | 12 |  5 |  9 | 10 | 11 | 
CHA | 14 | 12 | 13 | 10 | 15 | 13 | 
-----------------------------------
AVG  11.7 12.0 11.3 11.3 11.3 12.0 
-----------------------------------
```
