import logging.config
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from .config import log_dir

log_dir.mkdir(parents=True, exist_ok=True)

log_path = log_dir / "livingspace-toolkit.log"

logger = logging.getLogger(name="livingspace_toolkit")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt="[%(levelname)s | %(filename)s | %(lineno)s] %(asctime)s: %(message)s",
                              datefmt="%Y-%m-%dT%H:%M:%S%z")
rotating_file_handler = RotatingFileHandler(
    log_path,
    maxBytes=2_000_000,   # 2MB
    backupCount=5,         # keep 5 old logs
    mode="a+",
    encoding="utf8"
)
stream_handler = StreamHandler()

rotating_file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(rotating_file_handler)
logger.addHandler(stream_handler)
