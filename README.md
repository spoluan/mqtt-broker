# MQTT Broker Setup with Docker Compose

This repository provides a complete setup for running an MQTT broker using Docker and Docker Compose. It includes scripts to automate the setup, start, and stop processes, as well as configuration files to customize the broker.

## Contents

- `docker-compose.yml`: Defines the services and configurations for the MQTT broker using Docker Compose.
- `mosquitto.conf`: Configuration file for customizing the MQTT broker settings.
- `setup.sh`: Script to install Docker and Docker Compose on your system.
- `run.sh`: Script to start the MQTT broker using Docker Compose and set up the username and password.
- `stop.sh`: Script to stop the running Docker containers.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone git@github.com:spoluan/mqtt-broker.git
    cd your-repo-name
    ```

2. Run the setup script to install Docker and Docker Compose:
    ```bash
    ./setup.sh
    ```

## Usage

1. To start the MQTT broker and set up the username and password, run:
    ```bash
    ./run.sh
    ```

2. To stop the MQTT broker, run:
    ```bash
    ./stop.sh
    ```

## Configuration

- The `mosquitto.conf` file is used to customize the MQTT broker's configuration. Modify this file as needed before running the `run.sh` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
