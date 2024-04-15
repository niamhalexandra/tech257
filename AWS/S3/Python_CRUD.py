# LIST S3 BUCKETS

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

print("List of S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")

# CREATE BUCKET

import boto3

#name the bucket
bucket_name = 'tech257-niamh-test-boto3'

#specify region
region = 'eu-west-1'

#specify location constraint
location_constraint = 'EU'

#create s3 client
s3 = boto3.client('s3', region_name=region)

#create the new bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstr>
print(f"Bucket '{bucket_name}' created")

#UPLOAD FILE TO BUCKET
import boto3

#define which bucket
bucket_name = 'tech257-niamh-test-boto3'

# List of files to upload
files_to_upload = ['test.txt']

# Create an S3 client
s3 = boto3.client('s3')

# Upload each file to the bucket
for file_name in files_to_upload:
    with open(file_name, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, file_name)
    print(f"file '{file_name}' uploaded to '{bucket_name}'")

#DOWNLOAD FILES

import boto3

# specify bucket 
bucket_name = 'tech257-niamh-test-boto3'

# list of files to download
files_to_download = ['test.txt']

# Create an S3 client
s3 = boto3.client('s3')

# Download each file from the bucket
for file_name in files_to_download:
    s3.download_file(bucket_name, file_name, f"downloaded_{file_name}")
    print(f"file '{file_name}' downloaded")

#DELETE FILE FROM BUCKET

import boto3

#name of S3 bucket
bucket_name = 'tech257-niamh-test-boto3'

#specify file you want to delete
file_name = 'test.txt'

#create an S3 client
s3 = boto3.client('s3')

#delete the file from the bucket
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f"file '{file_name}' deleted from '{bucket_name}'")

#DELETE THE BUCKET

import boto3

#specify bucket
bucket_name = 'tech257-niamh-test-boto3'

#create an S3 client
s3 = boto3.client('s3')

#delete the specified bucket
s3.delete_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' deleted")

