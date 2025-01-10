import os 
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARENING").upper()

def get_logger():

    log = logging.Logger("marcelo", log_level)
    #ch logging.StreamHanler() # Console/terminal/stderr
    #ch setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        "meulog.log",
        maxBytes=300, # 10**6
        backupCount=10,
    )
    fh.setLevel(log_level)
    fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelName)s '
        '1:%(lineneno)d f:%(filename)s: %(message)s'
    )
    # ch setFormatter(fmt)
    fh.setFormatter(fmt)
    #log.addHandler(ch)
    log.addHandler(fh)