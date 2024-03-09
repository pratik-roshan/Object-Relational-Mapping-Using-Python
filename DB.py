# import psycopg2
from psycopg2 import connect, extras

# def connect(config):
#     return psycopg2.connect(**config)

class DB:
    connection = None

    @staticmethod
    def initialize(**config):
        DB.connection = connect(**config)
        return DB.connection
    
    @staticmethod
    def get_cursor():
        return DB.connection.cursor(cursor_factory=extras.RealDictCursor)
    
    @staticmethod
    def commit():
        DB.connection.commit()

    @staticmethod
    def close():
        DB.connection.close()

    @staticmethod
    def rollback():
        DB.connection.rollback()

    @staticmethod
    def execute(query, values=None, single=False, multi=False):
        result = None
        try:
            cursor = DB.get_cursor()
            cursor.execute(query, values)
            DB.commit()
        
        except Exception as e:
            DB.rollback()
        
        else:
            if single:
                result = cursor.fetchone()
            if multi:
                result = cursor.fetchall()
        
        finally:
            cursor.close()
        return result