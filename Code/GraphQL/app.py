from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
from schema import schema
from config import configLogin

DATABASE, COMPANY, PASSWORD = configLogin()

client = connect(DATABASE, host=f'mongodb+srv://{COMPANY}:{PASSWORD}@cluster0.qk8pnen.mongodb.net/')

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(port=5002)
