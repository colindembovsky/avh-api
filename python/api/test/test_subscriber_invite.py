"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.15.0-15704
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import avh_api
from avh_api.model.coupon_options import CouponOptions
from avh_api.model.plan import Plan
from avh_api.model.trial import Trial
globals()['CouponOptions'] = CouponOptions
globals()['Plan'] = Plan
globals()['Trial'] = Trial
from avh_api.model.subscriber_invite import SubscriberInvite


class TestSubscriberInvite(unittest.TestCase):
    """SubscriberInvite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriberInvite(self):
        """Test SubscriberInvite"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubscriberInvite()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
