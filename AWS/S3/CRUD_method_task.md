# Task using CRUD method with Python Boto3

1. Used 'sudo nano' to create individual python files for each step of task. 

2. Code to list S3 Buckets:
   
   ~~~python
   import boto3
   #Create an S3 client
   s3 = boto3.client('s3')
   #List all S3 buckets
   response = s3.list_buckets()
   print("List of S3 Buckets:")
   for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
    ~~~

3. Code to create new Bucket:
   
   ~~~python
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
   s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': location_constraint})
   print(f"Bucket '{bucket_name}' created")
   ~~~

4. Code to upload a file:
   
   ~~~python
   import boto3
   #define which bucket
   bucket_name = 'tech257-niamh-test-boto3'
   #list of files to upload
   files_to_upload = ['test.txt']
   #Create an S3 client
   s3 = boto3.client('s3')
   #Upload each file to the bucket
   for file_name in files_to_upload:
    with open(file_name, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, file_name)
    print(f"file '{file_name}' uploaded to '{bucket_name}'")
   ~~~
   
5. Code to delete file from a bucket:
   
   ~~~python
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
   ~~~

6. Code to delete the bucket:
   
   ~~~python
   import boto3
   #specify bucket
   bucket_name = 'tech257-niamh-test-boto3'
   #create an S3 client
   s3 = boto3.client('s3')
   #delete the specified bucket
   s3.delete_bucket(Bucket=bucket_name)
   print(f"Bucket '{bucket_name}' deleted")
   ~~~