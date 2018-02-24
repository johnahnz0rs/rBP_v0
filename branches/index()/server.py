# in this branch, i want to implement:
	# 1. quote of the day on the splash page
		# 1a. qotd displayed in div .quote
			# (future release) - add scrollbar so i can read more quotes, as desired?? will this functionality be useful in increasing motivation or be a distraction to getting started?
		# 1b. add the ability to add fav quotes - @app.route('/add_quote')
		
	# 2. collapsible list of daily desires/habits
		# 2a. the list should be of each habit i want to build, e.g.
			 # - Bullet Journal/To-Do lists
			 	# - what's on today's docket?
			 	# - what did i accomplish today + reflection
			 	# - make tomorrow's to-do list
			# - Study:
			 	# - khanacademy (10 min)
			 	# - duolingo (5-10 min)
			 	# - codingdojo and/or some language docs (30-240 min)
			 # - First you get the money:
			 	# - upwork
			 	# - craigslist
			 	# - preferred companies
			 	# - etc
			 # - Calories:
			 	# - food tracker
			 		# (future release) - import food tracker from app
			 	# - pick tomorrow's meals
			 		# (future release) - pick 2-3 days out, 1 week out


from flask import Flask, redirect, render_template, session, url_for, request
import random

app = Flask(__name__)



@app.route('/')
def index():
	session['quotes_list'] = [
	'"You dont get in life what you want; you get in life what you are. So who are you? Everything in this lifeis about the story that you are telling yourself. Who YOU believe you are." - "Unbreakable" by Redfrost Motivation',
	'"Esquire is a title for [members of the landed gentry] above the rank of gentlemen and below the rank of knight." - Roman J. Israel, Esq.',
	'"Difference between the uni\'s and the Strike Team is you don\'t hand your superior pieces to a puzzle; you hand them the whole pictures." - The Shield',
	'"Truth is like poetry. And most people fucking hate poetry. - overheard in a DC bar" - The Big Short (2015)',
	'"What you reveal, you heal." - Jay-Z',
	'"I\'m out here in grind mode, wrapped up in the paper chase / I wanna fuck a fine ho and candy paint the 88." - Mr. Scarface',
	'"1. Knowledge, 2. Strategy, 3. Execute" - Tai Lopez',
	'"Lesson 1: Introduce logic to women; Lesson 2: A good relationship is an insecure woman; Lesson 3: Don\'t be a time ho; Lesson 4: Do not negotiate with the ladies; Lesson 5: Do not ever flinch; Lesson 6: Always prioritize your happines; Lesson 7: Stop editing yourself." - Patrice O\'Neal'
	]

	session['quotes_count'] = len(session['quotes_list'])
	session['random_num'] = random.randrange(1,session['quotes_count'])

	# set the qotd
	session['random_quote'] = session['quotes_list'][session['random_num']]

	return render_template('index.html')


@app.route('/add_quote')
def add_quote():
	return render_template('add_quote.html')


app.secret_key = '00'
app.run(debug=True)