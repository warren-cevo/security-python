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

AWS_ACCESS_KEY_ID="AKIAJWY3D3GJ6N4UTEST"
AWS_SECRET_ACCESS_KEY="CmeRfzYcE2lD1z8AeKkM1E4j9G4fW8o5H2xLTEST"
PRIVATE_KEY="-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn\nNhAAAAAwEAAQAAAQEArPN99L/D9jXUwtFjoAzhnzA5a7t/YJiSrcTm+hKSxPp/nklfu1Km\ntDbMBOrXsAqLRcMz5JZoF8G1jebXOO3u2LRB+INFsxqDV76TZjUC1y4SAX17h5UvstT3sn\naPPt+TzwX3PmF8ooN+L8hDIZpvty6m+7b09QRFx4l7+j30MgO+kjwNHUyocn7qokoyH2p4\nfzvtoWePNyL191O9GNg6LmjneG25nN/NBoFYc/Zu+XfDY3gMECNurGHVV3W4ZNpoqjpZWU\nFx4eG0tShBZ+pvuFPy669+H8b5laNEjPGYclInW8unW6T9nuaoQjc/metBwaODgkOsAR0u\nddRxR8nIUwAAA9C2NMXdtjTF3QAAAAdzc2gtcnNhAAABAQCs8330v8P2NdTC0WOgDOGfMD\nlru39gmJKtxOb6EpLE+n+eSV+7Uqa0NswE6tewCotFwzPklmgXwbWN5tc47e7YtEH4g0Wz\nGoNXvpNmNQLXLhIBfXuHlS+y1Peydo8+35PPBfc+YXyig34vyEMhmm+3Lqb7tvT1BEXHiX\nv6PfQyA76SPA0dTKhyfuqiSjIfanh/O+2hZ483IvX3U70Y2DouaOd4bbmc380GgVhz9m75\nd8NjeAwQI26sYdVXdbhk2miqOllZQXHh4bS1KEFn6m+4U/Lrr34fxvmVo0SM8ZhyUidby6\ndbpP2e5qhCNz+Z60HBo4OCQ6wBHS511HFHychTAAAAAwEAAQAAAQEAl3IwnZ0+z96bjG0m\nvAQLngXwgjIRfFieOKPvTpPtCagBEG5X8gSSDcTeKoAqlvDkvBYO3uAGDqeFf9jgJe3T9N\ncD3cW1xvw0fyVWlW1eK2cgRUXIYhV1SzfKHvBKx1eoauRieLGNHhHe8aB/iHFf2hx0BH9V\nSSiQogX2Fk8iAphr9qLuR+M0eMtsZmq9nNpk0iXiohw7b3xNb1QrewoeiXiSI4xANdbkmx\n7R2Jnm132toa+ofPZWbpRptYyzv5TWRhEob4GQSknEvS7NEep3cxnv71d1wQvCfhkMKLXH\nKrIck4X46fLa+65OV8Bq37x91kRagOl4VFBZBT61Y9+DoQAAAIEAltUA8Zx5ETlUOXdGCQ\n+ftbCLZlmlPGGabFdg/EKM+M96Q3sj7L2lIP0Htt5w/HmM3Hz9uLk/d/m20zPq8xkltwCo\nF4R80K5HA38Q26fPRpJzDhch+k7AYuQwjziPSH1uzP3BdQo74KVuyvaTk+9VoeeFslF13P\njflhvUmCyquNkAAACBANtkmGdXwaMHrFKAibQreQuQD9CBRFRDRYNWOP4nPOp7YyCY4xbf\n02kHfFUmf7UqvY36v+jTC4RJ1mJH9KVlqJOB/JLhb6Wrv3xuddcxbwaMwb6dGgsZM+iB7G\nqBlcHlrxnWi6bXXK9WpQWaLNYdE4MKgRvKTSq20glezRWDijznAAAAgQDJzyCedgs5ibpb\nhvtNy5TGXPyX2lI9qoMDV2LSJZhp5TPL/mZqITUrehs0siM9IQ4DqhL4DgKBkYOLI/W6mW\nCXkQVFkGGLovzFUMM/wpK1Ua20k+0XakblI11yK3fjd0XJ0K5FyQ1YzG9XXZ8EuZo/2p2A\n8Y/K54JYuMflOJVftQAAABZoYW5uZXNAZGFrYXIuZGEuY3dpLm5sAQID\n-----END OPENSSH PRIVATE KEY-----\n"

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
