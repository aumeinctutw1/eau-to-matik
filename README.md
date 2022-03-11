# embedded3

## Install SMBUS and activate I2C

```bash
sudo raspi-config
```

Select "3 Interface Options" -> "I5 I2C" -> YES -> finish

```bash
sudo reboot
```

Check the connection of the device:
```bash
sudo i2cdetect -y 1
```

### If not already installed, install the smbus libraries

```bash
sudo apt update
sudo apt install python-smbus python3-smbus python-dev python3-dev i2c-tools
```