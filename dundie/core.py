"""Core module of dundie"""
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from  filepath to the database"""
    
    
    try:
        with open (filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        #print(f"File not found {e}")
        log.error(str(e))
        raise e