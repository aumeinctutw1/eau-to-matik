# embedded3

# Install SMBUS and activate I2C

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
