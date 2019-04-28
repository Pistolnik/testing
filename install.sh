#/bin/bash

sudo apt update

sudo apt install -y python3-pip

sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install -y  ansible
sudo apt install -y git-core
