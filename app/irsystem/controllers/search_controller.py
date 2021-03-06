from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "beepboop: Bot Finder"
net_id = "Fawn Wong (fyw6), Cindy Wang (cw653), Danna Greenberg (dg489), Stephanie Hogan (sjh278), Annie Zhang (zz229)"

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Search results: "
		# data should be a list of dictionaries d for now, in decreasing order of importance
		# each dictionary d has a rank field and a list of results, e, of that rank for the three search categories
		# for now make sure to define the list e in the order of bot name, bot comment, user comment searches
		# each element in list e is a dictionary representing a result
		data = [
			{"rank": "1", 
			"list": [
				{"name": "A Bot 1", "comment": "A Comment 1", "link": "http://www.google.com", "category": "bot_name"},
				{"name": "B Bot 1", "comment": "B Comment 1", "link": "http://www.google.com", "category": "bot_comments"},
				{"name": "C Bot 1", "comment": "C Comment 1", "link": "http://www.google.com", "category": "user_comments"}
			]},
			{"rank": "2", 
			"list": [
				{"name": "A Bot 2", "comment": "A Comment 2", "link": "http://www.google.com", "category": "bot_name"},
				{"name": "B Bot 2", "comment": "B Comment 2", "link": "http://www.google.com", "category": "bot_comments"},
				{"name": "C Bot 2", "comment": "C Comment 2", "link": "http://www.google.com", "category": "user_comments"}
			]},
			{"rank": "3", 
			"list": [
				{"name": "A Bot 3", "comment": "A Comment 3", "link": "http://www.google.com", "category": "bot_name"},
				{"name": "B Bot 3", "comment": "B Comment 3", "link": "http://www.google.com", "category": "bot_comments"},
				{"name": "C Bot 3", "comment": "C Comment 3", "link": "http://www.google.com", "category": "user_comments"}
			]},
			{"rank": "4", 
			"list": [
				{"name": "A Bot 4", "comment": "A Comment 4", "link": "http://www.google.com", "category": "bot_name"},
				{"name": "B Bot 4", "comment": "B Comment 4", "link": "http://www.google.com", "category": "bot_comments"},
				{"name": "C Bot 4", "comment": "C Comment 4", "link": "http://www.google.com", "category": "user_comments"}
			]},
			{"rank": "5", 
			"list": [
				{"name": "A Bot 5", "comment": "A Comment 5", "link": "http://www.google.com", "category": "bot_name"},
				{"name": "B Bot 5", "comment": "B Comment 5", "link": "http://www.google.com", "category": "bot_comments"},
				{"name": "C Bot 5", "comment": "C Comment 5", "link": "http://www.google.com", "category": "user_comments"}
			]},
		]
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)



