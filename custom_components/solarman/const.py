from datetime import timedelta

DOMAIN = 'solarman'

DEFAULT_PORT_INVERTER = 8899
DEFAULT_INVERTER_MB_SLAVEID = 1
DEFAULT_LOOKUP_FILE = 'deye_hybrid.yaml'
DEFAULT_DAYLIGHT_ONLY = False
LOOKUP_FILES = ['deye_4mppt.yaml', 'deye_hybrid.yaml', 'deye_string.yaml',  'sofar_lsw3.yaml', 'sofar_wifikit.yaml', 'solis_hybrid.yaml', 'solis_1p8k-5g.yaml', 'sofar_g3hyd.yaml' , 'sofar_hyd3k-6k.yaml', 'custom_parameters.yaml']

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

CONF_INVERTER_HOST = 'inverter_host'
CONF_INVERTER_PORT = 'inverter_port'
CONF_INVERTER_SERIAL = 'inverter_serial'
CONF_INVERTER_MB_SLAVEID = 'inverter_mb_slaveid'
CONF_LOOKUP_FILE = 'lookup_file'
CONF_DAYLIGHT_ONLY = 'daylight_only'

SENSOR_PREFIX = 'Solarman'
