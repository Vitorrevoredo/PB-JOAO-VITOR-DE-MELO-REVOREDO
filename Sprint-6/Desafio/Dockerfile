FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install boto3 pandas python-dotenv

CMD ["python", "upload_s3.py"]

