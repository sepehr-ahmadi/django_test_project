from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
import requests
import psycopg2
import psycopg2.extras

import database_cafe

app = Flask(__name__, template_folder='templates')


###----------------main pages------------------------####

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


###---------------------user part------------------------######

@app.route('/user_list')
def user_list():
    list_users = database_cafe.read_user_database('*')
    return render_template("user_list.html", list_users=list_users)


@app.route('/user_register', methods=['POST', 'GET'])
def user_register():
    if request.method == 'POST':
        user_registration_data = request.form
        database_cafe.create_user_database(user_registration_data)
        return redirect(url_for('home'))
    return render_template('user_register.html')


@app.route('/user_update', methods=['POST', 'GET'])
def user_update():
    if request.method == 'POST':
        user_registration_data = request.form
        database_cafe.update_user_database(user_registration_data)
    return render_template('user_update.html')


@app.route('/user_delete', methods=['POST', 'GET'])
def user_delete():
    if request.method == 'POST':
        user_registration_data = request.form
        database_cafe.delete_user_database(user_registration_data)
    return render_template('user_delete.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_login_data = request.form
        print((database_cafe.read_user_database(user_login_data)))

        if database_cafe.read_user_database(user_login_data) != []:
            return redirect(url_for('customer_dashboard'))

    return render_template("login.html")


@app.route("/customer_dashboard")
def customer_dashboard():
    # return render_template("customer_dashboard.html",userdata=request.args.get('userdata'))
    return render_template("customer_dashboard.html", userdata=request.args.get('userdata'))


@app.route("/cashier_dashboard")
def cashier_dashboard():
    return render_template("cashier_dashboard.html")


###_________________________________menu part_______________________________###

@app.route("/menu_api")
def menu_api():
    resp = requests.get("http://www.ma-web.ir/maktab52/users.json")
    print(resp.json())
    userdict = {"users": resp.json()}
    return userdict


@app.route("/menu_register", methods=['POST', 'GET'])
def menu_register():
    if request.method == 'POST':
        menu_registration_data = request.form
        print(menu_registration_data)
        database_cafe.create_menu_item_database(menu_registration_data)
        # return redirect(url_for('home'))
    return render_template("menu_register.html")


@app.route("/menu_list", methods=['POST', 'GET'])
def menu_list():
    menu_list = database_cafe.read_menu_item_database('*')
    return render_template("menu_list.html", menu_list=menu_list)


@app.route('/menu_update', methods=['POST', 'GET'])
def menu_update():
    if request.method == 'POST':
        menu_registration_data = request.form
        print(menu_registration_data)
        database_cafe.update_menu_item_database(menu_registration_data)
    return render_template('menu_update.html')


@app.route('/menu_delete', methods=['POST', 'GET'])
def menu_delete():
    if request.method == 'POST':
        menu_registration_data = request.form
        database_cafe.delete_menu_item_database(menu_registration_data)
    return render_template('menu_delete.html')


###----------------------------orders part-------------------###
@app.route('/orders_create', methods=['POST', 'GET'])
def orders_create():
    order_list = database_cafe.read_menu_item_database('*')
    if request.method == 'POST':
        order_registration_data_table_number = request.form.getlist('table_number')
        order_registration_data_id = request.form.getlist('id')
        order_registration_data_number = request.form.getlist('number')
        for i in range(len(order_registration_data_id)):
            order_create_data = {}
            if order_registration_data_number[i] != None:
                order_create_data['status'] = 'on process'
                order_create_data['number'] = order_registration_data_number[i]
                order_create_data['menu_item_id'] = order_registration_data_id[i]
                order_create_data['table_id'] = int(order_registration_data_table_number[0])
                order_create_data['time_stamp'] = datetime.now()
                database_cafe.create_orders_database(order_create_data)
    return render_template('orders_create.html', order_list=order_list)


###----------------------------receipts part-----------------###
@app.route("/receipts", methods=['GET', 'POST'])
def receipts():
    if request.method == 'POST':
        receipts_data = database_cafe.read_receipts_database()

    return render_template('receipts_request.html')


@app.route("/receipts_print")
def receipts_print():
    return render_template('recepits-print.html')


####------------------------table part-----------------------------#####
@app.route('/table_register', methods=['POST', 'GET'])
def table_register():
    if request.method == 'POST':
        table_registration_data = request.form
        print(request.form)
        database_cafe.create_table_database(table_registration_data)
        # return redirect(url_for('cashier_dashboard'))
    return render_template('table_register.html')


@app.route("/table_list")
def table_list():
    table_list = database_cafe.read_table_database('*')
    return render_template("table_list.html", table_list=table_list)


@app.route('/table_update', methods=['POST', 'GET'])
def table_update():
    if request.method == 'POST':
        table_registration_data = request.form
        database_cafe.update_table_database(table_registration_data)
    return render_template('table_update.html')


@app.route('/table_delete', methods=['POST', 'GET'])
def table_delete():
    if request.method == 'POST':
        table_registration_data = request.form
        database_cafe.delete_table_database(table_registration_data)
    return render_template('table_delete.html')


if __name__ == '__main__':
    pass
