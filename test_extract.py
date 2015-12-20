import unnittest
import extract

class Test(unittest.TestCase):
	
	def construct_dict(self):
		name = 'bastille'
		description = 'Bastille represents Parisian romance—stylish, exotic strangers rub elbows in this dazzling, historical neighborhood. Its streetscapes cinema-worthy and its nightclubs legendary, Bastille’s centuries-old buildings share winding alleyways and broad promenades with ethnic eateries and avant-garde performance spaces, while its green spaces and gardens offer peaceful respites from the streets’ exuberant atmosphere. You won’t have trouble orienting yourself in this part of Paris—the July Column stands tall in the center of Place de la Bastille.'
		result = extract.construct_dict(name, description)
		expected = {'neighborhood': 'bastille'; 'desc': 'Bastille represents Parisian romance—stylish, exotic strangers rub elbows in this dazzling, historical neighborhood. Its streetscapes cinema-worthy and its nightclubs legendary, Bastille’s centuries-old buildings share winding alleyways and broad promenades with ethnic eateries and avant-garde performance spaces, while its green spaces and gardens offer peaceful respites from the streets’ exuberant atmosphere. You won’t have trouble orienting yourself in this part of Paris—the July Column stands tall in the center of Place de la Bastille.'}
		self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()