from flask import Flask
from flask import request
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def rest_get():
    return u"rest get"

@app.route('/<model_name>/<model_id>.xml', methods=['GET'])
def rest_foos_get_xml(model_name, model_id):
    return u"<foo><id>%s</id><name>%s</name></foo>" % (model_id, model_name)

@app.route('/foos.xml', methods=['GET'])
def rest_foos_get_xml_find_by():
    logging.error(request.args)
    return u'<foos type="array"><foo><id>123</id><name>bar</name></foo></foos>'

@app.route('/foos.json', methods=['GET'])
def rest_foos_get_json_find_by():
    #return u'[{"id":123,"name":"tanarky_get"},{"id":345,"name":"foobar"}]'
    return u'{"id":123,"name":"tanarky_get"}'

@app.route('/foos/1.json', methods=['GET'])
def rest_foos_get_json():
    return u'{"id":123,"name":"tanarky_get"}'

@app.route('/', methods=['POST'])
def rest_post():
    return u'{"id":123,"name":"tanarky_post"}'

@app.route('/foos/<model_id>.xml', methods=['PUT'])
def rest_put(model_id):
    logging.error(request.data)
    return u'{"id":123,"name":"tanarky_put"}'

@app.route('/', methods=['DELETE'])
def rest_delete():
    return u'{"id":123,"name":"tanarky_delete"}'

if __name__ == '__main__':
    app.run(debug=True, port=10080)
