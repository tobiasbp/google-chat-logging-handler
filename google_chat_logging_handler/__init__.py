import logging
import http.client
import json

from urllib.parse import urlparse


class GoogleChatHandler(logging.Handler):
    """A handler for logging to Google Chat using webhooks"""

    def __init__(self, webhook: str) -> None:
        """Instantiate handler with webhook"""
        # Parse webhook to URL object
        self._url = urlparse(webhook)

        # Call parent instantiator
        logging.Handler.__init__(self)

    def emit(self, record: logging.LogRecord) -> None:
        """Post a record to Goggle Chat"""
        try:

            # The connection to use
            conn = http.client.HTTPSConnection(self._url.netloc)

            # Convert the log record to a JSON object to post
            json_to_post = json.dumps({"text": f"{self.format(record)}"})

            # Post the request
            conn.request("POST", f"{self._url.path}?{self._url.query}", json_to_post)

            # Get the response
            response = conn.getresponse()

            # Would we ever get anything other than 200 on a success?
            if response.status != 200:
                raise ConnectionError("Non 200 response when posting to Google Chat.")

        except Exception:
            self.handleError(record)
