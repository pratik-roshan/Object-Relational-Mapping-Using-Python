from DB import DB

configs = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "sql@123",
    "database": "pythondb"
}

class User:
    def __init__(self, id=None, first_name=None, last_name=None, email=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self) -> str:
        return f"User(first_name={self.first_name!r}, last_name={self.last_name!r}, email={self.email!r})"
    
    def save_user(self):
        insert_query = """INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"""
        DB.execute(insert_query, (self.first_name, self.last_name, self.email))

    def delete_user(self, id):
        pass

    def update_user(self, id, first_name, last_name):
        pass

    def get_user():
        query = """SELECT * FROM users"""
        data = DB.execute(query, single=True)
        print(data)
        return User(**data)
    
    def get_all_users():
        query = """SELECT * FROM users"""
        all_data = DB.execute(query, multi=True)
        return [User(**data) for data in all_data]



    # def save_user(self):
    #     with connect(configs) as conn:
    #         with conn.cursor() as cur:
    #             insert_query = """INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"""
    #             cur.execute(insert_query, (self.first_name, self.last_name, self.email))
    #         # conn.commit()
    #         # conn.close()

    # @staticmethod
    # def get_user():
    #     with connect(configs) as conn:
    #         with conn.cursor() as cur:
    #             select_query = """SELECT * FROM users"""
    #             cur.execute(select_query)
    #             data = cur.fetchone()
    #             return User(*data)

    # @staticmethod
    # def get_all_users():
    #     with connect(configs) as conn:
    #         with conn.cursor() as cur:
    #             select_query = """SELECT * FROM users"""
    #             cur.execute(select_query)
    #             all_data = cur.fetchall()
    #             return [User(*data) for data in all_data]