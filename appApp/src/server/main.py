# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, make_response

from flask_cors import CORS

from firebase_admin import credentials, firestore, initialize_app
import json

import matching_algorithm
from matching_algorithm import Matching_Algorithm
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



cred = credentials.Certificate('keys.json')
default_app = initialize_app(cred)
db = firestore.client()
amotot_ref = db.collection('amotot')
request_ref = db.collection('requests')

@app.route('/allAssociations', methods=['GET'])
def allAssociations():
    associations = amotot_ref.get()
    assArr = []
    for aso in associations:
        assArr.append(aso.to_dict())
    return jsonify(assArr),200


@app.route('/getAssociations', methods=['GET'])
def getAssociations():
    # dates = request.json["dates"]
    dates = request.args.get("dates")
    dates = json.loads(dates)
    # return dates
    try:
        # Check if ID was passed to URL query
        if dates and len(dates) > 0:
            # docs = request_ref.stream().
            # for doc in docs :
            #     amotot.append(doc)
            records = [];
            for dat in dates:
                req =  amotot_ref.where(u'dates', 'array_contains', dat).get()
                if req:
                    for re in req:
                        if re.to_dict() not in records :
                            records.append(re.to_dict())

                # dail = json.loads(records)

            return jsonify(records), 200
        else:
            # all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return "saas", 400
    except Exception as e:
        return f"An Error Occured: {e}"
    return "" , 400

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


# TODO - return specific association by name
# def getAssociationsByName():
@app.route('/addReq', methods=['POST'])
def createRequest():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        for req in request.json:
            id = req['id']
            request_ref.document(id).set(req)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}", 400


@app.route('/getZivuog', methods=['GET'])
def zivug():
    listDat =[]
    req = request_ref.where(u"date" , "<=", '27.02.2022').where(u"date" , ">=" ,'17.02.2022').get()
    amotot= amotot_ref.get();
    valid = []
    for amo in amotot:
        amos = amo.to_dict()['dates']
        objAmo = amo.to_dict()
        for dat in amos:
            if dat <= '27.2.2022' and dat >= '17.2.2022':
                listDat =[];
                listDat.append(dat)
                valid.append({"name":objAmo['name'],"pepole_num":objAmo['pepole_num'],"dates":listDat})

    s = []
    for re in req:
        s.append(re.to_dict())
    result = matching_algorithm.Create_Matches(s,valid)
    print(result)
    return jsonify(result),200



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# @app.route('/add', methods=['POST'])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
