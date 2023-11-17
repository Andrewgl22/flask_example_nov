from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.age = data['age']
        self.country = data['country']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"   
        results = connectToMySQL('userz').query_db(query)  

        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(username,email,age,country) VALUES (%(username)s,%(email)s,%(age)s,%(country)s)"
        return connectToMySQL('userz').query_db(query,data)  
    
    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        result = connectToMySQL('userz').query_db(query,data)
        return cls(result[0]) 
    
    @classmethod
    def edit_user(cls,data):
        query = "UPDATE users SET username=%(username)s,email=%(email)s, age=%(age)s,country=%(country)s WHERE id=%(id)s"
        return connectToMySQL('userz').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('userz').query_db(query,data)

    




    