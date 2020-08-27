#Overview

### Deployment of Cloud Endpoint secured with API Keys and Bearer for reaching private Cloud Function, private Cloud Run and IAP protected App Engine.

Following Components are used.
* Cloud Functions: GET an Employee from Firestore using API Key.
* Cloud Run: Add an Employee into Firestore using Bearer Token.
* App Engine: DELETE an Employee from Firestore using Bearer Token.
* Cloud Endpoints ESPV2 Beta: Proxy service to control the requests.
* Firestore: Store Employee data.

![Architecture](https://github.com/vikramshinde12/endpoints-espv2/blob/master/Architecture.png)

The complete detail about this repo is available in the [please refer the blog](https://medium.com/@vikramshinde/secure-apis-in-cloud-run-cloud-functions-and-app-engine-using-cloud-endpoints-espv2-beta-b51b1c213aea)