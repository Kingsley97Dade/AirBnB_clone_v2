#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static { alias /data/web_static/current/; }"

# Add or update alias in Nginx configuration
if grep -q "location /hbnb_static" "$nginx_config"; then
    sudo sed -i "s@location /hbnb_static.*@$nginx_alias@" "$nginx_config"
else
    sudo sed -i "/server {/a $nginx_alias" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0

