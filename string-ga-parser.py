# string-ga-parser.py
# Erik Fredericks, 2020
# This file parses out the number of generations and execution time from
# the string search test and spits it out into an easier-to-read format for
# R.
import os

times       = []
gens        = []
strings     = []

pi_times    = []
pi_gens     = []
pi_strings  = []

pi4_times   = []
pi4_gens    = []
pi4_strings = []

for i in range(1,25):
  with open("PC-STRING-DATA/string-ga-{0}.txt".format(i)) as f:
    lines = f.readlines()
    gens.append(int(lines[0].split(':')[1].strip()))
    strings.append(lines[1][16:].strip())

  with open("PC-STRING-DATA/time-string-ga-{0}.txt".format(i)) as f:
    lines = f.readlines()
    line_time = lines[1].split()
    split_time = line_time[1].split('m')

    the_min = float(split_time[0].strip())
    the_sec = float(split_time[1].split('s')[0].strip())

    times.append((the_min * 60) + the_sec)

  with open("PI-STRING-DATA/string-ga-{0}-pi.txt".format(i)) as f:
    pi_lines = f.readlines()
    pi_gens.append(int(pi_lines[0].split(':')[1].strip()))
    pi_strings.append(pi_lines[1][16:].strip())

  with open("PI-STRING-DATA/time-string-ga-{0}-pi.txt".format(i)) as f:
    pi_lines = f.readlines()
    pi_line_time = pi_lines[1].split()
    pi_split_time = pi_line_time[1].split('m')

    pi_the_min = float(pi_split_time[0].strip())
    pi_the_sec = float(pi_split_time[1].split('s')[0].strip())

    pi_times.append((pi_the_min * 60) + pi_the_sec)

  with open("PI4-STRING-DATA/string-ga-{0}-pi.txt".format(i)) as f:
    pi4_lines = f.readlines()
    pi4_gens.append(int(pi4_lines[0].split(':')[1].strip()))
    pi4_strings.append(pi4_lines[1][16:].strip())

  with open("PI4-STRING-DATA/time-string-ga-{0}-pi.txt".format(i)) as f:
    pi4_lines = f.readlines()
    pi4_line_time = pi4_lines[1].split()
    pi4_split_time = pi4_line_time[1].split('m')

    pi4_the_min = float(pi4_split_time[0].strip())
    pi4_the_sec = float(pi4_split_time[1].split('s')[0].strip())

    pi4_times.append((pi4_the_min * 60) + pi4_the_sec)

# Sanity check
print(gens)
print(pi_gens)
print(pi4_gens)
print('---')
print(times)
print(pi_times)
print(pi4_times)
for s in pi_strings:
  print(s)

# Write to a CSV file for parsing in R
with open('string-search-results.csv','w') as f:
  f.write('Laptop Generations,Pi Generations,Pi4 Generations,Laptop Time,Pi Time,Pi4 Time\n')
  for i in range(len(gens)):
    f.write('{0},{1},{2},{3},{4},{5}\n'.format(gens[i],pi_gens[i],pi4_gens[i],times[i],pi_times[i],pi4_times[i]))

