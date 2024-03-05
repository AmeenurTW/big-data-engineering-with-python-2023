!pip install mysql-connector-python #install mySQLที่เก็บดาต้า
sudo service mysql stop     # For systems using service
# or
sudo systemctl stop mysql   # For systems using systemctl

sudo mysqld_safe --skip-grant-tables &
