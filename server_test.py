import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# server.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
# server.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
# server.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
# server.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
# server.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')

server.config['MYSQL_HOST'] = 'localhost'
server.config['MYSQL_USER'] = 'auth_user'
server.config['MYSQL_PASSWORD'] = 'auth123'
server.config['MYSQL_DB'] = 'auth'
server.config['MYSQL_PORT'] = 3306


@server.route('/test_route', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return "Missing credentials", 401
    
    cur = mysql.connection.cursor()
    res = cur.execute(
        f"SELECT e_mail, password FROM user WHERE e_mail ='{auth.username}';"
    )
    if res > 0:
        user_row = cur.fetchone()
        e_mail = user_row[0]
        password = user_row[1]
        if auth.username != e_mail or auth.password != password:
            return "Invalid credentials", 401
        else:
            # return 'Fuck yeah'
        return createJWT(auth.username, 'kupa', True)

    else:
        return "Invalid credentials", 401

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)