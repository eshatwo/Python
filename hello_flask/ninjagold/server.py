from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'DB'

@app.route('/')
def index():
    if 'gold' in session:
        print(session['gold'])
    else:
        session['gold']=0
        session['activities'] = []
    return render_template('index.html', gold=session['gold'], activities =session['activities'])

@app.route('/process_money',methods=['POST'])
def process_money():
    now = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
    if 'farm' in request.form:
        rand = random.randrange(10,21)
        session['gold'] += rand
        session['activities'].append(f'<p class="green">Earned {rand} gold from the Farm! ({now})</p>')
    if 'cave' in request.form:
        rand = random.randrange(5,11)
        session['gold'] += rand
        session['activities'].append(f'<p class="green">Earned {rand} gold from the Cave! ({now})</p>')
    if 'house' in request.form:
        rand = random.randrange(2,6)
        session['gold'] += rand
        session['activities'].append(f'<p class="green">Earned {rand} gold from the House! ({now})</p>')
    if 'casino' in request.form:
        luck = random.randrange(0,3)
        rand = random.randrange(0,51)
        if luck == 0:
            session['gold'] += rand
            session['activities'].append(f'<p class="green">Entered Casino and earned {rand} gold! ({now})</p>')
        else:
            if session['gold'] - rand < 0:
                session['gold'] = 0
                session['activities'].append(f'<p class="red">Entered Casino and lost all of your gold! ({now})</p>')
            else: 
                session['gold'] -= rand
                session['activities'].append(f'<p class="red">Entered Casino and lost {rand} gold... Ouch.. ({now})</p>')
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)