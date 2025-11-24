from loguru import logger
import os

def configure_loguru():
    os.makedirs("logs", exist_ok=True)

    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="7 days",
        encoding="utf-8",
        enqueue=True 
    )
    import logging
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            logger.log(level, record.getMessage())

    
    logging.getLogger().handlers = [InterceptHandler()]