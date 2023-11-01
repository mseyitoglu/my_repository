#!/bin/bash

yum update -y
yum install python3 -y
yum install pip -y
pip3 install flask
from Flask import Flask

FOLDER="https://raw.githubsercontent.com/mseyitoglu/my_repository/master/001-roman-numerals-converter"

cd /home/ec2-user

wget ${FOLDER}/app.py
mkdir templates
cd templates
wget ${FOLDER}/templates/index.html
wget ${FOLDER}/templates/result.html
cd ..

python3 app.py