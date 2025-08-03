import logging 
from logging.handlers import TimedRotatingFileHandler

class AdmLogger:
    def __init__(self):
        self.logger_gui = logging.getLogger("gui")
        self.logger_logic = logging.getLogger("logic")
        self.logger_ad_operations = logging.getLogger("ad_operations")

        self._configure_logger(self.logger_gui)
        self._configure_logger(self.logger_logic)
        self._configure_logger(self.logger_ad_operations)

    def _configure_logger(self, logger):
        """Konfiguracja ogólna loggera, dodanie StreamHandler oraz FileHandler"""
        logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        file_handler = TimedRotatingFileHandler("app.log", when="midnight", interval=1, backupCount=7, encoding="utf-8", delay=True)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def get_logger(self, component: str):
        """Zwróć logger odpowiedni dla danego komponentu."""
        if component == "gui":
            return self.logger_gui
        elif component == "logic":
            return self.logger_logic
        elif component == "ad_operations":
            return self.logger_ad_operations
        else:
            raise ValueError(f"Nieznany komponent: {component}")
