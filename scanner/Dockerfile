FROM sonarqube
RUN apk update
RUN apk add unzip wget nodejs
RUN mkdir /downloads/sonarqube -p
RUN cd /downloads/sonarqube
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873-linux.zip
RUN unzip sonar-scanner-cli-4.2.0.1873-linux.zip
RUN mv sonar-scanner-4.2.0.1873-linux /opt/sonar-scanner
RUN export SONAR_HOST_URL='http://localhost:9001'
RUN export SONAR_LOGIN="admin"
