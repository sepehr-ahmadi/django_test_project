from flask import Flask, render_template, request
import requests
import psycopg2
import psycopg2.extras

import database_cafe

app = Flask(__name__, template_folder='templates')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/user')
def user():
    list_users = database_cafe.read_user_database()
    return render_template("user.html", list_users=list_users)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        print(request.form[''])
    # user_registration_data = request.form['first_name']
    # print(user_registration_data)
    return render_template('register.html')


@app.route("/menu_api")
def menu_api():
    resp = requests.get("http://www.ma-web.ir/maktab52/users.json")
    print(resp.json())
    userdict = {"users": resp.json()}
    return userdict
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/receipts")
def receipts():
    return render_template('receipts.html')


@app.route("/receipts_print")
def recepits_print():
    return render_template('recepits-print.html')


@app.route("/table")
def table():
    return render_template('table.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=8765)
