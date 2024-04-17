# Containerising the Northwind Flask App

1. Go to terminal and clone the repo where the app is stored to your local machine.
2. Navigate to that file and create a 'requirements.txt' for all of the dependiencies needed to run the app and then a 'Dockerfile' to specify what's needed to run the app and including what ports to open (in this case 5000)
   
## Dockerfile

~~~
# parent image
FROM python:3.8
 
# Set a working directory in the container
WORKDIR /app
 
# Copy the current directory contents into the container at /app
COPY . .
 
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
 
# Make port 5000 available to everyone outside of this container
EXPOSE 5000
 
# Define environment variable
ENV FLASK_APP=northwind_web.py
 
# Run app.py when the container launches
CMD [ "waitress-serve", "--port=5000", "northwind_web:app"]
~~~

### requirements.txt file:
~~~
waitress==3.0.0
Flask==3.0.2
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.27
pymysql==1.1.0
Jinja2==3.1.3
Flask-Waitress==0.0.1
cffi
~~~

3. Use 'docker build -t' to build the image
4. then 'docker run' 
5. Test in browser with 'localhost:5000'
6. Docker commit the changes and push to Docker hub