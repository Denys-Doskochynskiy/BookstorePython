
from src.main.classes.bookstore import Bookstore
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartBookstore(Bookstore, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(64), unique=False)
    _producer = db.Column(db.String(64), unique=False)
    _number_of_pages = db.Column(db.Integer, unique=False)
    _text_language = db.Column(db.String(32), unique=False)
    _new_condition = db.Column(db.Boolean, unique=False)
    _price_in_uah = db.Column(db.Float, unique=False)
    _connection_protocol = db.Column(db.String(32), unique=False)
    _data_transfer_amount = db.Column(db.Float, unique=False)

    def __init__(self, name="N/A", producer="N/A",
                 number_of_pages=0.0, text_language='N/A',
                 new_condition=False, price_in_uah=0.0,
                 connection_protocol='telnet', data_transfer_amount=0.0):
        super().__init__(name, producer,
                         number_of_pages, text_language,
                         new_condition, price_in_uah)
        self._connection_protocol = connection_protocol
        self._data_transfer_amount = data_transfer_amount


class SmartBookstoreSchema(ma.Schema):
    class Meta:
        fields = ('id','_name', '_producer',
                  '_number_of_pages', '_text_language', '_new_condition',
                  '_price_in_uah', '_connection_protocol',
                  '_data_transfer_amount')


smart_bookstore_schema = SmartBookstoreSchema()
smart_bookstores_schema = SmartBookstoreSchema(many=True)


@app.route("/smart_bookstore", methods=["POST"])
def add_smart_bookstore():

    name = request.json['name']
    producer = request.json['producer']
    number_of_pages = request.json['number_of_pages']
    text_language = request.json['text_language']
    new_condition = request.json['new_condition']
    price_in_uah = request.json['price_in_uah']
    connection_protocol = request.json['connection_protocol']
    data_transfer_amount = request.json['data_transfer_amount']
    smart_bookstore = SmartBookstore(name,
                                              producer,
                                              number_of_pages,
                                              text_language,
                                              new_condition,
                                              price_in_uah,
                                              connection_protocol,
                                              data_transfer_amount)
    db.session.add(smart_bookstore)
    db.session.commit()
    return smart_bookstore_schema.jsonify(smart_bookstore)


@app.route("/smart_bookstore", methods=["GET"])
def get_smart_bookstore():
    all_smart_bookstore = SmartBookstore.query.all()
    result = smart_bookstores_schema.dump(all_smart_bookstore)
    return jsonify({'smart_bookstores': result})


@app.route("/smart_bookstore/<id>", methods=["GET"])
def smart_bookstore_detail(id):
    smart_bookstore = SmartBookstore.query.get(id)
    if not smart_bookstore:
        abort(404)
    return smart_bookstore_schema.jsonify(smart_bookstore)


@app.route("/smart_bookstore/<id>", methods=["PUT"])
def smart_bookstore_update(id):
    smart_bookstore = SmartBookstore.query.get(id)
    if not smart_bookstore:
        abort(404)
    old_smart_bookstore = copy.deepcopy(smart_bookstore)
    smart_bookstore.name = request.json['name']
    smart_bookstore.producer = request.json['producer']
    smart_bookstore.number_of_pages = request.json['number_of_pages']
    smart_bookstore.text_language = request.json['text_language']
    smart_bookstore.new_condition = request.json['new_condition']
    smart_bookstore.price_in_uah = request.json['price_in_uah']
    smart_bookstore.connection_protocol = request.json['connection_protocol']
    smart_bookstore.data_transfer_amount = request.json['data_transfer_amount']
    db.session.commit()
    return smart_bookstore_schema.jsonify(old_smart_bookstore)


@app.route("/smart_bookstore/<id>", methods=["DELETE"])
def smart_bookstore_delete(id):
    smart_bookstore = SmartBookstore.query.get(id)
    if not smart_bookstore:
        abort(404)
    db.session.delete(smart_bookstore)
    db.session.commit()
    return smart_bookstore_schema.jsonify(smart_bookstore)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')

