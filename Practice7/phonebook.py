import psycopg2
from config import load_config

import csv

def main():
    while True:
        print("\nPRESS [1] TO ADD CONTACT")
        print("PRESS [2] TO LIST CONTACTS")
        print("PRESS [3] TO SEARCH BY NAME")
        print("PRESS [4] TO SEARCH BY PREFIX PHONE")
        print("PRESS [5] TO UPDATE USERNAME")
        print("PRESS [6] TO UPDATE PHONE")
        print("PRESS [7] TO DELETE CONTACT BY ID")
        print("PRESS [8] TO DELETE CONTACT BY NAME")
        print("PRESS [9] TO DELETE CONTACT BY PHONE")
        print("PRESS [10] TO ADD FROM CSV")
        print("PRESS [0] TO EXIT")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            search_by_phone_prefix()
        elif choice == "5":
            update_username()
        elif choice == "6":
            update_phone()
        elif choice == "7":
            delete_by_id()
        elif choice == "8":
            delete_by_name()
        elif choice == "9":
            delete_by_phone()
        elif choice == "10":
            insert_from_csv("contacts.csv")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


def connect():
    config = load_config()
    return psycopg2.connect(**config)


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    sql = "INSERT INTO phonebook (username, phone) VALUES (%s, %s)"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (username, phone))
        conn.commit()

        print("Contact added successfully")

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def show_all_contacts():
    sql = "SELECT * FROM phonebook ORDER BY id"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql)
        rows = cur.fetchall()

        print("\n--- CONTACTS ---")
        for row in rows:
            print(f"ID: {row[0]}, Username: {row[1]}, phone: {row[2]}")

        cur.close() 
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def search_by_name():
    name = input("Enter name to search:")
    sql = "SELECT * FROM phonebook WHERE username ILIKE %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, ('%' + name + '%',))
        rows = cur.fetchall()
        
        print("\n--- CONTACTS ---")
        for row in rows:
            print(f"ID: {row[0]}, Username: {row[1]}, phone: {row[2]}")
        
        if not rows:
            print("Contact not found")
        
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def search_by_phone_prefix():
    prefix = input("Enter prefix to search:")
    sql = "SELECT * FROM phonebook WHERE phone LIKE %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (prefix + '%',))
        rows = cur.fetchall()
        
        print("\n--- CONTACTS ---")
        for row in rows:
            print(f"ID: {row[0]}, Username: {row[1]}, Phone: {row[2]}")
        
        if not rows:
            print("COntact not found")
        
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def update_username():
    id = input('Enter ID:')
    new_name = input('Enter new username:')

    sql = "UPDATE phonebook SET username = %s WHERE ID = %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (new_name, id))
        conn.commit()

        if cur.rowcount > 0:
            print("Username updated")
        else:
            print("Contact not found")
        
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def update_phone():
    id = input('Enter ID:')
    new_phone = input('Enter new phone:')

    sql = "UPDATE phonebook SET phone = %s WHERE ID = %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (new_phone, id))
        conn.commit()

        if cur.rowcount > 0:
            print("Phone updated")
        else:
            print("Contact not found")
        
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def delete_by_id():
    id = input("Enter ID: ")
    
    sql = "DELETE FROM phonebook WHERE ID = %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (id,))
        conn.commit()

        if cur.rowcount > 0:
            print("Contact deleted")
        else:
            print("Contact not found")
        
        conn.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def delete_by_name():
    name = input("Enter username: ")
    
    sql = "DELETE FROM phonebook WHERE username = %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (name,))
        conn.commit()

        if cur.rowcount > 0:
            print("Contact deleted")
        else:
            print("Contact not found")
        
        conn.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def delete_by_phone():
    phone = input("Enter phone: ")
    
    sql = "DELETE FROM phonebook WHERE phone = %s"

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(sql, (phone,))
        conn.commit()

        if cur.rowcount > 0:
            print("Contact deleted")
        else:
            print("Contact not found")
        
        conn.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def insert_from_csv(filename):
    sql = "INSERT INTO phonebook (username, phone) VALUES(%s, %s)"

    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            username = row[0]
            phone = row[1]

            try:
                cur.execute(sql, (username, phone))
            except:
                print("Skipped:", row)

    conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()