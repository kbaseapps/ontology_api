"""Exception classes."""

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidParamsError(Error):
    def __init__(self, message):
        self.message = message

class InvalidUserError(Error):
    def __init__(self, message):
         self.message = message

class REError(Error):
    """Error from the RE API."""

    def __init__(self, resp):
        """Takes a requests response object."""
        try:
            body = resp.json()
            self.resp_json = body
        except ValueError:
            self.resp_json = None
        self.resp_text = resp.text

