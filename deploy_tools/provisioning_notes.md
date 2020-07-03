Provisioning site baru
======================

## Package yang required:

* nginx
* Python 3.6
* virtualenv + pip
* Git

misal, di ubuntu:

    sudo apt-get install nginx git python3 python3.6-venv

## Config Virtual Host Nginx

* lihat nginx.template.conf
* ganti SITENAME dengan, misalnya, staging.nama-domainku.com

## Service systemd

* lihat gunicorn-systemd.template.service
* ganti SITENAME dengan, misalnya, staging.nama-domainku.com

## struktur folder:
Anggap kita punya akun user di /home/username

/home/username
    sites
        SITENAME
            database
            source
            static
            virtualenv
