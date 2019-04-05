import os
from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config.from_object(os.environ['FLASK_ENV'])
app.config['SECRET_KEY'] = 'RwoMdfBrwk6IOuLJGk6CYQ=='
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(basedir, "feature_req.db"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import FeatureRequest


@app.route('/', methods=['GET'])
def get_all():
    req_data = request.get_json()
    if req_data and "client" in req_data:
        qr = FeatureRequest.query.filter(FeatureRequest.client == req_data['client']).order_by(
            FeatureRequest.client_priority).all()
    else:
        qr = FeatureRequest.query.order_by(FeatureRequest.client).order_by(FeatureRequest.client_priority).all()
    if not qr:
        return jsonify(json_list={})
    else:
        return jsonify(list=[i.serialize for i in qr])


@app.route('/new', methods=['POST'])
def new_fr():
    req_data = request.get_json()
    title = req_data.get('title', None)
    description = req_data.get('description', None)
    client = req_data.get('client', None)
    client_priority = req_data.get('client_priority', None)
    target_date = req_data.get('target_date', None)
    product_area = req_data.get('product_area', None)

    if not title or not description or not client:
        res = app.response_class(
            response=json.dumps({"message": "Title, description and client is required"}),
            status=406,
            mimetype='application/json'
        )
        return res

    qr = FeatureRequest.query.filter(FeatureRequest.client == client).filter(
        FeatureRequest.client_priority >= client_priority).order_by(FeatureRequest.client_priority).all()

    # change Client Priority if needes
    if qr:
        next_prio = client_priority + 1
        for i in qr:
            i.client_priority = next_prio
            next_prio += 1

    fr = FeatureRequest(title=title, description=description, client=client, client_priority=client_priority,
                        targe_date=target_date, product_area=product_area)
    db.session.add(fr)
    db.session.commit()

    response = app.response_class(
        response=json.dumps({"id": fr.id}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/delete', methods=['POST'])
def del_fr():
    try:
        db.session.query(FeatureRequest).get({'id': id}).delete()
        res = app.response_class(
            response=json.dumps({"message": "Delete success!"}),
            status=200,
            mimetype='application/json'
        )
    except:
        res = app.response_class(
            response=json.dumps({"message": "Error deleting FR"}),
            status=406,
            mimetype='application/json'
        )

    return res


if __name__ == '__main__':
    app.run()
