#!/bin/bash

# Update Apt-Repo and install requirments for repository usage over HTTPS
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker official GPG key
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker stable Repository to apt-sourcelist
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update Apt-Repo and install Docker-Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Install Python and Docker-Compose
sudo apt install -y libffi-dev libssl-dev python3-dev python3 python3-pip
pip3 install docker-compose

# Add current user to "docker" group
sudo usermod -aG docker $USER