#!/usr/bin/env python

'''
Author: Jithesh E J
E-mail: mail@jithe.sh
Created: 01/01/2015
Usage: sudo ipredator_client.py /source/path/filename -d /destination/path username password
    ipredator_client.py -h for help
    The script assumes you have already downloaded the configuration files 
    from https://www.ipredator.se/guide/openvpn/debian/native#needed_files & the configuration
    is based on https://www.ipredator.se/guide/openvpn/debian/native

The MIT License (MIT)

Copyright (c) [2015] [Jithesh Eriyakkadan Janardhanan]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import apt
import sys
import subprocess
import argparse
import shutil
import os.path

def configure_client():
    cache = apt.Cache()
    if cache['openvpn'].is_installed:
        # OpenVPN client is already installed! Let's not do anything and move out of the loop
        pass
    else:
        # Oopsie! OpenVPN client is not installed! Let's get on with it, shall we?
        try:
            subprocess.check_call(['apt-get', '--assume-yes', 'install', 'openvpn'])
        except subprocess.CalledProcessError as e:
            print 'Installation failed:', e

    parser = argparse.ArgumentParser(description = 'Accepting source & destination arguments from commandline')
    parser.add_argument('source', metavar = 'SOURCE_PATH', help = 'full path to ipredator conf file')
    parser.add_argument('-d', '--destination', metavar = 'DESTINATION_PATH: OPTIONAL', nargs = '?', default = '/etc/openvpn', help = 'Directory to copy the conf file to. defaults to /etc/openvpn')
    parser.add_argument('user', metavar = 'USERNAME', help = 'IPredator username')
    parser.add_argument('password', metavar = 'PASSWORD', help = 'IPredator password')
    args = parser.parse_args()

    # Copying the IPredator configuration file from source to destination

    try:
        shutil.copy(args.source, args.destination)
    except IOError as e:
        print e
    if os.path.isfile(args.destination + '/update-resolv-conf'):
        dns_conf = 'script-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf'
        with open(args.destination + '/IPredator-CLI-Password.conf', 'a') as confFile:
            confFile.writelines(dns_conf)
    else:
        sys.exit('update-resolv-conf does not exist!')
    
    # Creating /etc/openvpn/IPredator.auth file & appending credentials to it
    
    try:
        subprocess.check_call(['touch', '/etc/openvpn/IPredator.auth'])
    except subprocess.CalledProcessError as e:
        print e

    with open('/etc/openvpn/IPredator.auth', 'w') as authFile:
        authFile.write(args.user + '\n') 
        authFile.write(args.password)

    # Changing the ownership and permissions on files
    
    subprocess.call(['chown', 'root:root', '/etc/openvpn/IPredator-CLI-Password.conf'])
    subprocess.call(['chown', 'root:root', '/etc/openvpn/IPredator.auth'])
    subprocess.call(['chmod', '400', '/etc/openvpn/IPredator-CLI-Password.conf'])
    subprocess.call(['chmod', '400', '/etc/openvpn/IPredator.auth'])
    
if __name__ == '__main__':
    configure_client()
