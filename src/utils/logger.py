import logging
from src.config import Config

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if Config.DEBUG else logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
