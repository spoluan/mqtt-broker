#!/bin/bash
# maintainer: "SEVENDI ELDRIGE RIFKI POLUAN <sevendipoluan@gmail.com>"

set -x  

echo "Stopping existing containers ..."
docker-compose down
echo "Done!"