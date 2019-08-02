from app import app
from flask import render_template, request
from app.models import model

def findGreatestPoints(chasePoints, morganStanleyPoints, boaPoints, wellsFargoPoints, goldmanPoints):
    greatestPoints = 0
    myList = [chasePoints, morganStanleyPoints, boaPoints, wellsFargoPoints, goldmanPoints]
    for element in myList:
        if element>greatestPoints:
            greatestPoints = element
            
    if greatestPoints == chasePoints:
        return 'chase.html'
    elif greatestPoints == boaPoints:
        return 'boa.html'
    elif greatestPoints == wellsFargoPoints:
        return 'wellsfargo.html'
    elif greatestPoints == goldmanPoints:
        return 'goldmansachs.html'
    else: # greatestPoints == morganStanleyPoints:
        return 'morganstan.html'
    
   

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
        
    
@app.route('/whichBankForYouStocks', methods = ['GET','POST'])  
def whichBankForYouStocks():
    if request.method == 'GET':
        
        # return "how did you get here? go back to homepage! DEtonatIoN commences in 0.5 seconds"
        return render_template('index.html')
    else:
        userdata = request.form
        theirName = userdata['name']
        q1Answers = userdata['question1']
        q2Answers = userdata['question2']
        q3Answers = userdata['question3']
        q4Answers = userdata['question4']
        q5Answers = userdata['question5']
        
        chasePoints = 0
        boaPoints = 0
        goldmanPoints = 0
        morganStanleyPoints = 0
        wellsFargoPoints = 0
        
        if q1Answers == "prevExperienceYes":
            chasePoints += 1
        if q2Answers == "commFreeTradeYes":
            chasePoints += 1
        if q3Answers == "connCheckingYes":
            boaPoints += 1
        if q4Answers == "feesNo":
            goldmanPoints += 1
        if q5Answers == "taxLostHarvestingYes":
            morganStanleyPoints += 1
            
        bestBankForYou = findGreatestPoints(chasePoints, morganStanleyPoints, boaPoints, wellsFargoPoints, goldmanPoints)
        print(bestBankForYou)
        if bestBankForYou == 'goldmansachs.html':
            return render_template('goldmansachs.html', name = theirName)
        elif bestBankForYou == 'morgstan.html':
            return render_template('morganstan.html', name = theirName)
        elif bestBankForYou == 'boa.html':
            return render_template('boa.html', name = theirName)
        elif bestBankForYou == 'wellsfargo.html':
            return render_template('wellsfargo.html', name = theirName)
        else:
            return render_template('chase.html', name = theirName)
        
        
        
        
@app.route('/whichBankForYouCorporate', methods = ['GET','POST'])  
def whichBankForYouCorporate():
    if request.method == 'GET':
        
        # return "how did you get here? go back to homepage! DEtonatIoN commences in 0.5 seconds"
        return render_template('index.html')
    else:
        userdata = request.form
        theirName = userdata['name']
        q1Answers = userdata['question1']
        q2Answers = userdata['question2']
        q3Answers = userdata['question3']
        q4Answers = userdata['question4']

        chasePoints = 0
        boaPoints = 0
        goldmanPoints = 0
        morganStanleyPoints = 0
        wellsFargoPoints = 0
        
        if q1Answers == "ratingYes":
            chasePoints += 1
        if q2Answers == "branchesYes":
            wellsFargoPoints += 1
        if q3Answers == "costBusinessYes":
            boaPoints += 1
        if q4Answers == "businessCreditCardYes":
            chasePoints += 1
      
            
        bestBankForYou = findGreatestPoints(chasePoints, morganStanleyPoints, boaPoints, wellsFargoPoints, goldmanPoints)
        print(bestBankForYou)
        if bestBankForYou == 'goldmansachs.html':
            return render_template('goldmansachs.html', name = theirName)
        elif bestBankForYou == 'morgstan.html':
            return render_template('morganstan.html', name = theirName)
        elif bestBankForYou == 'boa.html':
            return render_template('boa.html', name = theirName)
        elif bestBankForYou == 'wellsfargo.html':
            return render_template('wellsfargo.html', name = theirName)
        else:
            return render_template('chase.html', name = theirName)
        
        
        
        
        
        
@app.route('/whichBankForYouPersonal', methods = ['GET','POST'])  
def whichBankForYouPersonal():
    if request.method == 'GET':
        
        # return "how did you get here? go back to homepage! DEtonatIoN commences in 0.5 seconds"
        return render_template('index.html')
    else:
        userdata = request.form
        theirName = userdata['name']
        q1Answers = userdata['question1']
        q2Answers = userdata['question2']
        q3Answers = userdata['question3']
        q4Answers = userdata['question4']
        q5Answers = userdata['question5']
        q6Answers = userdata['question6']

        
        chasePoints = 0
        boaPoints = 0
        goldmanPoints = 0
        morganStanleyPoints = 0
        wellsFargoPoints = 0
        
        if q1Answers == "atmAccessYes":
            wellsFargoPoints += 1
        if q2Answers == "easyAppYes":
            chasePoints += 1
        if q3Answers == "zeroLiabYes":
            boaPoints += 1
        if q4Answers == "nationWideYes":
            chasePoints += 1
        if q5Answers == "ATMDepositYes":
            chasePoints += 1
        if q6Answers == "checkingFeeNo":
            wellsFargoPoints += 1
            
        bestBankForYou = findGreatestPoints(chasePoints, morganStanleyPoints, boaPoints, wellsFargoPoints, goldmanPoints)
        print(bestBankForYou)
        if bestBankForYou == 'goldmansachs.html':
            return render_template('goldmansachs.html', name = theirName)
        elif bestBankForYou == 'morgstan.html':
            return render_template('morganstan.html', name = theirName)
        elif bestBankForYou == 'boa.html':
            return render_template('boa.html', name = theirName)
        elif bestBankForYou == 'wellsfargo.html':
            return render_template('wellsfargo.html', name = theirName)
        else:
            return render_template('chase.html', name = theirName)
        
        
        
        
                
            
# @app.route('/')
@app.route('/bank')
def bank():
    return render_template('bank.html')
# @app.route('/')
@app.route('/boa')
def boa():
    return render_template('boa.html')
# @app.route('/')
@app.route('/creators')
def us():
    return render_template('creators.html')

# @app.route('/')
@app.route('/personal')
def personal():
    return render_template('personal.html')
# @app.route('/')
@app.route('/wellsfargo')
def wellsfargol():
    return render_template('wellsfargo.html')
# @app.route('/')
@app.route('/goldmansachs')
def goldmansachs():
    return render_template('goldmansachs.html')
# @app.route('/')
@app.route('/chase')
def chase():
    return render_template('chase.html')
# @app.route('/')
@app.route('/ourbanks')
def ourbanks():
    return render_template('ourbanks.html')
# @app.route('/')
@app.route('/morgstan')
def morgstans():
    return render_template('morgstan.html')

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



