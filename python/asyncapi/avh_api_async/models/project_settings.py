# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.9.0-13085
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from avh_api_async.configuration import Configuration


class ProjectSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'version': 'float',
        'internet_access': 'bool',
        'dhcp': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'internet_access': 'internet-access',
        'dhcp': 'dhcp'
    }

    def __init__(self, version=None, internet_access=None, dhcp=None, local_vars_configuration=None):  # noqa: E501
        """ProjectSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._internet_access = None
        self._dhcp = None
        self.discriminator = None

        self.version = version
        self.internet_access = internet_access
        self.dhcp = dhcp

    @property
    def version(self):
        """Gets the version of this ProjectSettings.  # noqa: E501


        :return: The version of this ProjectSettings.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProjectSettings.


        :param version: The version of this ProjectSettings.  # noqa: E501
        :type version: float
        """

        self._version = version

    @property
    def internet_access(self):
        """Gets the internet_access of this ProjectSettings.  # noqa: E501


        :return: The internet_access of this ProjectSettings.  # noqa: E501
        :rtype: bool
        """
        return self._internet_access

    @internet_access.setter
    def internet_access(self, internet_access):
        """Sets the internet_access of this ProjectSettings.


        :param internet_access: The internet_access of this ProjectSettings.  # noqa: E501
        :type internet_access: bool
        """

        self._internet_access = internet_access

    @property
    def dhcp(self):
        """Gets the dhcp of this ProjectSettings.  # noqa: E501


        :return: The dhcp of this ProjectSettings.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this ProjectSettings.


        :param dhcp: The dhcp of this ProjectSettings.  # noqa: E501
        :type dhcp: bool
        """

        self._dhcp = dhcp

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectSettings):
            return True

        return self.to_dict() != other.to_dict()
