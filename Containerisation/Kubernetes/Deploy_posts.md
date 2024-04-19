# Connecting the Database & running with k8s

1. Create a yaml for deploying the database, (see 'posts_deploy.yml')
2. Create a service yaml for the Database (see 'posts_service.yml')
3. Create an environmnet variable in the initial node app deploy yaml. In the value use the cluster IP of your database. It should look like this:
   ~~~yml
     env:
            - name: DB_HOST
              value: "mongodb://10.111.128.95:27017/posts"
   ~~~

4. Then run the 'kubectl create' to set up all pods. 
5. Navigate to the app /posts on browserto view!
   
   [alt text](<Screenshot 2024-04-19 at 12.31.33.png>)

## If the database doesn't seed:

1. run command in terminal:
   ~~~
   kubectl exec <pod-name> env node seeds/seed.js
   ~~~
2. You may have to run it for every pod on some occassions
