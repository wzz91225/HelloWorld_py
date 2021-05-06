# coding=utf-8

# ************************** BEGIN: import **************************
import csv
import mysql.connector
# ************************** END: import **************************



# ************************** BEGIN: parameter configuration **************************
# show every operation result(or not) 
SHOW_RESULT = True

# 导入csv文件名 input csv file name
input_csv_filename = "94 bpm.csv"

#  connect database to relevant parameter
MySQL_Database_host = "localhost"
MySQL_Database_user = ""        #  username
MySQL_Database_password = ""    #  password

# create relevant parameter into database
drop_exist_database = False         # delete existing database with same name(or not)
database_name = "project_gjs"       # name of database
drop_exist_table = True             # delete existing table with same name(or not)
table_name = "patient"              # name of the table
# ************************** END: parameter configuration **************************



# ************************** BEGIN: functions **************************
def read_data(input_csv_filename):
    arr1 = list()
    arr2 = list()
    arr3 = list()

    with open(input_csv_filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row.__len__() > 8:
                arr1.append(row[6])
                arr2.append(row[7])
                arr3.append(row[8])
    
        # reader = csv.DictReader(csvfile)
        # arr1 = [row[" gyroZ (rad/s)"] for row in reader]
        # arr2 = [row[" magX (碌T)"] for row in reader]    # useless
        # arr3 = [row[" magY (碌T)"] for row in reader]    # useless

    # delete title
    arr1.pop(0)
    arr2.pop(0)
    arr3.pop(0)

    return arr1, arr2, arr3



def array2string(arr):
    # str0 = str(arr)
    # str0 = str0.replace('[', '')
    # str0 = str0.replace(']', '')
    # str0 = str0.replace('\'', '')
    # str0 = str0.replace(' ', '')

    return str(arr).replace('[', '').replace(']', '').replace('\'', '').replace(' ', '')



def connect_mysql_database(host, user, password):
    # connect to mysql database
    return mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
# ************************** END: functions **************************



if __name__ == "__main__":

    # ************************** BEGIN: read data **************************
    [arr1, arr2, arr3] = read_data(input_csv_filename)

    if SHOW_RESULT:
        print("\narray:")
        print(arr1[0], arr1[-1])
        print(arr2[0], arr2[-1])
        print(arr3[0], arr3[-1])
    # ************************** END: read data **************************



    # ************************** BEGIN: array to string **************************
    str1 = array2string(arr1)  #Casting array to string
    str2 = array2string(arr2)
    str3 = array2string(arr3)
    
    if SHOW_RESULT:
        print("\nstring:")
        print(str1[:100])  
        print(str2[:100])  
        print(str3[:100])
    # ************************** END: array to string **************************



    # ************************** BEGIN: connect mysql database **************************
    db = connect_mysql_database(
        MySQL_Database_host, 
        MySQL_Database_user, 
        MySQL_Database_password)

    if SHOW_RESULT:
        print("\nmysqldb:")
        print(db)
    # ************************** END: connect mysql database **************************


    
    # ************************** BEGIN: create database **************************
    cursor = db.cursor()

    if drop_exist_database:
        cursor.execute("DROP DATABASE IF EXISTS " + database_name)
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)

    if SHOW_RESULT:
        cursor.execute("SHOW DATABASES")
        print("\nDatabases:")
        for x in cursor:
            print(x)
    # ************************** END: create database **************************
    


    # ************************** BEGIN: create table **************************
    cursor.execute("USE " + database_name)

    if drop_exist_table:
        cursor.execute("DROP TABLE IF EXISTS " + table_name)
    cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + """(
            `id` INT NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(30) DEFAULT NULL,
            `sex` VARCHAR(10) DEFAULT NULL,
            `birth_year` INT DEFAULT NULL,
            `datacolume1` MEDIUMTEXT DEFAULT NULL,
            `datacolume2` MEDIUMTEXT DEFAULT NULL,
            `datacolume3` MEDIUMTEXT DEFAULT NULL,
            PRIMARY KEY(`id`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8""")

    if SHOW_RESULT:
        cursor.execute("SHOW TABLE STATUS")
        print("\nTable Status:")
        for x in cursor:
            print(x)
        
        cursor.execute("DESC " + table_name)
        print("\n" + table_name + ":")
        for x in cursor:
            print(x)
    # ************************** END: create table **************************



    # ************************** BEGIN: insert data **************************
    sql = "INSERT INTO " + table_name + " (name, datacolume1, datacolume2, datacolume3) VALUES (%s, %s, %s, %s)"
    val = ("gjs", str1, str2, str3)
    cursor.execute(sql, val)
    db.commit()

    if SHOW_RESULT:
        print(cursor.rowcount, "was inserted.")

        cursor.execute("SELECT * FROM " + table_name)
        print("\n" + table_name + " data:")
        for x in cursor:
            print(x[0:3])
            print(x[4][:100])
            print(x[5][:100])
            print(x[6][:100])
    # ************************** END: insert data **************************


    # close database
    db.close()
