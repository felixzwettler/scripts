#!/usr/bin/env bash
## backup script

BACKUPTIME=$(date +%Y-%m-%d_%H-%M-%S)

# Directories to backup
BACKUPSOURCES="/home /etc /opt/ /var/www"

BACKUPDEST="/media/cloud/Systeme/fz-cloud/backups/backup-$BACKUPTIME.tar.gz"

# Backing up using gzipped tar
tar -cpzf $BACKUPDEST $BACKUPSOURCES
chmod pi:pi $BACKUPDEST

# Restore with for example:
# tar -xpzf "/media/cloud/Systeme/fz-cloud/backup-2020-01-01_03-00-00.tgz"
