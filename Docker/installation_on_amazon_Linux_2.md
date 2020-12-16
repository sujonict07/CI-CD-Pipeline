To install Docker on an Amazon EC2 instance

1. Update the installed packages and package cache on your instance.
```
sudo yum update -y
```

2. Install the most recent Docker Engine package.
```
sudo amazon-linux-extras install docker
```

3. Start the Docker service.

```
sudo service docker start
```

4. Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
```
sudo usermod -a -G docker ec2-user
```

5. Log out and log back in again to pick up the new docker group permissions. 
You can accomplish this by closing your current SSH terminal window and reconnecting to your instance in a new one. 
Your new SSH session will have the appropriate docker group permissions.

6. Verify that the ec2-user can run Docker commands without sudo.
```
docker info
```
7. Make docker auto-start
```
sudo chkconfig docker on
```

Because you always need it....
```
sudo yum install -y git
```
Reboot to verify it all loads fine on its own.
```
sudo reboot
```

### docker-compose install

Copy the appropriate docker-compose binary from GitHub:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
```
NOTE: to get the latest version (thanks @spodnet): 
```
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
```
Fix permissions after download:
```
sudo chmod +x /usr/local/bin/docker-compose
```
Verify success:

```
docker-compose version
```
