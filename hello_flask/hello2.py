from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)         
@app.route('/')         
def hello_world():
    #return 'Hello World!'  
    return render_template('hello2.html', phrase="hello", times=5)


if __name__=="__main__":   

                           
    app.run(debug=True)    

