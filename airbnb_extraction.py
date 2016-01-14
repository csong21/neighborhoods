import re
import csv
import os
import glob

"""Extract the description of the neighborhood.""" 
def extract_description(filename):
	fhand = open(filename)
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

def extract_gray_tab(filename):
    fhand = open(filename)
    text = fhand.read()
    gray_tab_reg = 'class="large gray btn"&gt;&lt;span class="name"&gt;([a-zA-Z ]+?)&lt;/span&gt;&lt;/a&gt;&lt;/li&gt;</span>'
    tag_list = re.findall(gray_tab_reg,text)
    tag_string = ''
    for tag in tag_list:
        tag_string += (tag + ' ')
    return tag_string

def extract_community_says(filename):
    fhand = open(filename)
    text = fhand.read()
    community_says_reg = 'class="neighborhood-tag"&gt;([a-zA-Z ]+?)</span></p>'
    tag_list = re.findall(community_says_reg,text)
    tag_string = ''
    for tag in tag_list:
        tag_string += (tag + ' ')
    return tag_string

def construct_dict(name, description, tags):
	arrond = dict(neighborhood=None, desc=None, tags=None)
	arrond['neighborhood'] = name
	arrond['desc'] = description
	arrond['tags'] = tags
	return arrond

def csv_save(arronds, csvfile):
	with open(csvfile,'wb') as f:
		w = csv.writer(f)
		w.writerow(arronds[0].keys())
		for arrond in arronds:
			w.writerow(arrond.values())

def main():
	path = os.getcwd() #get the path at terminal when executing this file
	city_input = raw_input('enter the city:') #to get all the neighborhood names in New York, type "new_york"; for Paris, type in "paris"
	folderpath = '%s/data/%s'%(path, city_input) #for new york, folderpath = '/Volumes/CECELIA/ohparis/neighborhoods/data/new_york'
	csvfile = '%s.csv'% city_input
	arronds_row = []
	os.chdir(folderpath)
	arronds_city = glob.glob("*.txt")
	for neighborhood in arronds_city:
		filepath = '%s/%s'%(folderpath, neighborhood)
		description = extract_description(filepath)
		tags = extract_gray_tab(filepath) + extract_community_says(filepath)
		arrond = construct_dict(neighborhood[:-4], description, tags) #chop off ".txt"
		arronds_row.append(arrond)

	csv_save(arronds_row, csvfile)

if __name__ == '__main__':
	main()