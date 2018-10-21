__Log Analyzer Code Question!!__

Dear PolySign applicant- we are very excited to begin the interview process with you. Below is a question that you can work on at your leisure in the next 2 days (it should take no more than 1-2 hours). Please feel free to email anna@polysign.io with any questions (we expect that you’ll run into things). When you are finished, email the python file to anna@polysign.io

# Background
You will a set of simple usage metrics given a server access log. The access log has the following format:
2018-01-01T10:00:00 1 200
2018-01-01T23:13:09 2 401
2018-01-03T10:01:01 1 200
2018-01-05T11:14:00 1 200

Each line represents a single request.
Each line contains a set of tab‐delimited fields.
timestamp expressed as an ISO 8601 string, YYYY-MM-DDTHH:MM:SS . You can assume UTC timezone for all entries.
user_id is a unique numeric identifier.
status_code is the HTTP status code returned. 200 indicates success. Any other value represents an error.
Log lines are sorted by timestamp in strictly increasing order.

# Your Task
You will be provided with a set of access logs (they are also in the Google Drive folder). Write a program that computes and prints the following summary and daily metrics for each file.
Summary Metrics
1. Total number of requests.
2. Total number of errors.
3. Total number of days represented.
4. Total number of unique users.
Daily Metrics
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
Your program should take a single command line argument specifying the log file to read. The output format shown above is a rough guideline. Correct results are more important than matching the format.
Feel free to ask questions!
Communicate any shortcuts you take based on the time constraints. This may be done via comments in your code sample.
