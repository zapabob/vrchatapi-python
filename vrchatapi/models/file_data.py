# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.9.1
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from vrchatapi.configuration import Configuration


class FileData(object):
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
        'category': 'str',
        'file_name': 'str',
        'md5': 'str',
        'size_in_bytes': 'int',
        'status': 'FileStatus',
        'upload_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'category': 'category',
        'file_name': 'fileName',
        'md5': 'md5',
        'size_in_bytes': 'sizeInBytes',
        'status': 'status',
        'upload_id': 'uploadId',
        'url': 'url'
    }

    def __init__(self, category='queued', file_name=None, md5=None, size_in_bytes=None, status=None, upload_id='', url=None, local_vars_configuration=None):  # noqa: E501
        """FileData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._category = None
        self._file_name = None
        self._md5 = None
        self._size_in_bytes = None
        self._status = None
        self._upload_id = None
        self._url = None
        self.discriminator = None

        self.category = category
        self.file_name = file_name
        self.md5 = md5
        self.size_in_bytes = size_in_bytes
        self.status = status
        self.upload_id = upload_id
        self.url = url

    @property
    def category(self):
        """Gets the category of this FileData.  # noqa: E501


        :return: The category of this FileData.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FileData.


        :param category: The category of this FileData.  # noqa: E501
        :type category: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["multipart", "queued", "simple"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def file_name(self):
        """Gets the file_name of this FileData.  # noqa: E501


        :return: The file_name of this FileData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileData.


        :param file_name: The file_name of this FileData.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) < 1):
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._file_name = file_name

    @property
    def md5(self):
        """Gets the md5 of this FileData.  # noqa: E501


        :return: The md5 of this FileData.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileData.


        :param md5: The md5 of this FileData.  # noqa: E501
        :type md5: str
        """
        if self.local_vars_configuration.client_side_validation and md5 is None:  # noqa: E501
            raise ValueError("Invalid value for `md5`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                md5 is not None and len(md5) < 0):
            raise ValueError("Invalid value for `md5`, length must be greater than or equal to `0`")  # noqa: E501

        self._md5 = md5

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this FileData.  # noqa: E501


        :return: The size_in_bytes of this FileData.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this FileData.


        :param size_in_bytes: The size_in_bytes of this FileData.  # noqa: E501
        :type size_in_bytes: int
        """
        if self.local_vars_configuration.client_side_validation and size_in_bytes is None:  # noqa: E501
            raise ValueError("Invalid value for `size_in_bytes`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size_in_bytes is not None and size_in_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `size_in_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size_in_bytes = size_in_bytes

    @property
    def status(self):
        """Gets the status of this FileData.  # noqa: E501


        :return: The status of this FileData.  # noqa: E501
        :rtype: FileStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileData.


        :param status: The status of this FileData.  # noqa: E501
        :type status: FileStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def upload_id(self):
        """Gets the upload_id of this FileData.  # noqa: E501


        :return: The upload_id of this FileData.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this FileData.


        :param upload_id: The upload_id of this FileData.  # noqa: E501
        :type upload_id: str
        """
        if self.local_vars_configuration.client_side_validation and upload_id is None:  # noqa: E501
            raise ValueError("Invalid value for `upload_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upload_id is not None and len(upload_id) < 0):
            raise ValueError("Invalid value for `upload_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._upload_id = upload_id

    @property
    def url(self):
        """Gets the url of this FileData.  # noqa: E501


        :return: The url of this FileData.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileData.


        :param url: The url of this FileData.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, FileData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileData):
            return True

        return self.to_dict() != other.to_dict()