#!/bin/bash
# maintainer: "SEVENDI ELDRIGE RIFKI POLUAN <sevendipoluan@gmail.com>"

set -x  

echo "Stopping existing containers ..."
docker-compose down 

echo "Starting new containers ..."
docker-compose -f docker-compose.yml up -d

echo "Generating the pwfile ..."  

# Define the username and password
username="username"
password="your_pass"

# Create a file with the content "username:password"
echo "$username:$password" > mosquitto/config/pwfile

# Print a message to indicate that the file has been created
echo "File 'pwfile' created with content: $username:$password"
 
echo "Accessing the container and configuring MQTT ..."
docker exec -it mqtt-broker sh -c "cd mosquitto/config && mosquitto_passwd -U pwfile"

echo "Restarting the container ..."
docker restart mqtt-broker

echo "Done!"