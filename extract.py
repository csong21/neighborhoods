
# coding: utf-8

# In[3]:

import re


# In[129]:

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
			print content

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
            
def main():
    neighborhoods = ['le-marais', 'quartier-latin', 
					'bastille', 'pigalle-saint-georges', 
					'montmartre', 'opera-grands-boulevards', 
					'champs-elysees', 'la-villette', 
					'canal-saint-martin', 'republique', 
					'saint-germain-des-pres-odeon', 'montparnasse',
					'pere-lachaise-menilmontant']
    for neighborhood in neighborhoods:
        filename = '%s.txt' % neighborhood
        print neighborhood
        print extract_gray_tab(filename) + extract_community_says(filename)
        print extract_description(filename)


# In[128]:

main()


# In[ ]:



