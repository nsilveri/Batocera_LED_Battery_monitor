import logging
import os
import time

# Creazione del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creazione dell'handler per scrivere su file
log_file = '/userdata/Battery_monitor/logs.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Definizione del formato del messaggio di log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Aggiunta dell'handler al logger
logger.addHandler(file_handler)

# Avvio dei due script
try:
    logger.info('Avvio Battery_monitor.py')
    os.system('python3 /userdata/Battery_monitor/Battery_monitor.py')
except Exception as e:
    logger.exception('Errore durante l\'avvio di Battery_monitor.py')

try:
    logger.info('Avvio OLED_info.py')
    os.system('python3 /userdata/Battery_monitor/OLED_info.py')
except Exception as e:
    logger.exception('Errore durante l\'avvio di OLED_info.py')
