# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TwoFactorVerifyRequestSchema(object):

    """Implementation of the 'TwoFactorVerifyRequestSchema' model.

    TODO: type model description here.

    Attributes:
        to (string): The phone number to send the 2fa code to.
        mfrom (string): The application phone number, the sender of the 2fa
            code.
        application_id (string): The application unique ID, obtained from
            Bandwidth.
        scope (string): An optional field to denote what scope or action the
            2fa code is addressing.  If not supplied, defaults to "2FA".
        digits (float): The number of digits for your 2fa code.  The valid
            number ranges from 2 to 8, inclusively.
        expiration_time_in_minutes (float): The time period, in minutes, to
            validate the 2fa code.  By setting this to 3 minutes, it will mean
            any code generated within the last 3 minutes are still valid.  The
            valid range for expiration time is between 0 and 15 minutes,
            exclusively and inclusively, respectively.
        code (string): The generated 2fa code to check if valid

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "mfrom": 'from',
        "application_id": 'applicationId',
        "digits": 'digits',
        "expiration_time_in_minutes": 'expirationTimeInMinutes',
        "code": 'code',
        "scope": 'scope'
    }

    def __init__(self,
                 to=None,
                 mfrom=None,
                 application_id=None,
                 digits=None,
                 expiration_time_in_minutes=None,
                 code=None,
                 scope=None):
        """Constructor for the TwoFactorVerifyRequestSchema class"""

        # Initialize members of the class
        self.to = to
        self.mfrom = mfrom
        self.application_id = application_id
        self.scope = scope
        self.digits = digits
        self.expiration_time_in_minutes = expiration_time_in_minutes
        self.code = code

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        application_id = dictionary.get('applicationId')
        digits = dictionary.get('digits')
        expiration_time_in_minutes = dictionary.get('expirationTimeInMinutes')
        code = dictionary.get('code')
        scope = dictionary.get('scope')

        # Return an object of this model
        return cls(to,
                   mfrom,
                   application_id,
                   digits,
                   expiration_time_in_minutes,
                   code,
                   scope)