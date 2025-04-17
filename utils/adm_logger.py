# import logging

# class AdmLogger:
#     _logger = None

#     @classmethod
#     def get_logger(cls):
#         if cls._logger:
#             return cls._logger

#         logger = logging.getLogger("AdmLogger")
#         logger.setLevel(logging.DEBUG)

#         handler = logging.StreamHandler()
#         handler.setLevel(logging.DEBUG)

#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)

#         logger.addHandler(handler)

#         file_handler = logging.FileHandler("app.log", encoding="utf-8")
#         file_handler.setLevel(logging.DEBUG)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)

#         cls._logger = logger
#         return logger

#     @classmethod
#     def info(cls, message):
#         logger = cls.get_logger()
#         logger.info(message)

#     @classmethod
#     def error(cls, message):
#         logger = cls.get_logger()
#         logger.error(message)

#     @classmethod
#     def warning(cls, message):
#         logger = cls.get_logger()
#         logger.warning(message)

#     @classmethod
#     def debug(cls, message):
#         logger = cls.get_logger()
#         logger.debug(message)

#     @classmethod
#     def exception(cls, message):
#         logger = cls.get_logger()
#         logger.exception(message)





# utils/adm_logger.py
import logging 
from logging.handlers import TimedRotatingFileHandler

class AdmLogger:
    def __init__(self):
        # Inicjalizacja loggerów
        self.logger_gui = logging.getLogger("gui")
        self.logger_logic = logging.getLogger("logic")
        self.logger_ad_operations = logging.getLogger("ad_operations")

        self._configure_logger(self.logger_gui)
        self._configure_logger(self.logger_logic)
        self._configure_logger(self.logger_ad_operations)

    def _configure_logger(self, logger):
        """Konfiguracja ogólna loggera, dodanie StreamHandler oraz FileHandler"""
        # Ustawienie poziomu logowania
        logger.setLevel(logging.DEBUG)

        # Handler do konsoli
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Handler do zapisu w pliku
        # file_handler = logging.FileHandler("app.log", encoding="utf-8")
        file_handler = TimedRotatingFileHandler("app.log", when="midnight", interval=1, backupCount=7, encoding="utf-8")
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
