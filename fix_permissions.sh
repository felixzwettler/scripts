#!/bin/sh
chown -R pi:www-data .
find . -type f -exec chmod 664 {} \;
find ./bin -type f -exec chmod 775 {} \;
find . -type d -exec chmod 775 {} \;
find . -type d -exec chmod +s {} \;
