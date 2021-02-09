# scripts
scripts, little programs, etc.

## backup.sh
server backup script ( which contains only a tar command, really sophisticated I know! ).

## git_clean_commit_hist.sh
delete the commit history of your git repository.

## fix_permissions.sh
Fixing permissions for the current directory.

## pishrink.sh
create shrinked raspberry pi msd-card images.

fork of https://github.com/Drewsif/PiShrink  

## zeit-download.py
fetching the latest ZEIT-Issue from the zeit.de website using the requests and beautifulsoup module.
Note: openSSL TLS 1.1 support must be enabled, otherwise the requests module will fail. This is **NOT** the default in Debian 10.

In the script the variables `username`, `password` and `downloadpath` for the download path must be changed accordingly. Of course, you will need a subscription to ZEIT digital.

The script can be executed periodically, for example with `crontab`. To do this, execute the command `crontab -e` and add this line to make a daily fetch at 3am:

    0 0 */3 * * python3 /path/to/script/zeit-download.py >/dev/null 2>&1
