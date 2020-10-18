#!/usr/bin/env python

import pandas
import sys

counts = dict()
for sample in sys.argv[1:]:
	counts[sample] = {}
	with open(sample, 'r') as data:
		for line in data:
			try:
				ko = line.split('\t')[1].rstrip()
				counts[sample][ko] = counts[sample][ko] + 1
			except IndexError:
				continue
			except KeyError:
				counts[sample][ko] = 1
			except Exception as e:
				print("ERROR: {}".format(type(e)))

samples = sorted(counts.keys())
ko_list = list()
for sample in samples:
	ko_list = list(set(ko_list + counts[sample].keys()))

data = dict()
ko_list = sorted(ko_list)
for sample in samples:
	data[sample] = []
	for ko in ko_list:
		try:
			data[sample].append(counts[sample][ko])
		except KeyError:
			data[sample].append(0)
		except Exception as e:
			print("ERROR: {}".format(type(e)))

df = pandas.DataFrame(data=data, index=ko_list)
print(df.to_csv())
