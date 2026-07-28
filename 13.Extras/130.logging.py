# --------------------------------------------------
#! ------------------ add logging ------------------
# --------------------------------------------------
# ? print out to console or file
# ? print logs of what happens
# --------------------------------------------------
# ? debug
# ? info
# ? warning
# ? error
# ? critical
# --------------------------------------------------
#! name => logging module give it to the default logger
# --------------------------------------------------
# todo# basic config
# ? level --> level of severity
# ? filename --> file name and extension
# ? mode --> mode of the file a => append
# ? format --> format for the log message
# --------------------------------------------------
# ? getlogger --> return a logger with the specified name


import logging

# print(dir(logging))

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="\n (%(asctime)s) --> 'adham is %(name)s' | %(levelname)s --> %(message)s",
    datefmt="%d - %B - %Y, %H:%M:%S",
)

# root
logging.critical("adham has critical")
logging.error("adham has error")
logging.warning("adham has warning")

my_logger = logging.getLogger("Adham")
# Adham
my_logger.critical("adham has critical")
my_logger.error("adham has error")
my_logger.warning("adham has warning")
