import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename="/var/www/rpi-apache-server/logs/rpi-apache-server.log", format="%(asctime)s %(message)s")
sys.path.insert(0, "/var/www/html/rpi-apache-server")
sys.path.insert(0, "/var/www/html/rpi-apache-server/.venv/lib/python3.8/site-packages")

from app import app as application