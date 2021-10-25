URL of images:
Jupyter Notebook Image : https://hub.docker.com/r/ibmcom/jupyter-base-notebook-ppc64le
Apache Spark: https://hub.docker.com/r/bitnami/spark
Apache hadoop: https://hub.docker.com/r/bde2020/hadoop-namenode
               https://hub.docker.com/r/bde2020/hadoop-datanode
Sonarqube: https://hub.docker.com/_/sonarqube


Note:

0. I am using minikube(local k8s cluster) to finish the checkpoint one
 Ensure that you install k8s cli and minikube and docker before running these command

1. since these things are deployed on local, so they are complicated. I will deploy them to the cloud for the final step, then the user do not need to set them up

2. since they are deployed on local cluster, the processing time might be very long... it will be resolved after I move them to the cloud


Instruction:

For Jupyter Notebook Image and Apache Spark image, folliwng this instruction:
1. pull the images from dokcer hub
    docker pull ibmcom/jupyter-base-notebook-ppc64le
    docker pull bitnami/spark

For each image of above two images, follow the following steps to deploy it on Kubernetes:
2. open a new terminal tab

3. kubectl create deployment app-name --image=docker.io/image-name

4. kubectl expose deployment app-name --type=NodePort --port=default_port_number (each app is differ, listed in the following)
    jupyter-notebook:8888
    spark:8080

5. kubectl get services app-name

6. kubectl port-forward service/app-name local-port:default_port_number (do not stop it, I use it to connect to the container)


For Sonarqube and Sonarqube Scanner, follow this instruction:
1. pull the images from dokcer hub 
    docker pull sonarqube

2. open a new terminal tab

3. move to scanner folder

4. run "docker -t sonarqube_scanner ." to build a image

5. run folliwng command:
    kubectl create deployment kubectl create deployment sonarqube-app --image=docker.io/sonarqube_scanner

6. run following command:
    kubectl expose deployment sonarqube-app --type=NodePort --port=9000

7. run following command:  
    kubectl port-forward service/sonarqube-app 9000:9000 (do not stop it, I use it to connect to the container)

For Hadoop, follw this instruction:
1. pull the images from dokcer hub 
    docker pull bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    dokcer pull bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8

2. open a new terminal tab

3. run following command:
    kubectl create deployment hadoop-data-node --image=docker.io/hadoop-datanode:2.0.0-hadoop3.2.1-java8

4. run following command:
    kubectl expose deployment hadoop-data-node --type=NodePort --port=50075

5. run following command:(since I need to set a env variable so I need to use yaml to deploy it)
    kubectl apply -f hadoop-name-node-deployment.yaml

6. run following command:
    kubectl expose deployment hadoop-data-node --type=NodePort --port=8020

7. run following command:
    kubectl port-forward service/sonarqube-app 8020:8020 (do not stop it, I use it to connect to the container)

After setting up, you run "python app.py" to use the tool
