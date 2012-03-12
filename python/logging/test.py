import logging

def main():
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    exit(main())
