#!/bin/bash

sudo yum update -y
sudo yum install python3 -y
sudo yum install pip -y
sudo pip3 install flask
FOLDER="https://raw.githubusercontent.com/mseyitoglu/my_repository/master/001-roman-numerals-converter"

cd /home/ec2-user

wget ${FOLDER}/app.py
mkdir templates
cd templates
wget ${FOLDER}/templates/index.html
wget ${FOLDER}/templates/result.html
cd ..

python3 app.py