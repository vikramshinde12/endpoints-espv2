from flask import jsonify
from google.cloud import firestore


def get_emp(request):
    try:
        if request.args and 'employee_id' in request.args:
            employee_id = request.args.get('employee_id')
        else:
            return 'Precondition Failed', 412

        client = firestore.Client()
        doc_ref = client.collection(u'employee').document(u'{}'.format(employee_id))
        doc = doc_ref.get()
        if doc.to_dict():
            response = jsonify(doc.to_dict())
            response.status_code = 200
        else:
            response = jsonify({
                'httpResponseCode': '404',
                'errorMessage': 'Employee does not exist'
            })
            response.status_code = 404
        return response
    except Exception as e:
        return e
