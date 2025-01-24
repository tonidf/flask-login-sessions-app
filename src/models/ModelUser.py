from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self, db, user):

        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM user WHERE username = %s'
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()

            if row:
                id = row[0]
                username = row[1]
                password= User.check_password(row[2], user.password)
                fullname = row[3]

                user = User(id, username, password, fullname)
                return user
            else:
                return None

        except Exception as e:

            raise Exception(e)
