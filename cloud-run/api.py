import os
from flask import Flask, request
from google.cloud import firestore

app = Flask(__name__)


@app.route('/employee', methods=['POST', 'PUT'])
def add_update_employee():
    json_ = request.get_json()
    if 'id' not in json_:
        return 'Precondition Failed', 412

    client = firestore.Client()
    doc_ref = client.collection(u'employee').document(u'{}'.format(json_.get('id')))
    doc_ref.set(json_)
    return 'Created', 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))