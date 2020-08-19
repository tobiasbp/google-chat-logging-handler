import logging
import os

import google_chat_logging_handler as gclh

# Get the Webhook URL from the environment variable GCHAT_LOG_WEBHOOK 
webhook_url = os.getenv("GCHAT_LOG_WEBHOOK")
 
# List of logging handlers to use
logging_handlers = []

# Create a Google Chat logging handler
gch = gclh.GoogleChatHandler(webhook_url)

# The format of a log entries posted to Google Chat
f = logging.Formatter("%(message)s")

# Add the formatter to the Google Chat handler
gch.setFormatter(f)

# Set log level for logging to Google Chat
gch.setLevel("INFO")

# Add handler for logging to Google Chat to list of handlers to use
logging_handlers.append(gch)


# Add handler for logging to stdout
logging_handlers.append(logging.StreamHandler())

# Configure logging
logging.basicConfig(
  format='%(asctime)s:%(levelname)s:%(message)s',
  level="INFO",
  handlers=logging_handlers
  )


logging.info("Hello world from _GoogleChatHandler_")
