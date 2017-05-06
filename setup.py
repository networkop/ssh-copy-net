from setuptools import setup

setup(
    name = 'ssh-copy-net',
    description = 'ssh-copy-id for network devices',
    author = 'networkop',
    url='https://github.com/networkop/ssh-copy-net',
    author_email='mmkashin@gmail.com',
    version = '0.1',
    install_requires=['netmiko>=1.4.0'],
    scripts = ['bin/ssh-copy-net']
)
