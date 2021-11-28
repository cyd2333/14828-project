URL of images:
Jupyter Notebook Image : https://hub.docker.com/r/jupyter/datascience-notebook
Apache Spark: https://hub.docker.com/r/bitnami/spark
Apache hadoop: https://hub.docker.com/r/bde2020/hadoop-namenode
               https://hub.docker.com/r/bde2020/hadoop-datanode
Sonarqube: https://hub.docker.com/_/sonarqube

video (upload to the box): https://cmu.box.com/s/7ua1yyeakzjf8g1l63yq40xnri5qpviv

Step of building up the project:

1. build up the images:
    In this project, I used five images in total. In the folliwng sections, i will introduce them 
    one by one in detail:

    1.1 main app:
    This is the image for the driver, which is used to print the URL based on user's input.
    In this image, i wrote a python program to read the user's input, and it will return a URL based 
    on user's input

    1.2 juypter notebook:
    This is a image for jupyter notebook. I built it based on the image that I found on docker hub.
    I added a command line to make the jupyter book not require the token

    1.3 Spark:
    For the spark image, I directly use the image that I found online

    1.4 Apache hadoop:
    for the hadoop image, I directly use the image that I found online

    1.5 Sonarqube:
    For the sonarqube scanner, I built based on the official Sonarqube image. I wrote some command line to 
    download and install the sonarqube scanner in the sonarqube. 

2. upload the images to the GCP's container registry:
    For each image, run following step to upload it to container registry:
    
    2.1 run "docker tag" to rename the docker image to be "docker_hub_id/image_name"
    2.2 run "docker push" to push the image to the docekr hub
    2.3 switch to GCP cloud shell
    2.4 run "docker pull" with specified docker image name to pull the docker image from docker hub
    2.5 run "docker tag" to rename the docker image to be "gcr.io/project_id/image_name"
    2.6 run "docker push" to push it to the cloud registry

    Note: 
    I attach a screenshot of cloud registry
    In the screenshot, 
    "hadoop-datanode" is the image for hadoop's datanode
    "hadoop-namenode" is the image for hadoop's namenode
    "juypter-notebook-no-token" is the image for the juypter notebook
    "main-app-new" is the image for the driver
    "sonarqube-scanner" is the image for the sonarqube scanner
    "spark-image" is the image for the spark

3. create a GKE cluster, named yingdongcluster

4. deploy the images to the GCP's kubernetes engine (GKE):

    for each image, we need to deploy them to the GKE. Since different images require different configuration, I
    will introduce them separately:

    4.1 main app:
    After deploy to the GKE, I manually set the "stdin" and "tty" to be true. The reason for this setting is to 
    ensure that the driver can interact with the user

    4.2 juypyter notebook:
    I simply deploy it to the GKE by clicking "deploy to GKE"

    4.3 spark:
    I simply deploy it to the GKE by clicking "deploy to GKE"

    4.4 hadoop namenode
    During the deployment of namenode, I add enviroment variable based on the instruction
    after deployment, I scale it to be one as the project required
    I take a screenshot of the environment variable that I set in the folder
    refer to : https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml
                https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env

    4.5 hadoop datanode
    During the deployment of datanode, I add enviroment variable based on the instruction
    after deployment, I scale it to be two as the project required
    I take a screen shot of the enviroment variable that I set in the folder
    refer to : https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env

    4.6 SonarQube
    I simply deploy it to the GKE by clicking "deploy to GKE"

    Note: 
    I attach a screenshot of apps that run on the GKE cluster (Screenshot_GKE_workload)
    In the screenshot,
    "datanode" is Hadoop's datanode app
    "juypter-notebook" is Juypter notebook's app
    "main-app-new" is drvier's app
    "namenode" is Hadoop's namenode app
    "nginx-2" is Spark's app
    "sonarqube-scanner" is Sonarqube's app

5. Create the service to expose the app to the external access

    Since each app's servie is different, i will introduce them one by one

    5.1 Hadoop namenode:
        it needs one port to communicate with datanode, and the one another port to allow user 
        to access its web interface
        I expose port 9000 for datanode communication, port 9870 for web interface

    5.2 Spark:
        It needs one port for user to access its web interface
        I expose port 8080 for web interface

    5.3  juypter-notebook:
        It needs one port for user to access its web interface
        I expose port 8888 for web interface
    
    5.4 sonarqube-scanner:
        it needs one port for user to access its web interface
        I expose port 9000 for web interface

    other: 
        since there is no web interface for driver and datanode, I did not expose port for them
    
    Note:
    I attach a screenshot of services of GKE cluster (Screenshot_GKE_services)
    In the screenshot:
        "jupyter-notebook-service" is service of juypter notebook app
        "namenode-service" is service of hadoop namenode app
        "nginx-2-service" is service of hadoop datanode app
        "sonarqube-scanner-4dtgr" is service of Sonarqube scanner app
    
6. use kebectl command to access the driver
    in order to access the k8s machine, we need to use a command with specified container name and pod name
    The following is the command that I used: 
        kubectl -n default attach main-app-new-698cd5b8c8-gv5sv -c main-app-new-1 -i -t
