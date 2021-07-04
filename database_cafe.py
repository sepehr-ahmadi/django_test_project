import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "masiandsepehr7368"

conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)


def create_user_database(userdata):
    cur = conn.cursor()
    cur.execute(
        """Insert into users(first_name,last_name,phone_number,birth_day,password_to_login,email) VALUES (%s, %s,%s,%s,%s,%s);""",
        (userdata['first_name'], userdata['last_name'], userdata['phone_number'],
         userdata['birthday'],
         userdata['password'], userdata['email']))
    conn.commit()
    cur.close()


def update_user_database(userdata):
    cur = conn.cursor()
    cur.execute(
        """UPDATE users SET "first_name" =%s,"last_name"=%s,"phone_number"=%s,"birth_day"=%s,"password_to_login"=%s,"email"=%s  WHERE phone_number =%s""",
        (userdata['first_name'], userdata['last_name'], userdata['phone_number'],
         userdata['birthday'],
         userdata['password'], userdata['email'], userdata['phone_number']))
    conn.commit()
    cur.close()


def delete_user_database(userdata):
    cur = conn.cursor()
    print(userdata["phone_number"])
    cur.execute("""DELETE FROM users WHERE "phone_number"=%s;""", (userdata['phone_number'],));
    conn.commit()
    cur.close()


def read_user_database(userdata):
    cur = conn.cursor()
    if userdata == "*":
        s = 'SELECT * FROM users'
        cur.execute(s)

    else:
        s = 'SELECT * From users where phone_number=%s'
        cur.execute(s, (userdata["phone_number"],))
    list_users = cur.fetchall()
    cur.close()
    return list_users


####table

def create_table_database(tabledata):
    cur = conn.cursor()
    cur.execute(
        """Insert into tables(table_number,cafe_space_position) VALUES ( %s,%s);""",
        (tabledata['table_number'], tabledata['cafe_space_position']))
    conn.commit()
    cur.close()


def update_table_database(tabledata):
    cur = conn.cursor()
    cur.execute(
        """UPDATE tables SET "table_number" =%s,"cafe_space_position"=%s WHERE table_number =%s""",
        (tabledata['table_number'], tabledata['cafe_space_position'], tabledata['table_number']))
    conn.commit()
    cur.close()


def delete_table_database(tabledata):
    cur = conn.cursor()
    cur.execute("""DELETE FROM tables WHERE "table_number"=%s;""", (tabledata['table_number'],));
    conn.commit()
    cur.close()


def read_table_database(tabledata):
    cur = conn.cursor()
    if tabledata == "*":
        s = 'SELECT * FROM tables'
        cur.execute(s)
    else:
        s = 'SELECT * From tables where phone_number=%s'
        cur.execute(s, (tabledata["table_number"],))
    list_tables = cur.fetchall()
    cur.close()
    return list_tables


# menu_item
def create_menu_item_database(menu_item_data):
    cur = conn.cursor()
    cur.execute(
        """Insert into menu_item(name,catagory,discount,delivering_time_period,estimated_cooking_time,price) VALUES (%s, %s,%s,%s,%s,%s);""",
        (menu_item_data['name'], menu_item_data['catagory'], menu_item_data['discount'],
         menu_item_data['delivering_time_period'],
         menu_item_data['estimated_cooking_time'], menu_item_data['price']))
    conn.commit()
    cur.close()


def update_menu_item_database(menu_item_data):
    cur = conn.cursor()
    cur.execute(
        """UPDATE menu_item SET "name" =%s,"catagory"=%s,"discount"=%s,"delivering_time_period"=%s,"estimated_cooking_time"=%s,"price"=%s  WHERE id =%s""",
        (menu_item_data['name'], menu_item_data['catagory'], menu_item_data['discount'],
         menu_item_data['delivering_time_period'],
         menu_item_data['estimated_cooking_time'], menu_item_data['price'], menu_item_data['id']))
    conn.commit()
    cur.close()


def delete_menu_item_database(menu_item_data):
    cur = conn.cursor()
    cur.execute("""DELETE FROM menu_item WHERE "id"=%s;""", (menu_item_data['id'],));
    conn.commit()
    cur.close()


def read_menu_item_database(menu_item_data):
    cur = conn.cursor()
    if menu_item_data == "*":
        s = 'SELECT * FROM menu_item'
        cur.execute(s)
    else:
        s = 'SELECT * From menu_item where name=%s'
        cur.execute(s, (menu_item_data["phone_number"],))
    list_users = cur.fetchall()
    cur.close()
    return list_users


###oredrs
def create_orders_database(orderdata):
    cur = conn.cursor()
    cur.execute(
        """Insert into orders(id,status,number,menu_item_id,table_id,time_stamp) VALUES (%s,%s,%s,%s,%s,%s);""",
        (orderdata['id'], orderdata['status'], orderdata['number'], orderdata['menu_item_id'],
         orderdata['table_id'],
         orderdata['time_stamp']))
    conn.commit()
    cur.close()


def update_orders_database(orderdata):
    cur = conn.cursor()
    cur.execute(
        """UPDATE orders SET "id=%s" "status" =%s,"number"=%s,"menu_item_id"=%s,"table_id"=%s,"time_stamp"=%s,  WHERE id =%s""",
        (orderdata['id'], orderdata['status'], orderdata['number'], orderdata['menu_item_id'],
         orderdata['table_id'],
         orderdata['time_stamp']))
    conn.commit()
    cur.close()


def delete_orders_database(orderdata):
    cur = conn.cursor()
    print(orderdata["id"])
    cur.execute("""DELETE FROM orders WHERE "id"=%s;""", (orderdata['id'],));
    conn.commit()
    cur.close()


def read_orders_database(orderdata):
    cur = conn.cursor()
    if orderdata['id'] == "*":
        s = 'SELECT * FROM orders'
    else:
        s = 'SELECT * From orders where id=%s'
    cur.execute(s, (orderdata["phone_number"],))
    list_order = cur.fetchall()
    cur.close()
    return list_order


##receipts
def create_receipts_database(receiptsdata):
    cur = conn.cursor()
    cur.execute(
        """Insert into receipts(id,user_id,orders_id,total_price,final_price,time_stamp) VALUES (%s, %s,%s,%s,%s,%s);""",
        (receiptsdata['id'], receiptsdata['user_id'], receiptsdata['orders_id'],
         receiptsdata['total_price'],
         receiptsdata['final_price'], receiptsdata['time_stamp']))
    conn.commit()
    cur.close()


def update_receipts_database(receiptsdata):
    cur = conn.cursor()
    cur.execute(
        """UPDATE receipts SET "id" =%s,"user_id"=%s,"orders_id"=%s,"total_price"=%s,"final_price"=%s,"time_stamp"=%s  WHERE id =%s""",
        (receiptsdata['id'], receiptsdata['user_ic'], receiptsdata['orders_id'],
         receiptsdata['total_price'],
         receiptsdata['final_price'], receiptsdata['time_stamp'], receiptsdata['id']))
    conn.commit()
    cur.close()


def delete_receipts_database(receiptsdata):
    cur = conn.cursor()
    cur.execute("""DELETE FROM receipts WHERE "id"=%s;""", (receiptsdata['id'],));
    conn.commit()
    cur.close()


def read_receipts_database(receiptsdata):
    cur = conn.cursor()
    if receiptsdata['id'] == "*":
        s = 'SELECT * FROM receipts'
    else:
        s = 'SELECT * From receipts where id=%s'
    cur.execute(s, (receiptsdata["id"],))
    list_receipts = cur.fetchall()
    cur.close()
    return list_receipts
