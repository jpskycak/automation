ssh -L 8001:localhost:8888 root@104.131.75.234

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip

sudo apt-get -y install ipython ipython-notebook
sudo -H pip install jupyter