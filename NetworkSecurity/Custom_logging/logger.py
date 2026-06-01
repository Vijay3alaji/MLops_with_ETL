import os
import logging
from datetime import datetime

# 1. Define the unique log file name with a timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# 2. Create an absolute path to the 'logs' folder inside your current working directory
LOG_DIR_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR_PATH, exist_ok=True)

# 3. Combine the directory path and file name into the final path
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)


# 4. Configure logging to write to BOTH the file and your terminal
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # This writes logs to your new file
        logging.StreamHandler()             # This keeps printing logs to your terminal screen
    ]
)

logger = logging.getLogger(__name__)

# Test it out to verify it works!
if __name__ == "__main__":
    logger.info("Logging has been successfully configured!")