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

# Tylko do szybkich testów
server.config['MYSQL_HOST'] = 'localhost'
server.config['MYSQL_USER'] = 'auth_user'
server.config['MYSQL_PASSWORD'] = 'auth123'
server.config['MYSQL_DB'] = 'auth'
server.config['MYSQL_PORT'] = 3306


@server.route('/login', methods=['POST'])
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
            # Simplified for testing
            return createJWT(auth.username, 'secret', True)
            # return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)

    else:
        return "Invalid credentials", 401


@server.route('/validate', methods=['POST'])
def validate():
    encoded_jwt = request.headers['Authorization']
    if not encoded_jwt:
        return "Missing credentials", 401
    # One needs to check for the type of the authentication
    encoded_jwt = encoded_jwt.split(' ')[1]

    try:
        # Simplified for testing
        decoded_jwt = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
        # decoded_jwt = jwt.decode(encoded_jwt, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
    except:
        # Delete these line. For testing only
        print('Something went wrong at /validate route')
        print(encoded_jwt)
        return "Not authorized", 403
    return decoded_jwt, 200


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz
        },
        secret,
        algorithm = "HS256"
    )

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)