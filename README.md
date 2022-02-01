Install xdotools

Add the below line to 'crontab -e'\
- */5 * * * * /home/pi/refresh.sh 2>&1 | /usr/bin/logger -t REFRESHSCRIPT

Copy everything to their folders and chmod +x refresh.sh