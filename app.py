from flask import Flask, render_template, request, flash, url_for, redirect
import random

app = Flask(__name__)

app.secret_key = "panchait" # necessary, if we are using flash and session

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/game')
def page1():
    return render_template("page1.html")

@app.route('/page', methods=["POST"])
def difficulties():

    if request.method == "POST":

        turns = request.form.get("turns", "10")
        turns = int(turns)

        turn = request.form["difficulty"]

        if turn == "e":
            no = random.randint(1, 10)
            
        elif turn == "n":
            no = random.randint(1, 100)
        
        elif turn == "h":
            no = random.randint(1, 1000)

        
        guess = request.form.get("guess", "")
        if guess == "":
            guess = no


        value_hold = request.form.get("values", "") # if we use request.form["values"] it will raise an key error so thats why we are using this
        new = request.form.get("value_hold", "")
        pss = request.form.get("pss", "Hints")

        if value_hold == "b":
            new = new[0:-1]
            value = new
        
        elif value_hold == "s":
            if new == "":
                value = ""
            
            else:
                if int(new) == int(guess):
                    return render_template("win.html")
                
                elif int(new) > int(guess):
                    pss = "Guess Is Greater"

                elif int(new) < int(guess):
                    pss = "Guess Is Lesser"
                
                value = ""

                turns = turns - 1

                if turns == 0:
                    return render_template("loss.html")
                

        else:
            value = ""
            value = new + value_hold


    return render_template("game.html",pss = pss ,guess = guess, turns = turns, value_hold = value_hold, value = value )

@app.route('/', methods=['POST', 'GET'])
def register():

    name = ""
    password = ""

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']

    
        with open("D:\\Name.txt", "a+") as file:
            file.seek(0)
            names = file.read().splitlines()
        
        with open("D:\\Password.txt", "a+") as file:
            file.seek(0) # when we open in append the pointer is in the end of the file so we move it to the start
            passwords = file.read().splitlines()
        
        if name in names:
            flash("User_name Is Already In Use !", "danger")
            return  redirect(url_for('register'))
            
        with open("D:\\Name.txt", "a") as file:
            file.write(name + "\n")
        
        with open("D:\\Password.txt", "a") as file:
            file.write(password + "\n")
        
        flash("Successfuly Registered !", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():

    name = ""
    password = ""

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
    
        with open("D:\\Name.txt", "a+") as file:
            file.seek(0)
            names = file.read().splitlines()
        
        with open("D:\\Password.txt", "a+") as file:
            file.seek(0) # when we open in append the pointer is in the end of the file so we move it to the start
            passwords = file.read().splitlines()
        
        if name in names and password in passwords:
            return redirect(url_for('home')) # using redirect instead of render tamplate is because it will remove the flash meassage once its show, in render tamplate it permenantly remain
        
        else:
            flash("Wrong Password/Name !", "danger")
            return redirect(url_for("login"))
    
    # When the request method is GET, just render the login page
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)