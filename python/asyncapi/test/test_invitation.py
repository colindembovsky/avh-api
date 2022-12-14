# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.15.0-15704
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import avh_api_async
from avh_api_async.models.invitation import Invitation  # noqa: E501
from avh_api_async.rest import ApiException

class TestInvitation(unittest.TestCase):
    """Invitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Invitation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = avh_api_async.models.invitation.Invitation()  # noqa: E501
        if include_optional :
            return Invitation(
                identifier = '', 
                email = '', 
                settings = None
            )
        else :
            return Invitation(
        )

    def testInvitation(self):
        """Test Invitation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
