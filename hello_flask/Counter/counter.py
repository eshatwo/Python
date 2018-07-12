from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'counter'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    print(session)
    print(request.cookies)
    return render_template('index.html', count=session['count'])

@app.route('/plus')
def plus():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.pop('count')
    return redirect('/')

app.run(debug=True)


