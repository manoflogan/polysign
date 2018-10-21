"""
The module encapsulate all the classes that are used to aggreate all the log
information.
"""

import collections
import datetime
import jinja2
import logging
import os

import logging_config

logger = logging_config.get_logger('default')


class RequestAggregator(object):
    """Aggregates all the request metrics associated with a request."""

    def __init__(self):
        self.total_requests_by_date = collections.defaultdict(list)
        self.total_errors_by_date = collections.defaultdict(list)
        self.total_requests_by_user = collections.defaultdict(list)
        self.total_errors_by_user = collections.defaultdict(list)
        self.number_of_uniques = collections.OrderedDict()

    def initialise_datasets(self, date_object, user_id, status):
        """Initialies the data sets based on th date objects, user id and status.

        The following objects are initialised:

        1. total number of requests per a given date
        2. total number of requests per user
        3. total number of error requests per a given date
        4. total number of error requests per user id

        Args:
            date_object: date object representing the date of request
            user_id: unique user id represented as an string
            status: http status as an string
        """
        # status has to be 200.
        if status != '200':
            self.total_errors_by_date[date_object].append(user_id)
            self.total_errors_by_user[user_id].append(date_object)

        self.total_requests_by_date[date_object].append(user_id)
        self.total_requests_by_user[user_id].append(date_object)

    @property
    def total_requests(self):
        """Returns the total requests made."""
        count = 0
        for date_object in self.total_requests_by_date:
            count += len(self.total_requests_by_date[date_object])
        return count

    @property
    def total_errors(self):
        """Returns the total errors returned."""
        count = 0
        for date_object in self.total_errors_by_date:
            count += len(self.total_errors_by_date[date_object])
        return count

    @staticmethod
    def daterange(start_date, range_number):
        """Yields the date between start date and end date."""
        for number in range(range_number):
            yield start_date + datetime.timedelta(days=number)

    @property
    def total_number_of_days(self):
        """Returns the total unique number of days between two date ranges;
        both dates inclusive
        """
        sorted_iteritems = sorted(
            self.total_requests_by_date.items(), key=lambda x: x[0])
        # Min and max date
        min_date = sorted_iteritems[0][0]
        max_date = sorted_iteritems[-1][0]
        number_of_days = (max_date - min_date).days + 1

        logging.info('Aggregating all requests by date.')
        for dt in RequestAggregator.daterange(min_date, number_of_days):
            self.number_of_uniques[dt] = (
                len(self.total_requests_by_date.get(dt))
                if dt in self.total_requests_by_date else 0)
        return number_of_days

    @property
    def number_of_users(self):
        """Returns the total number of unique users."""
        return len(self.total_requests_by_user)

    def generate_reports(self):
        """Generates a string representation based on the information.

        The implementation populates an extracted template string to generate
        the report contents.

        Returns:
           populated template string
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(dir_path),
            autoescape=jinja2.select_autoescape(['txt']))
        temp = env.get_template('reports.txt')
        return temp.render({
            'total_requests': self.total_requests,
            'total_errors': self.total_errors,
            'number_of_days': self.total_number_of_days,
            'unique_users': self.number_of_users,
            'daily_uniques': self.number_of_uniques
        })
