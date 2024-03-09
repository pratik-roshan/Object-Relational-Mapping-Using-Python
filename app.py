from DB import DB
from user import User

configs = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "sql@123",
    "database": "pythondb"
}

connection = DB.initialize(**configs)
print('Connection: ', connection)

# # Create
# user = User(None, 'Aleena', 'Shah', 'shahaleena@gmail.com')
# user.save_user()

# Get
user = User.get_user()
print(user)

users = User.get_all_users()
print(users)






# import psycopg2
# from psycopg2 import sql
# from DB import connect

# configs = {
#     "host": "localhost",
#     "port": 5432,
#     "user": "postgres",
#     "password": "sql@123",
#     "database": "pythondb"
# }

# conn = connect(configs)
# cur = conn.cursor()

# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(255) NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL
# )
# """

# cur.execute(create_users_table)
# conn.commit()

# # # ------------------------------------------INSERT DATA INTO DATABASE----------------------------------------------------------------------------
# # # Best Practice
# # insert_query = """
# # INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)
# # """
# # cur.execute(insert_query, ("Pranish", "Bhagat", "pranishbhagat@gmail.com"))
# # conn.commit()

# # # Alternative Approach using sql
# # insert_query = sql.SQL("""
# # INSERT INTO users (first_name, last_name, email) VALUES ({fname}, {lname}, {email})
# # """).format(fname=sql.Literal("Arpit"), lname=sql.Literal("Roshan Shah"), email=sql.Literal("arpitroshan01@gmail.com"))
# # cur.execute(insert_query)
# # conn.commit()

# # -------------------------------------Fetching Data From Database----------------------------------------------------------------------------
# select_query = """
# SELECT * FROM users
# """
# cur.execute(select_query)

# # fetchone(), fetchall()
# for row in cur.fetchall():
#     print(row)

# cur.close()

# conn.close()