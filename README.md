# Subnet Calculator

This is a subnet calculator application written in Python. It calculates the details of each subnet in a main network, including the subnet ID, mask, first and last IP addresses, and broadcast address.

## Installation
Before running the application, make sure you have Python 3.7 or higher installed. This CLI app is made using `typer`, which you will need to install:

```bash
pip install typer
```

## Running the Application
You can run the application from the command line with the following format:

```bash 
python subnet_calc.py network_ip_in_CIDR subnet1=count subnet2=count ....
```

Example:

```bash
python .\subnet_calc.py 190.12.40.0/23 A=125 B=90 C=60 D=50 E=28 L1=1 L2=1 L3=1
```

Output:

```bash
IP=190.12.40.0/23
---------
Subnet Name: A
Subnet ID: 190.12.40.0/25
Mask: 255.255.255.128
First IP: 190.12.40.1
Last IP: 190.12.40.126
Broadcast: 190.12.40.127

Subnet Name: B
Subnet ID: 190.12.40.128/25
Mask: 255.255.255.128
First IP: 190.12.40.129
Last IP: 190.12.40.254
Broadcast: 190.12.40.255

Subnet Name: C
Subnet ID: 190.12.41.0/26
Mask: 255.255.255.192
First IP: 190.12.41.1
Last IP: 190.12.41.62
Broadcast: 190.12.41.63

Subnet Name: D
Subnet ID: 190.12.41.64/26
Mask: 255.255.255.192
First IP: 190.12.41.65
Last IP: 190.12.41.126
Broadcast: 190.12.41.127

Subnet Name: E
Subnet ID: 190.12.41.128/27
Mask: 255.255.255.224
First IP: 190.12.41.129
Last IP: 190.12.41.158
Broadcast: 190.12.41.159

Subnet Name: L1
Subnet ID: 190.12.41.160/30
Mask: 255.255.255.252
First IP: 190.12.41.161
Last IP: 190.12.41.162
Broadcast: 190.12.41.163

Subnet Name: L2
Subnet ID: 190.12.41.164/30
Mask: 255.255.255.252
First IP: 190.12.41.165
Last IP: 190.12.41.166
Broadcast: 190.12.41.167

Subnet Name: L3
Subnet ID: 190.12.41.168/30
Mask: 255.255.255.252
First IP: 190.12.41.169
Last IP: 190.12.41.170
Broadcast: 190.12.41.171
```

