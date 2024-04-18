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

2. Perform a create with the blow command specifying desired yaml file:
   ~~~
   kubectl create -f app_deployment.yml
   ~~~

3. Check the pods are there with:
   ~~~
   kubectl get pods
   ~~~

4. Check deployment:
   ~~~
   kubectl get deployment
   ~~~
![alt text](<Screenshot 2024-04-18 at 15.36.41.png>)


## Creating a service.yml file:

1. Create niginx_service.yml file, similar to the deployment.yml file, it should look like this:
   ~~~yml 
   apiVersion: v1
   kind: Service

  metadata:
    name: nginx-svc
    namespace: default # can name them in different namespaces within the same cluster
  spec:
  ports:
    - nodePort: 30001 # range is 30000-32768
      port: 80
      targetPort: 80
  selector:
    app: nginx # connects this service to the nginx deployment
  type: NodePort # type of service. Also use LoadBalancer - for local use cluster IP
  ~~~

2. Use the same commands as above to create etc. Check in browser:
![alt text](<Screenshot 2024-04-18 at 15.24.10.png>)

