"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.9.0-13085
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import avh_api
from avh_api.model.project_quota import ProjectQuota
from avh_api.model.project_settings import ProjectSettings
from avh_api.model.project_usage import ProjectUsage
globals()['ProjectQuota'] = ProjectQuota
globals()['ProjectSettings'] = ProjectSettings
globals()['ProjectUsage'] = ProjectUsage
from avh_api.model.project import Project


class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProject(self):
        """Test Project"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Project()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
