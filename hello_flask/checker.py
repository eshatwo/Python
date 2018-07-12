from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)    

@app.route('/')         
def checker():
    return render_template('checker.html', row=8, column=8)  

@app.route('/<x>/<y>')
def count(x, y):
    return render_template('checker.html', row=int(x), column=int(y))

if __name__=="__main__":
	app.run(debug=True)
