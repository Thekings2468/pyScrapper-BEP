from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

dbc = create_engine('sqlite:///db.sqlite3')
app = Flask(__name__, static_url_path='')
api = Api(app)

class Jobs(Resource):
    def get(self):
        conn = dbc.connect()
        query = conn.execute("SELECT * FROM empregos")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchJobType(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE tipo_oferta LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchContractType(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE vinculo LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchCareer(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE carreira LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchCategory(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE categoria LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchDistrict(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE distrito LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchOrg(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE organismo LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchSkills(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE habilitacoes LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SearchExpire(Resource):
    def get(self, q):
        conn = dbc.connect()
        q = '%' + q + '%'
        query = conn.execute('SELECT * FROM empregos WHERE data_limite LIKE (?)', (q))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Jobs, '/jobs')
api.add_resource(SearchJobType, '/search/type/<q>')
api.add_resource(SearchContractType, '/search/contract/<q>')
api.add_resource(SearchCareer, '/search/career/<q>')
api.add_resource(SearchCategory, '/search/category/<q>')
api.add_resource(SearchDistrict, '/search/district/<q>')
api.add_resource(SearchOrg, '/search/org/<q>')
api.add_resource(SearchSkills, '/search/skills/<q>')
api.add_resource(SearchExpire, '/search/expire/<q>')

if __name__ == '__main__':
    app.run(port='5002')