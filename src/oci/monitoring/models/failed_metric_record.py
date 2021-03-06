# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FailedMetricRecord(object):
    """
    The record of a single metric object that failed input validation and the reason for the failure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FailedMetricRecord object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this FailedMetricRecord.
        :type message: str

        :param metric_data:
            The value to assign to the metric_data property of this FailedMetricRecord.
        :type metric_data: MetricDataDetails

        """
        self.swagger_types = {
            'message': 'str',
            'metric_data': 'MetricDataDetails'
        }

        self.attribute_map = {
            'message': 'message',
            'metric_data': 'metricData'
        }

        self._message = None
        self._metric_data = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this FailedMetricRecord.
        An error message indicating the reason that the indicated metric object failed input validation.


        :return: The message of this FailedMetricRecord.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this FailedMetricRecord.
        An error message indicating the reason that the indicated metric object failed input validation.


        :param message: The message of this FailedMetricRecord.
        :type: str
        """
        self._message = message

    @property
    def metric_data(self):
        """
        **[Required]** Gets the metric_data of this FailedMetricRecord.
        Identifier of a metric object that failed input validation.


        :return: The metric_data of this FailedMetricRecord.
        :rtype: MetricDataDetails
        """
        return self._metric_data

    @metric_data.setter
    def metric_data(self, metric_data):
        """
        Sets the metric_data of this FailedMetricRecord.
        Identifier of a metric object that failed input validation.


        :param metric_data: The metric_data of this FailedMetricRecord.
        :type: MetricDataDetails
        """
        self._metric_data = metric_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
