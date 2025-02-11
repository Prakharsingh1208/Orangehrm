import logging

class Log_gen:
    @staticmethod
    def create_log():
        logging.basicConfig(filename=".\\logs\\logfile.log", format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", force=True)
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log
