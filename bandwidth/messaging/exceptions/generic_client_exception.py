# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from bandwidth.api_helper import APIHelper
import bandwidth.exceptions.api_exception
import bandwidth.messaging.models.field_error


class GenericClientException(bandwidth.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the GenericClientException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(GenericClientException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.mtype = dictionary.get('type')
        self.description = dictionary.get('description')
        self.field_errors = None
        if dictionary.get('fieldErrors') is not None:
            self.field_errors = [bandwidth.messaging.models.field_error.FieldError.from_dictionary(x) for x in dictionary.get('fieldErrors')]