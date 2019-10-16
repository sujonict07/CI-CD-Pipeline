# Installing Docker on Centos7 server

### Pre-requisites
1. Centos-7 EC2 Instance

## Installation Steps

1. Install docker and start docker services
   ```sh 
   yum install docker -y
   docker --version 
   
   # start docker services
   service docker start
   service docker status
   ```
1. Create a user called dockeradmin
   ```sh
   useradd dockeradmin
   passwd dockeradmin
   ```
1. add a user to docker group to manage docker 
   ```
   usermod -aG docker dockeradmin
   ```

### Validation test

1. Pull hello-world image.
   ```sh
   sudo docker pull hello-world
   ```


2. Verify that docker is installed correctly by running the hello-world image.
   ```sh
   sudo docker run hello-world
   ```

# Installing Docker on Ubuntu 18.04 server
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
sudo echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu artful stable" >> /etc/apt/sources.list.d/docker.list
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt update
sudo apt install docker-ce
sudo docker -v
sudo apt install docker-compose
sudo docker-compose --version
```
