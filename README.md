ipredator-debian
================

Python script to setup IPredator VPN on Debian-based systems. The script is based on the IPredator guide that describes setting up [OpenVPN on Debian Linux](https://www.ipredator.se/guide/openvpn/debian/native) using the Debian package system.

### Usage

#### You need to run this script with superuser privileges

    sudo ./ipredator_client.py /home/hogwarts/Downloads/IPredator-CLI-Password.conf username password

#### To specify a destination path, use the `-d` or `--destination` option

    sudo ./ipredator_client.py /home/hogwarts/Downloads/IPredator-CLI-Password.conf -d /home/hogwarts/test username password

#### For help, run the script with `-h` or `--help` option

    ./ipredator_client.py --help

### Requirements

The script assumes that you have downloaded the `IPredator-CLI-Password.conf` file from [here](https://www.ipredator.se/guide/openvpn/debian/native#needed_files)
