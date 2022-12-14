# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.15.0-15704
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


class AgentAppStatus(object):
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
        'running': 'bool',
        'bundle_id': 'str'
    }

    attribute_map = {
        'running': 'running',
        'bundle_id': 'bundleID'
    }

    def __init__(self, running=None, bundle_id=None, local_vars_configuration=None):  # noqa: E501
        """AgentAppStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._running = None
        self._bundle_id = None
        self.discriminator = None

        self.running = running
        self.bundle_id = bundle_id

    @property
    def running(self):
        """Gets the running of this AgentAppStatus.  # noqa: E501

          # noqa: E501

        :return: The running of this AgentAppStatus.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this AgentAppStatus.

          # noqa: E501

        :param running: The running of this AgentAppStatus.  # noqa: E501
        :type running: bool
        """

        self._running = running

    @property
    def bundle_id(self):
        """Gets the bundle_id of this AgentAppStatus.  # noqa: E501

          # noqa: E501

        :return: The bundle_id of this AgentAppStatus.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this AgentAppStatus.

          # noqa: E501

        :param bundle_id: The bundle_id of this AgentAppStatus.  # noqa: E501
        :type bundle_id: str
        """

        self._bundle_id = bundle_id

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
        if not isinstance(other, AgentAppStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentAppStatus):
            return True

        return self.to_dict() != other.to_dict()
