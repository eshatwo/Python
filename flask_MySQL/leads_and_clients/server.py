from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

mysql = connectToMySQL('lead_gen_business')

@app.route('/')
def index():
    all_clients = mysql.query_db("SELECT clients.client_id, CONCAT(clients.first_name, ' ',  clients.last_name) AS name, COUNT(*) as leads FROM clients JOIN sites ON sites.client_id=clients.client_id JOIN leads ON sites.site_id=leads.site_id GROUP BY clients.client_id")
    return render_template('index.html', clients = all_clients)



if __name__ == "__main__":
    app.run(debug=True)