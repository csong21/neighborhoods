
# coding: utf-8
# # Matching neighborhoods from different cities by applying nearest neighbor model to texts retrieved from Airbnb
import graphlab
import airbnb_extraction
# Load text data from csv files

city = raw_input('enter the city:')
csvfile = 'matching_%s.csv'%city
#set path
nb_new_york = graphlab.SFrame('/Volumes/CECELIA/ohparis/neighborhoods/data/new_york/new_york.csv')
nb_paris = graphlab.SFrame('/Volumes/CECELIA/ohparis/neighborhoods/data/paris/paris.csv')

# Data contains:  name of neighborhood, tags and description.

#Compute TF-IDF for the corpus. To give more weight to informative words, we weigh them by their TF-IDF scores.
#First calculate the work count for the texts in description and tag.
nb_new_york['word_count_tags'] = graphlab.text_analytics.count_words(nb_new_york['tags'])
nb_new_york['word_count_desc'] = graphlab.text_analytics.count_words(nb_new_york['desc'])
nb_paris['word_count_tags'] = graphlab.text_analytics.count_words(nb_paris['tags'])
nb_paris['word_count_desc'] = graphlab.text_analytics.count_words(nb_paris['desc'])

#Calculate tfidf and add as a column to table
nb_new_york['tfidf_tags'] = graphlab.text_analytics.tf_idf(nb_new_york['word_count_tags'])
nb_new_york['tfidf_desc'] = graphlab.text_analytics.tf_idf(nb_new_york['word_count_desc'])
nb_paris['tfidf_tags'] = graphlab.text_analytics.tf_idf(nb_paris['word_count_tags'])
nb_paris['tfidf_desc'] = graphlab.text_analytics.tf_idf(nb_paris['word_count_desc'])

result_row = []
if city == 'paris':
	neighborhoods = nb_paris['neighborhood']
	for one in neighborhoods:
		itneighbor = nb_paris[nb_paris['neighborhood'] == one]
		m_dualcity = nb_new_york.append(itneighbor)
		knn_model = graphlab.nearest_neighbors.create(m_dualcity,features=['tfidf_tags'],label='neighborhood')
		counterpart = knn_model.query(itneighbor)
		result = dict(neighborhood=None, rank1=None, rank2=None, rank3=None, rank4=None)
		result['neighborhood'] = one
		result['rank1'] = counterpart['reference_label'][1]
		result['rank2'] = counterpart['reference_label'][2]
		result['rank3'] = counterpart['reference_label'][3]
		result['rank4'] = counterpart['reference_label'][4]	
		result_row.append(result)

elif city == 'new_york':
	neighborhoods = nb_new_york['neighborhood']
	for one in neighborhoods:
		itneighbor = nb_new_york[nb_new_york['neighborhood'] == one]
		m_dualcity = nb_paris.append(itneighbor)
		knn_model = graphlab.nearest_neighbors.create(m_dualcity,features=['tfidf_tags'],label='neighborhood')
		counterpart = knn_model.query(itneighbor)
		result = dict(neighborhood=None, rank1=None, rank2=None, rank3=None, rank4=None)
		result['neighborhood'] = one
		result['rank1'] = counterpart['reference_label'][1]
		result['rank2'] = counterpart['reference_label'][2]
		result['rank3'] = counterpart['reference_label'][3]
		result['rank4'] = counterpart['reference_label'][4]	
		result_row.append(result)

airbnb_extraction.csv_save(result_row, csvfile)
