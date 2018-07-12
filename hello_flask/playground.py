from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)    


@app.route('/')         
def playground():
    return 'Playground'  

@app.route('/play')
def boxes():
    return render_template('playground.html', times=3)

@app.route('/play/<x>')
def boxer(x):
    return render_template('playground.html', times=int(x))

@app.route('/play/<x>/<color>')
def color(x, color):
    return render_template('playground.html', times=int(x), color=color)

if __name__=="__main__":
	app.run(debug=True)
