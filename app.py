from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route("/menu")
def menu():
    return render_template('menu.html')


@app.route("/receipts")
def receipts():
    return render_template('Receipts.html')


@app.route("/receipts_print")
def recepits_print():
    return render_template('Recepits-print.html')


@app.route("/table")
def table():
    return render_template('table.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
