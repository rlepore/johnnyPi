JohnnyPi
========

Source code for Raspberry Pi Robot built from Linux User &amp; Developer issue #132

System Requirements
-------------------
Before installing any of the requirements found in our requirements file you must install the python dev tools library.  Since we are running the RaspberryPi on a Wheezy distro you will need to apt-get install the python dev tools as follows:

```unix
sudo apt-get install -y python-dev
```

Installation
------------
To install JohnnyPi follow the below steps:
#
1. Create a virtualenv for your environment
2. Activate your virtualenv
3. Install the johnnyPi requirements file. (You will need to choose the correct requirements file found in the requirements directory.)

```unix
virtualenv --no-site-packages .virtualenv/johnnyPi
source .virtualenv/johnnyPi/bin/activate
pip install -r requirements.txt
```
