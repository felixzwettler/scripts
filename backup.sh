#!/usr/bin/env bash
## backup.sh

# Directories to backup
BDIRS="/home /etc /var/lib /var/log /var/www /opt"

# Backing up using gzipped tar
tar -zcvf "/path/to/backup/backup.tgz" $BDIRS

# Restore with:
# tar -xzvf "/path/to/backup/backup.tgz"

