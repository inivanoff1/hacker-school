#!/bin/bash

cd ~

current_dt=$(date +"%a")
mysql_backup_dir="backup/mysql"
wp_backup_dir="backup/wp"

mkdir -p $mysql_backup_dir $wp_backup_dir

if [ $? -eq 0 ]; then
     sudo tar cvpf $wp_backup_dir/backup-wp-$current_dt.tar --keep-directory-symlink -C / etc/wordpress etc/apache2/sites-available/wordpress.conf srv/www/wp-content var/lib/wordpress/wp-content
     if [ $? -eq 0 ]; then
          wp_files=`sudo grep -l 'DB_NAME' /etc/wordpress/*`
          for file in $wp_files; do
               wp_db=`sudo cat $file | grep DB_NAME | cut -d \' -f 4`
               wp_user=`sudo cat $file | grep DB_USER | cut -d \' -f 4`
               wp_pass=`sudo cat $file | grep DB_PASSWORD | cut -d \' -f 4`
               sudo mysqldump -u$wp_user -p$wp_pass --databases $wp_db --single-transaction > $mysql_backup_dir/$wp_db-$current_dt.sql
          done
     else
          echo "Error creating an archive!"
     fi
else
     echo "Error creating directories!"
fi
