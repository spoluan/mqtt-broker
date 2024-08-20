#!/bin/bash
# maintainer: "SEVENDI ELDRIGE RIFKI POLUAN <sevendipoluan@gmail.com>"

# Install updates
echo "Install update ..."
apt-get update -y

# Install Docker
apt install docker.io dos2unix -y

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Run dos2unix on all *.sh files in subfolders
echo "Run dos2unix on all *.sh files in subfolders"
find . -type f -name "*.sh" -exec dos2unix {} \;

# Set permissions
chmod 777 -R *

echo "Done!"