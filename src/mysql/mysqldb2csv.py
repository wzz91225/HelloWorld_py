# coding=utf-8

# ************************** BEGIN: import **************************
import csv
import mysql.connector
# ************************** END: import **************************



# ************************** BEGIN: parameter configuration **************************
# 是否输出每步操作结果
SHOW_RESULT = True

# 导出数据csv文件名前缀
output_csv_filename_pr = "data_"

# 数据库连接相关参数
MySQL_Database_host = "localhost"
MySQL_Database_user = ""        # 数据库用户名
MySQL_Database_password = ""    # 数据库密码

# 数据库读取相关参数
database_name = "project_gjs"       # 数据库名称
table_name = "patient"              # 表格名称
# ************************** END: parameter configuration **************************



# ************************** BEGIN: functions **************************
def connect_mysql_database(host, user, password):
    # connect to mysql database
    return mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
# ************************** END: functions **************************



if __name__ == "__main__":

    # ************************** BEGIN: connect mysql database **************************
    db = connect_mysql_database(
        MySQL_Database_host, 
        MySQL_Database_user, 
        MySQL_Database_password)

    if SHOW_RESULT:
        print("\nmysqldb:")
        print(db)
    # ************************** END: connect mysql database **************************



    # ************************** BEGIN: get data **************************
    cursor = db.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("SELECT * FROM " + table_name)

    data = [x for x in cursor]
    
    print("\n" + table_name + " data:")
    print("(id, name, sex, birth_year)")
    for x in data:
        print(x[0:3])
    # ************************** END: output data **************************


    
    # ************************** BEGIN: select data **************************
    id_arr = [x[0] for x in data]
    id_count = 0
    while id_count == 0:
        print("\n Please input id to output data:")
        getid = input()
        id_count = id_arr.count(int(getid))

    id_index = id_arr.index(int(getid))
    # str1 = data[id_index][4]
    # str2 = data[id_index][5]
    # str3 = data[id_index][6]

    # arr1 = [float(x) for x in data[id_index][4].split(',')]
    # arr2 = [float(x) for x in data[id_index][5].split(',')]
    # arr3 = [float(x) for x in data[id_index][6].split(',')]

    arr1 = data[id_index][4].split(',')
    arr2 = data[id_index][5].split(',')
    arr3 = data[id_index][6].split(',')
    # ************************** END: select data **************************



    # ************************** BEGIN: output data **************************
    with open(output_csv_filename_pr + getid + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile, lineterminator = "\n")     # lineterminator defaults to '\r\n'
        writer.writerow([getid, arr1[0], arr2[0], arr3[0]])
        for i in range(len(arr1) - 1):
            writer.writerow(['', arr1[i + 1], arr2[i + 1], arr3[i + 1]])
        csvfile.close()
    # ************************** END: output data **************************




    # close database
    db.close()
