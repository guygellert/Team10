# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify
from flask_cors import CORS

from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



cred = credentials.Certificate('keys.json')
default_app = initialize_app(cred)
db = firestore.client()
amotot_ref = db.collection('amotot')
request_ref = db.collection('amotot')
@app.route('/add', methods=['POST'])
def createDate

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json["id"]

        amotot_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/allAssocations')
# TODO - return All Associations From DB
# def getAssociations():
def getAssociations():
   return "Hello World"

# TODO - return specific association by name
# def getAssociationsByName():




@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# @app.route('/add', methods=['POST'])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
