echo hi
dnf install nginx -y
nano /etc/nginx/conf.d/status.conf
nano /etc/nginx/nginx.conf
systemctl stop firewalld
systemctl start nginx
wget https://github.com/nginxinc/nginx-prometheus-exporter/releases/download/v1.1.0/nginx-prometheus-exporter_1.1.0_linux_amd64.tar.gz
tar -xzvf nginx-prometheus-exporter_1.1.0_linux_amd64.tar.gz
mv nginx-prometheus-exporter /usr/local/bin/
useradd -rs /bin/false nginx-prometheus-exporter
sudo chmod +x /usr/local/bin/nginx-prometheus-exporter
sudo chown nginx-prometheus-exporter:nginx-prometheus-exporter /usr/local/bin/nginx-prometheus-exporter
nano /etc/systemd/system/nginx-prometheus-exporter.service
systemctl daemon-reload
systemctl enable nginx-prometheus-exporter
systemctl start nginx-prometheus-exporter
systemctl status nginx-prometheus-exporter
systemctl restart nginx-prometheus-exporter
systemctl status nginx-prometheus-exporter
ls /usr/local/bin/nginx-prometheus-exporter
which nginx-prometheus-exporter
ExecStart=/path/to/nginx-prometheus-exporter -nginx.scrape-uri=http://localhost:80/nginx_status
sudo nano /etc/systemd/system/nginx-prometheus-exporter.service
id nginx-prometheus-exporter
sudo chown nginx-prometheus-exporter:nginx-prometheus-exporter /usr/local/bin/nginx-prometheus-exporter
sudo chmod 750 /usr/local/bin/nginx-prometheus-exporter
sudo systemctl daemon-reload
sudo systemctl restart nginx-prometheus-exporter
sudo systemctl status nginx-prometheus-exporter
wget https://dl.influxdata.com/telegraf/releases/telegraf-1.30.0-1.x86_64.rpm
yum localinstall telegraf-1.30.0-1.x86_64.rpm
nano /etc/telegraf/telegraf.conf
systemctl start telegraf
systemctl enable telegraf
systemctl status telegraf
ip a
