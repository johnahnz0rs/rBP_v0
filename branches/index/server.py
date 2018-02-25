


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
	print session['quotes_list']

	return render_template('index.html')


@app.route('/add_quote', methods=['post'])
def add_quote():
	# add new quote
	# session['quotes_list'].append('some string')
	new_quote = ''
	for char in request.form[
	'new_quote']:
		if char == '\'':
			new_quote += str('\'')
		elif char == '\"':
			new_quote += str('\"')
		else:
			new_quote += str(char)
	session['quotes_list'].append(str(new_quote))
	print session['quotes_list']
	# print session['quotes_list']['quotes_count']

	return redirect('/')


app.secret_key = '00'
app.run(debug=True)