from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key="ninja"

@app.route('/')
    
