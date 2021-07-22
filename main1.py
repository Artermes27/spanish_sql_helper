import sqlite3
import random
import os.path

def executeSQL(db_name, sql):    
    try:
        db = sqlite3.connect(db_name)
        cursor = db.cursor()
        status = cursor.execute(sql)          
        db.commit()
        db.close()
    except sqlite3.Error as e:
        print(e)
        return False
    return True

def createDatabase(db_name):
    try:
        db = sqlite3.connect(db_name)
        db.close()
    except sqlite3.Error as e:
        print(e)
        return
    print("database formed")
    return db

def createTable(db_name):
    CARS_TABLE = "spanish"
    sql = "DROP TABLE " + CARS_TABLE
    status = executeSQL(db_name,sql)
    sql = "CREATE TABLE " + CARS_TABLE + " (id INTEGER PRIARY KEY ,spanish TEXT, english TEXT, type TEXT)"
    status = executeSQL(db_name,sql)
    if status == True:
        print(CARS_TABLE + " table creation successful")
    else:
        print(CARS_TABLE +  " table creation failed " + sql)

def all(DB_NAME, DB_TABLE):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()                           
    cursor.execute("SELECT * FROM " + DB_TABLE) 
    rows = cursor.fetchall()                       
    db.close()
    if rows:
        for row in rows:
            print(row)
    else:
       print("No rows found")
    input("press enter to continue...")

def insertData(db_name, DB_TABLE):
    f = open("num.txt", "r")
    num = f.read()
    f.close()
    spanish = str(input("enter the new spanish word:")) 
    english = str(input("enter the new english word:"))
    groop = str(input("enter the groop this word will become a part of:"))
    sql = "INSERT INTO " + DB_TABLE + " VALUES('" + str(num) + "','" + spanish + "','" + english + "','" + groop + "')"
    executeSQL(db_name,sql)
    final_num = int(num) + 1
    f = open("num.txt", "w")
    f.write(str(final_num))
    f.close()

def randomData(db_name, db_table):
    f = open("num.txt", "r")
    last = int(f.read())
    last = last - 1
    f.close()
    random_num = random.randint(0, last)
    command_spanish = "SELECT spanish FROM " + db_table + " WHERE id = " + str(random_num)
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()                           
    cursor.execute(command_spanish) 
    rows = cursor.fetchall()
    db.close()
    if rows:
        for row in rows:
            user_translation = input("what does " + str(row[0]) + " mean in spanish:")
    command_english = "SELECT english FROM " + db_table + " WHERE id = " + str(random_num)
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()                           
    cursor.execute(command_english) 
    rows = cursor.fetchall()
    db.close()
    if rows:
        for row in rows:
            if user_translation == str(row[0]):
                print("correct")
            else:
                print("incorect")
                print("the correct answer would be " + str(row[0]))
    input("press enter to continue...")

def custom_command(db_name):
    sql = input("Please enter your custome sql command: ")
    executeSQL(db_name,sql)
    
if __name__ == "__main__":

    DB_NAME = "dictionary"
    DB_TABLE = "spanish"

    if os.path.isfile('dictionary'):
        print("database found")
    else:
        createDatabase(DB_NAME)
        createTable(DB_NAME)

    if os.path.isfile('num.txt'):
        print("numbers found")
    else:
        file = open("num.txt", "w")
        file.close
        ile = open("num.txt", "w")
        file.write("1")
        file.close

    choice = 0
    while choice != 4:
        print("=== Database Menu ===")
        print("1 show all data")
        print("2 add Data")
        print("3 random Data")
        print("4 custom commands")
        print("5 Quit")
        choice = int(input("Please enter your choice : "))
        if choice == 1:
            all(DB_NAME, DB_TABLE)
        elif choice == 2:
            insertData(DB_NAME, DB_TABLE)
        elif choice == 3:
            randomData(DB_NAME, DB_TABLE)
        elif choice == 4:
            custom_command(DB_NAME)
        elif choice == 5:
            print("program ended")
