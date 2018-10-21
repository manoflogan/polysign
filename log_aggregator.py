"""
This module represents a single point of entry into the log module classes.
"""

import argparse
import datetime
import logging
import re

import log_models as models
import logging_config

logger = logging_config.get_logger('default')

LOG_PATTERN = re.compile('^(.*)T.*\\t([A-Za-z0-9]+)\\t([XXX|0-9]+)$')


class InvalidDataSetException(Exception):
    """Raised if data set is found to be invalid."""

    def __init__(self, line):
        """Line that represents an invalid data set."""
        super().__init__('Invalid format for line: {}'.format(line))


def parse_logs_and_generate_report(file_path):
    """Initialises the data sets and generates reports.

    The implementation is responsible for extracting the timestamp, user id
    and statuses.

    Args:
       file_path: fully qualified file path of the log file
    """
    aggregator = models.RequestAggregator()
    logger.info('Initiating the parser and generating reports')
    with open(file_path, 'rb') as f:
        for line in f:
            line_str = line.decode('utf-8').replace('\n', '')
            if not line_str:
                logging.warn(
                    'The following line {} was found to be invalid'.format(
                        line_str))
                continue
            (date_object, user_id, status) = read_from_log_file(line_str)
            aggregator.initialise_datasets(date_object, user_id, status)
    logging.info('Generating reports for {}'.format(file_path))
    print(aggregator.generate_reports())


def read_from_log_file(line):
    """Read the contents of a log file.

    Args:
        line:  string representing the content of a file

    Returns:
        tuple representing the date string, user id, and status code
    """
    result = LOG_PATTERN.match(line)
    if result is None:
        logging.error('No expression match was found for {}.'.format(line))
        raise InvalidDataSetException(line)
    grp = result.groups()
    (date_object, user_id,
     status) = (datetime.datetime.strptime(grp[0], '%Y-%m-%d').date(),
                grp[1], grp[2])
    return date_object, user_id, status


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Parsing logs')
    arg_parser.add_argument(
        '-f',  type=str, action='store',
        help='Fully qualified path to the log file name', required='True')
    args, unknown_args = arg_parser.parse_known_args()
    logger.info('The log file path = %s', args.f)
    parse_logs_and_generate_report(args.f)
