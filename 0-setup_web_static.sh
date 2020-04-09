#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n/" /etc/nginx/sites-avail\
able/default
sudo service ngnix start
