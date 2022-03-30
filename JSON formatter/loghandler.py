# -*- coding: utf-8 -*-
import logging


class GeneralLogging:

    def __init__(self, appname="RUN LOG"):
        self.log = logging.getLogger(appname)
        self.log.setLevel(logging.DEBUG)
        self.streamhandler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.streamhandler.setFormatter(self.formatter)
        self.log.addHandler(self.streamhandler)

    def error_logger(self, url="N/A", msg="ERROR OCCURED", error="N/A", response="N/A"):
        """
        Used for a more custom general logging and catching exceptions during API calls.
        """
        self.log.info("######### ERROR START #########")
        self.log.info('API URL: {}'.format(url))
        self.log.info(msg)
        self.log.error(error)
        self.log.info('API Response content: {}'.format(response))
        self.log.info("######### ERROR END #########")
        # self.removeFilehandler()

    def removefilehandler(self):
        """
        Use this for the error logger to clean it out in longer test runs.
        Doing so will however require you to re-instantiate the GeneralLogging class.
        """
        self.log.removeHandler(self.streamhandler)

    def info(self, msg):
        """
        Used for information logging
        :param msg: String
        """
        self.log.info(msg)

    def warning(self, msg):
        """
        Used for logging warnings
        :param msg: String
        """
        self.log.warning(msg)

    def exception(self, msg):
        """
        Used for logging Exceptions without stopping scripts.
        Stopping during an exception can however be good, so make sure to think things through.
        :param msg: String
        """
        self.log.exception(msg)
