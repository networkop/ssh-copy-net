# ssh-copy-net

[ssh-copy-id](https://linux.die.net/man/1/ssh-copy-id) equivalent for network devices, implemented using [Netmiko](https://github.com/ktbyers/netmiko).

## Requires

Netmiko >= 1.4.0

## Supports

* Cisco IOS-XE
* JUNOS (SRX, MX)
* Arista EOS
* Alcatel SROS
* Dell  Force10 OS9
* HP Comware 7
* Mellanox MLNX-OS

## Installation

`pip install git+https://github.com/networkop/ssh-copy-net.git`

## Usage

Enter device IP, vendor and admin credentials. Default behaviour is to install local user's public SSH key.

```bash
[null@null ~]$ ssh-copy-net 10.6.142.1 juniper
Username: admin
Password:
All Done!
```

Login the device without entering password:

```bash
[null@null ~]$ ssh 10.6.142.1
--- JUNOS 12.3X48-D30.7 built 2016-04-28 22:37:34 UTC
{primary:node0}
null@srx-1>
```
