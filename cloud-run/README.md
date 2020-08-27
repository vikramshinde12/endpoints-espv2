1. Test the Docker image locally
```
docker build -t employee .
```

2. Run the Docker Container locally
```
docker run -e GOOGLE_APPLICATION_CREDENTIALS=/credentials/<filename>.json \
-v $PWD/credentials:/credentials \
-p 8080:8080 employee
```

3. Build a Docker image and push it to Container Registry.
```
gcloud builds submit --tag gcr.io/$PROJECT_ID/employee:v1 .
```

4. Deploy the container in Cloud Run
```
gcloud run deploy employee --no-allow-unauthenticated \
  --image gcr.io/$PROJECT_ID/employee:v1 \
  --region us-central1 --platform managed
```