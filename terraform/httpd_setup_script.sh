#!/bin/bash
sudo yum update -y
sudo yum install -y httpd git
sudo systemctl start httpd
sudo systemctl enable httpd

cd /var/www/html
git clone -b main git@github.com:raghavvv29/natwest-assignment-repo.git temp-site
cp -r temp-site/* .
rm -rf temp-site
