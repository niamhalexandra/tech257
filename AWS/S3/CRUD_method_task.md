# Task using CRUD method with Python Boto3

1. Used 'sudo nano' to create individual python files for each step of task. 

2. Code to list S3 Buckets:
   
   ~~~ 
   import boto3
   #Create an S3 client
   s3 = boto3.client('s3')
   #List all S3 buckets
   response = s3.list_buckets()
   print("List of S3 Buckets:")
   for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
    ~~~

    