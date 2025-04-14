import csv
import psycopg2

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "hello_122",
                        port = 5432)

cursor = conn.cursor()

# sql = "CREATE DATABASE phonebook"
# cursor.execute(sql)
# conn.commit()
# print("datebase created")

def create_table():
    sql = "CREATE TABLE users (ID SERIAL PRIMARY KEY, Name VARCHAR(50), Phone VARCHAR(20));"
    cursor.execute(sql)
    conn.commit()
    print("table created")

def insert_values(sql):

    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute(sql, row)
    conn.commit()
    print("data from csv file uploaded")

    y_n = input("Will you enter another phones? y/n: ")
    if y_n.lower() == 'y':
        number = int(input("Enter number of people that you will insert: "))
        for i in range(number):
            name = input("Enter name (Example: First_name Second_name): ")
            phone = input("Enter phone number (Example: +7(777)....): ")
            cursor.execute(sql, (name, phone))
        conn.commit()

def update_info():
    
    name = input("Enter the name whose info you want to change: ")
    field = input("What do you want to update? (name/phone): ").lower()
    enter = input("Enter the new value: ")

    if field in ['name', 'n']:
        sql = "UPDATE users SET Name = %s WHERE Name = %s;"
    elif field in ['phone', 'p']:
        sql = "UPDATE users SET Phone = %s WHERE Name = %s;"
    else:
        print("Invalid field")

    cursor.execute(sql, (enter, name))
    conn.commit()

def select_info():
    name = int(input("Enter name that you want to take info: "))
    sql = 'SELECT * FROM users WHERE Name = "%s";'
    cursor.execute(sql, (name,))
    results = cursor.fetchall()
    for row in results:
        print(row)

def delete_info():
    name = int(input("Enter name that you want to delete: "))
    sql = 'DELETE FROM users WHERE Name = "%s";'
    cursor.execute(sql, (name,))
    conn.commit()
    
create_table()

sql = "INSERT INTO users(Name, Phone) VALUES (%s, %s);"
insert_values(sql)

y_n = input("Will you update info? y/n: ")
if y_n.lower() == 'y':
    update_info()

select_info()

y_n = input("Will you delete info? y/n: ")
if y_n.lower() == 'y':
    delete_info()

cursor.close()
conn.close()
    

