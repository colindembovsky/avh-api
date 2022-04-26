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


class ApiNotFoundError(object):
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
        'error': 'str',
        'error_id': 'str',
        'name': 'str',
        'params': 'object'
    }

    attribute_map = {
        'error': 'error',
        'error_id': 'errorID',
        'name': 'name',
        'params': 'params'
    }

    def __init__(self, error=None, error_id=None, name=None, params=None, local_vars_configuration=None):  # noqa: E501
        """ApiNotFoundError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._error_id = None
        self._name = None
        self._params = None
        self.discriminator = None

        self.error = error
        self.error_id = error_id
        self.name = name
        self.params = params

    @property
    def error(self):
        """Gets the error of this ApiNotFoundError.  # noqa: E501

        Error text  # noqa: E501

        :return: The error of this ApiNotFoundError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiNotFoundError.

        Error text  # noqa: E501

        :param error: The error of this ApiNotFoundError.  # noqa: E501
        :type error: str
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def error_id(self):
        """Gets the error_id of this ApiNotFoundError.  # noqa: E501

        Error ID  # noqa: E501

        :return: The error_id of this ApiNotFoundError.  # noqa: E501
        :rtype: str
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this ApiNotFoundError.

        Error ID  # noqa: E501

        :param error_id: The error_id of this ApiNotFoundError.  # noqa: E501
        :type error_id: str
        """
        if self.local_vars_configuration.client_side_validation and error_id is None:  # noqa: E501
            raise ValueError("Invalid value for `error_id`, must not be `None`")  # noqa: E501

        self._error_id = error_id

    @property
    def name(self):
        """Gets the name of this ApiNotFoundError.  # noqa: E501

        Name of the object requested  # noqa: E501

        :return: The name of this ApiNotFoundError.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiNotFoundError.

        Name of the object requested  # noqa: E501

        :param name: The name of this ApiNotFoundError.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def params(self):
        """Gets the params of this ApiNotFoundError.  # noqa: E501

        params provided by user  # noqa: E501

        :return: The params of this ApiNotFoundError.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ApiNotFoundError.

        params provided by user  # noqa: E501

        :param params: The params of this ApiNotFoundError.  # noqa: E501
        :type params: object
        """

        self._params = params

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
        if not isinstance(other, ApiNotFoundError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiNotFoundError):
            return True

        return self.to_dict() != other.to_dict()
