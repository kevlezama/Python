import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FILE = "basic.log"

logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=FILE
    )
    
logging.debug("This is a debug message.")
logging.info("This is a debug message.")
logging.warning("This is a debug message.")
logging.error("This is a debug message.")
logging.critical("This is a debug message.")

