from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

app.config.from_pyfile("config.py")
app.config.from_object('config.ProdConfig')

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(app.config["DATABASE_USERNAME"], app.config["DATABASE_PASSWORD"], app.config["DATABASE_HOSTNAME"], app.config["DATABASE_NAME"])
# initialize the app with the extension
db.init_app(app)

ANOTHER_DATABASE_PASSWORD="sk_test_kovrMB0mupFJXfNZWx6Etg5y"
AND_ANOTHER_DATABASE_PASSWORD="sk_live_454kjkj4545FD3434Srere7878"

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

        results_as_dict = rs.mappings().all()

    try:
        return "db" + results_as_dict[0].username
    except:
        return "db"

@app.route("/while")
def whileTest():
    while True:
        print("x")

    return "500"
