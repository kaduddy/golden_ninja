from flask import Flask, render_template, request, redirect, session
import random 
from datetime import datetime                                         
app = Flask(__name__)  
app.secret_key = 'ThisIsSecret'                                                 
@app.route('/') 
def index():
	if 'gold' in session:
		pass
	else:
		session['gold'] = 0
	return render_template('index.html')
@app.route('/process_money', methods = ['POST'])
def game():
	if 'activities' not in session:
		session['activities'] = []
	if request.form['action'] == 'farm':
		session['farm_gold'] = random.randrange(10,21)
		session['gold'] += session['farm_gold']
		message = "Earned "+str(session['farm_gold'])+" golds from the farm! "+str(datetime.now().strftime("%Y-%m-%d %H:%M")) 
	elif request.form['action'] == 'cave':
		session['cave_gold'] = random.randrange(5,11)
		session['gold'] += session['cave_gold']
		message = "Earned "+str(session['cave_gold'])+" golds from the cave! "+str(datetime.now().strftime("%Y-%m-%d %H:%M"))	
	elif request.form['action'] == 'house':
		session['house_gold'] = random.randrange(2,5)
		session['gold'] += session['house_gold']
		message = "Earned "+str(session['house_gold'])+" golds from the house! "+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	elif request.form['action'] == 'casino':
		session['casino_gold'] = random.randrange(-50,50)
		session['gold'] += session['casino_gold']
		if session['casino_gold'] >= 0:
			message = "Entered a casino and lost"+str(session['casino_gold'])+" golds! "+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
		else:
			message = "Entered a casino and won"+str(session['casino_gold'])+ "golds!" +str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	# session['activities'].append(message)
	session['activities'] = [message] + session['activities']
	return redirect('/')
# @app.route('/reset', methods = ['POST'])
# def reset():
# 	session.pop('gold')
# 	return redirect('/')

app.run(debug=True) 