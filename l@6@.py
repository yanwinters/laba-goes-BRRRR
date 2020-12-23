import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred", 'a')
    return connection

connection = create_connection("localhost", "root", "HarriHole{2018%)")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred", 's')

create_database_query="CREATE DATABASE students_db"
create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred", 'd')

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred", 'a')
    return connection

connection = create_connection("localhost", "root", "HarriHole{2018%)", "students_db")

create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT, 
    first_name TEXT NOT NULL, 
    second_name TEXT NOT NULL, 
  PRIMARY KEY (id)
    ) ENGINE=InnoDB
"""

execute_query(connection, create_students_table)

create_students = """
INSERT INTO
students (first_name, second_name) values 
                                            ('Андрей', 'Волков'),
                                            ('Григорий', 'Атанасян'),
                                            ('Павел', 'Стручков'),
                                            ('Александр', 'Первый'),
                                            ('Юрий', 'Долгорукий'),
                                            ('Иван', 'Грозненький'),
                                            ('Боналеон', 'Напопарт'),
                                            ('Тони', 'Срак'),
                                            ('Егор', 'Федорук'),
                                            ('Илма', 'Онск'),
                                            ('Василий', 'Автоматов'),
                                            ('Дмитрий', 'Играющий'),
                                            ('Николай', 'Ли'),
                                            ('Георгий', 'Лагунов'),
                                            ('R2', 'D2'),
                                            ('Тарасов', 'Никита');
"""
execute_query(connection, create_students)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred", 'f')

select_students = "SELECT*FROM students"
students = execute_read_query(connection, select_students)

for student in students:
    print(student)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Второй'
WHERE
    id = 4
"""
execute_read_query(connection, update_students_second_name)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Грозный'
WHERE
    id = 6
"""
execute_read_query(connection, update_students_second_name)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Бонапарт'
WHERE
    id = 7
"""
execute_read_query(connection, update_students_second_name)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Старк'
WHERE
    id = 8
"""
execute_read_query(connection, update_students_second_name)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Калашников'
WHERE
    id = 11
"""
execute_read_query(connection, update_students_second_name)

update_students_second_name = """
UPDATE
    students
SET
    second_name = 'Белоключевский'
WHERE
    id = 12
"""
execute_read_query(connection, update_students_second_name)

delete_students = "DELETE FROM students WHERE id = 9"
execute_query(connection, delete_students)




