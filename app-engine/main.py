import os
from flask import Flask
from google.cloud import firestore

app = Flask(__name__)


@app.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    client = firestore.Client()
    doc_ref = client.collection(u'employee').document(u'{}'.format(employee_id))
    if not doc_ref.get().to_dict():
        return 'Not Found', 404
    else:
        doc_ref.delete()
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
