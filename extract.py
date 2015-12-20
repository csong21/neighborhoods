import re
import csv

"""Extract the description of the neighborhood.""" 
def extract_description(fhand):
	for line in fhand:
		line = line.strip()

		if line.startswith('<p class="p2"><span class="s1">&lt;meta name="description"'):
			words = line.split()
			nth_startword = 0
			nth_endword = 0
			i = 0
			for word in words:
				if word == 'name="description"':
					nth_startword = i
					i +=1
				else:
					i +=1
				nth_endword = i
			wanted = words[nth_startword+1: nth_endword+1]
			delimiter = ' '
			content = delimiter.join(wanted)

			m = 0
			nth_startletter = 0
			nth_endletter = 0
			foundstart_flag = -1
			for letter in content:
				if letter == '"':
					if foundstart_flag == -1:
						nth_startletter = m
						foundstart_flag = 1
					nth_endletter = m
					m +=1
				else:
					m +=1
			content = content[nth_startletter+1: nth_endletter]
			#content.replace("&amp;#x27; ", "\'")
			return content

def construct_dict(name, description):
	arrond = dict(neighborhood=None, desc=None, tags=None)
	arrond['neighborhood'] = name
	arrond['desc'] = description
	return arrond

def csv_save(arrond):
	f = open('nyparis.csv', 'wb')
	w = csv.DictWriter(f, arrond.keys())
	w.writerow(arrond)
	f.close()

def main():
	"""neighborhoods = ['le-marais', 'quartier-latin', 
					'bastille', 'pigalle-saint-georges', 
					'montmartre', 'opera-grands-boulevards', 
					'champs-elysees', 'la-villette', 
					'canal-saint-martin', 'republique', 
					'saint-germain-des-pres-odeon', 'montparnasse',
					'pere-lachaise-menilmontant']"""
	neighborhoods = ['quartier-latin']
	for neighborhood in neighborhoods:
		print neighborhood
		filename = '%s.txt' % neighborhood
		fhand = open(filename)
		description = extract_description(fhand)
		arrond = construct_dict(neighborhood, description)
		csv_save(arrond)

main()