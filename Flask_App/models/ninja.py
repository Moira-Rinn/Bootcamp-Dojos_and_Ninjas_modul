from Flask_App.config.mysql_connection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls, query, data=None):
        ninjas_from_db = connectToMySQL(
            'Dojos_and_Ninjas').query_db(query, data)
        ninjas = []
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas

#     @classmethod
#     def save(cls, data=None):
#         query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
#         user_id = connectToMySQL('users_schema').query_db(query, data)
#         return user_id

#     @classmethod
#     def remove_user(cls, query, data=None):
#         user_id = connectToMySQL('users_schema').query_db(query, data)
#         return user_id

#     @classmethod
#     def edit_user(cls, query, data=None):
#         user_id = connectToMySQL('users_schema').query_db(query, data)
#         return user_id
