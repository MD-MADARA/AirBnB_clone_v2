#!/usr/bin/env bash
#Set up web servers for the deployment of web_static

#Install Nginx if it not already installed
sudo apt update
sudo apt install nginx -y

#Create default nginx folder for the pages.
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/  #will contain current (symbolic link to test/)

#Server block
ServerBlock="server {
    listen 80;
    listen [::]:80 default_server;

    root /var/www/html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    add_header X-Served-By \$HOSTNAME;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

}"
#Nginx config file path
Config="/etc/nginx/sites-available/default"

#Create a fake HTML file to test Nginx configuration
Fake="<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>"
echo "$Fake" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
#If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group ( should be recursive).
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static.
echo "$ServerBlock" | sudo tee "$Config" > /dev/null

#Restart nginx server
sudo service nginx restart
