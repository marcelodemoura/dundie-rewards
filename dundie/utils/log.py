import os 
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelName)s '
        '1:%(lineneno)d f:%(filename)s: %(message)s'
)

def get_logger(logfile="dundie.log"):
    """Returns a configured logger."""
    #ch logging.StreamHanler() # Console/terminal/stderr
    #ch setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile,
        #"meulog.log",
        maxBytes=300, # 10**6
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    # ch setFormatter(fmt)
    fh.setFormatter(fmt)
    #log.addHandler(ch)
    log.addHandler(fh)
    return log