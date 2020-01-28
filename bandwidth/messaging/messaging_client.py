# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from bandwidth.decorators import lazy_property
from bandwidth.configuration import Configuration
from bandwidth.configuration import Environment
from bandwidth.messaging.controllers.api_controller import APIController


class MessagingClient(object):

    @lazy_property
    def client(self):
        return APIController(self.config)

    def __init__(self, timeout=60, max_retries=3, backoff_factor=0,
                 environment=Environment.PRODUCTION,
                 messaging_basic_auth_user_name='TODO: Replace',
                 messaging_basic_auth_password='TODO: Replace',
                 voice_basic_auth_user_name='TODO: Replace',
                 voice_basic_auth_password='TODO: Replace', config=None):
        if config is None:
            self.config = Configuration(timeout=timeout,
                                        max_retries=max_retries,
                                        backoff_factor=backoff_factor,
                                        environment=environment,
                                        messaging_basic_auth_user_name=messaging_basic_auth_user_name,
                                        messaging_basic_auth_password=messaging_basic_auth_password,
                                        voice_basic_auth_user_name=voice_basic_auth_user_name,
                                        voice_basic_auth_password=voice_basic_auth_password)
        else:
            self.config = config