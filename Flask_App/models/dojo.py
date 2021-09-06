from Flask_App.config.mysql_connection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, query, data=None):
        dojos_from_db = connectToMySQL(
            'Dojos_and_Ninjas').query_db(query, data)
        dojos = []
        for d in dojos_from_db:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def save(cls, data=None):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        dojo_id = connectToMySQL('Dojos_and_Ninjas').query_db(query, data)
        return dojo_id

#     @classmethod
#     def remove_user(cls, query, data=None):
#         user_id = connectToMySQL('users_schema').query_db(query, data)
#         return user_id

#     @classmethod
#     def edit_user(cls, query, data=None):
#         user_id = connectToMySQL('users_schema').query_db(query, data)
#         return user_id
