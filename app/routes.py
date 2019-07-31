from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index', methods = ['GET', "POST"])
def index():
    return render_template('index.html')
  
@app.route('/routeToWhichPage', methods = ['GET','POST'])  
def routeToWhichPage():
    if request.method == 'GET':
        
        # return "how did you get here? go back to homepage! DEtonatIoN commences in 0.5 seconds"
        return render_template('index.html')
    else:
        userdata = request.form
        theirName = userdata['name']
        pageTheyWant = userdata['bankingForWhat']
        print(str(pageTheyWant))
        if pageTheyWant == "personal":
            return render_template('personal.html', name = theirName)
        elif pageTheyWant == "corporate":
            return render_template('corporate.html', name = theirName)
        elif pageTheyWant == "stocks":
            return render_template('stocks.html', name = theirName)
        else:
            return render_template('index.html')
        
    
# @app.route('/')
@app.route('/bank')
def bank():
    return render_template('bank.html')


# @app.route('/')
@app.route('/personal')
def personal():
    return render_template('personal.html')
# @app.route('/')
@app.route('/ourbanks')
def ourbanks():
    return render_template('ourbanks.html')

@app.route('/bank', methods  = ['GET', "POST"])
def questions():
    if request.method == 'GET':
        
        # return "how did you get here? go back to homepage! DEtonatIoN commences in 0.5 seconds"
        return render_template('bank.html')
    else:
        userdata = request.form #this puts data into a dictionary 
        name = userdata['name']
        # age = model.shout(userdata ["age"])#the key for this dictionaary comes from the name of corresponding input in the form on the html
        # return ("Hello " + nickname + " i love "+ breakfast + ", great choice")
        return render_template('bank.html', name = name)



