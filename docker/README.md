# Docker containers
## Install Docker-engine and Docker-compose
Add executable permissions to `install_docker.sh` Bash script:
```bash
chmod +x install_docker.sh
```

Execute the installation script:
```bash
./install_docker.sh
```

## Create Grafana container
Create Grafana container from `docker-compose.yaml` file:
```bash
docker-compose up -d
```

After creating the container, Grafana should be accessible under `http//<RPI-IP>`.
Default admin user for Grafana is `admin` with password `admin`

Grafana data are stored in a Docker volume called `data`, which by default is located at `/var/lib/docker/volumes`.