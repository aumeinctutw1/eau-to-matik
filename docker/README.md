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

## Create Grafana and InfluxDB containers
Create Grafana and InfluxDB container from `docker-compose.yaml` file:
```bash
sudo docker-compose up -d
```
### Grafana
- After creating the container, Grafana should be accessible under `http//<RPI-IP>`
- Default admin user for Grafana is `admin` with password `admin`
- Grafana data are stored in a Docker volume called `grafana_data`, which by default is located at `/var/lib/docker/volumes`

### InfluxDB
- InfluxDB Dashboard is accessible at `http://<RPI-IP>:8086`
- The login credentials are specified in `docker-compose.yaml` in `enviroment` variables.
- InfluxDB data are stored in `influxdb_data` volume 
- InfluxDB settings from `/etc/influxdb2` are stored in `influxdb_etc` volume