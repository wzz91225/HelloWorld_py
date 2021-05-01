# coding=utf-8

# ************************** BEGIN: import **************************
import csv
import mysql.connector
# ************************** END: import **************************



# ************************** BEGIN: parameter configuration **************************
# 是否输出每步操作结果
SHOW_RESULT = True

# 导入数据csv文件名
input_csv_filename = "94 bpm.csv"

# 导出数据csv文件名
output_csv_filename = "alldata.csv"

# 数据库连接相关参数
MySQL_Database_host = "localhost"
MySQL_Database_user = ""        # 数据库用户名
MySQL_Database_password = ""    # 数据库密码

# 数据库创建相关参数
drop_exist_database = False         # 是否删除已有同名数据库
database_name = "project_gjs"       # 数据库名称
drop_exist_table = False            # 是否删除已有同名表格
table_name = "patient"              # 表格名称
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

        csvfile.close()

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
        print("\narray - first and last number:")
        print(arr1[0], arr1[-1])
        print(arr2[0], arr2[-1])
        print(arr3[0], arr3[-1])
    # ************************** END: read data **************************



    # ************************** BEGIN: array to string **************************
    str1 = array2string(arr1)
    str2 = array2string(arr2)
    str3 = array2string(arr3)
    
    if SHOW_RESULT:
        print("\nstring:")
        print("len=", len(str1), ":", str1[:100])  
        print("len=", len(str2), ":", str2[:100])  
        print("len=", len(str3), ":", str3[:100])
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
            print("len=", len(x[4]), ":", x[4][:100])
            print("len=", len(x[5]), ":", x[5][:100])
            print("len=", len(x[6]), ":", x[6][:100])
    # ************************** END: insert data **************************



    # ************************** BEGIN: output data **************************
    cursor.execute("SELECT * FROM " + table_name)

    with open(output_csv_filename, "w") as csvfile:
        writer = csv.writer(csvfile, lineterminator = "\n")     # lineterminator defaults to '\r\n'
        writer.writerow(["id", "name", "sex", "birth_year", "datacolume1", "datacolume2", "datacolume3"])
        writer.writerows(cursor)
        
        csvfile.close()
    # ************************** END: output data **************************




    # close database
    db.close()
