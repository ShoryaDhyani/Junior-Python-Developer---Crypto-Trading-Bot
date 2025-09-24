import logging
import os
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def safe_float(value, name="value"):
    try:
        return float(value)
    except ValueError:
        log_error(f"{name} must be a number, got: {value}")
        return None


def safe_int(value, name="value"):
    try:
        return int(value)
    except ValueError:
        log_error(f"{name} must be an integer, got: {value}")
        return None


def load_api_keys():
    load_dotenv()
    key=os.getenv("API_KEY")
    secret=os.getenv("API_SECRET")
    return key,secret

def log_info(msg: str):
    logging.info(msg)

def log_error(msg: str):
    logging.error(msg)

if __name__=="__main__":
    log_info("Hello")
