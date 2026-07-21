import logging


logging.basicConfig(
    filename= "organizer.log",
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    force=True
)

logger = logging.getLogger(__name__)



