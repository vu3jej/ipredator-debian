ipredator-debian
================

Python script to setup IPredator VPN on Debian-based systems. The script is based on the IPredator guide that describes setting up [OpenVPN on Debian Linux](https://www.ipredator.se/guide/openvpn/debian/native) using the Debian package system.

### Usage

##### The script needs to be run with superuser privileges
`sudo ./ipredator_client.py /home/hogwarts/Downloads/IPredator-CLI-Password.conf username password`
##### To specify an optional destination path, use the `-d` or `--destination` option

`sudo ./ipredator_client.py /home/hogwarts/Downloads/IPredator-CLI-Password.conf -d /home/hogwarts/test username password`

##### For help, run the script with `-h` or `--help` option

`./ipredator_client.py --help`

### Requirements

The script assumes that you have downloaded the `IPredator-CLI-Password.conf` file from [here](https://www.ipredator.se/guide/openvpn/debian/native#needed_files). The repo includes a copy of the file, but it might not be up to date.

### Todo

+ Extend the script to support other Linux distributions
+ Add pptp-client support(or is it broken and need not be supported?)
