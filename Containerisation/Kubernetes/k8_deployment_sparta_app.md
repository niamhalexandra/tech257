# Using kubernetes to deploy Sparta App

1. Create a .yaml file to specify what needs creating, what ports to open etc. Ensure the indentation is correct, do NOT use tab, only use the spacebar, it should look like this:
~~~yml
   apiVersion: apps/v1 # which api to use for deployment
   kind: Deployment # pod - service, what kind of resource we are creating

metadata:
  name: nginx-deployment # name of the deployment
spec:
  selector: # which pods to manage with this deployment
    matchLabels:
      app: nginx
  replicas: 3 # number of pods to run
  template: # template for the pods
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: niamhalexandra/firstrepo:first # image to use
          ports:
            - containerPort: 80 # port to expose
~~~

