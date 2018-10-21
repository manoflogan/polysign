__Log Analyzer Code Question!!__

- [Background](#background)
- [Your Task](#your-task)
- [Daily Metrics](#daily-metrics)
- [Additional Notes](#additional-notes)


# Background
You will a set of simple usage metrics given a server access log. The access log has the following format:

+ `2018-01-01T10:00:00 1 200`

+ `2018-01-01T23:13:09 2 401`

+ `2018-01-03T10:01:01 1 200`

+ `2018-01-05T11:14:00 1 200`

* Each line represents a single request.
* Each line contains a set of tab‐delimited fields.
    + timestamp expressed as an ISO 8601 string, YYYY-MM-DDTHH:MM:SS . You can assume UTC timezone for all entries.
    + user_id is a unique identifier.
    + status_code is the HTTP status code returned. 200 indicates success. Any other value represents an error.
* Log lines are sorted by timestamp in strictly increasing order.


# Your Task
You will be provided with a set of access logs (they are also in the Google Drive folder). Write a program that computes and prints the following summary and daily metrics for each file.
Summary Metrics
* Total number of requests.
* Total number of errors.
* Total number of days represented.
* Total number of unique users.


# Daily Metrics
For each day in the range represented by the access log, calculate the number of unique users.

For example, the output from sample.log should give you the following. Please double check your code to ensure it outputs these numbers from sample.log!

Totals
------
Requests 4

Errors 1

Days 5

Unique Users 2

Daily Uniques
-------------
2018-01-01 2

2018-01-02 0

2018-01-03 1

2018-01-04 0

2018-01-05 1


# Additional Notes
The program should take a single command line argument specifying the log file to read. The main module is invoked as follows:

`python log_aggregator.py -f <fully_qualified_path of the logfile>`
