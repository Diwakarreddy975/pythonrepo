import logging

class log001:

    def generate_log(self):

        logging.basicConfig(
            filename="Reports\miniproject01.log",
            level=logging.INFO,filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p'
        )
        logger=logging.getLogger()
        logger.setLevel(level="INFO")
        return logger