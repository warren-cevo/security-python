from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@127.0.0.1/snyk-test"
# initialize the app with the extension
db.init_app(app)

password = 'password';
secret = "secret";

aws_access_key_id="AKIAJWY3D3GJ6N4UTEST"
aws_secret_acces_key="CmeRfzYcE2lD1z8AeKkM1E4j9G4fW8o5H2xLTEST"

@app.route("/")
def hello_world():
    return "<p>Hellow, World!</p>"

@app.route("/db", methods=['GET'])
def testdb():
    args = request.args
    with db.engine.connect() as con:
        if args.get('id') is not None:
            rs = con.execute(text('SELECT * FROM users WHERE id=' + str(args.get('id'))))
        else:
            rs = con.execute(text('SELECT * FROM users'))

        for row in rs:
            print(row)

    return "db"

@app.route("/while")
def whileTest():
    while True:
        print("x")

    return "500"
