# python-network_1

This directory contains Python scripts that make HTTP requests, first with the `urllib` package and then with the `requests` package.

## Requirements

- Python 3, interpreted on Ubuntu 20.04 LTS
- Code follows the `pycodestyle` (PEP 8) style
- All files are executable and start with `#!/usr/bin/python3`
- Every module has a docstring
- Scripts `0` to `3` may only import `urllib` (and `sys` where noted); scripts `4` to `10` may only import `requests` (and `sys` where noted)

## Files

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `urllib` and displays the body, its type and its content |
| `1-hbtn_header.py` | Takes a URL and displays the `X-Request-Id` header value of the response (`urllib`) |
| `2-post_email.py` | Sends a POST request with an `email` parameter to a URL and displays the decoded body (`urllib`) |
| `3-error_code.py` | Displays the decoded body of a response, or `Error code: <status>` on an `HTTPError` (`urllib`) |
| `4-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `requests` and displays the body, its type and its content |
| `5-hbtn_header.py` | Takes a URL and displays the `X-Request-Id` header value of the response (`requests`) |
| `6-post_email.py` | Sends a POST request with an `email` parameter to a URL and displays the body (`requests`) |
| `7-error_code.py` | Displays the body of a response, or `Error code: <status>` if the status code is 400 or more (`requests`) |
| `8-json_api.py` | Sends a POST request with the letter `q` to a search API and displays `[<id>] <name>`, `No result` or `Not a valid JSON` |
| `10-my_github.py` | Uses Basic Authentication with a username and a personal access token to display your GitHub id |

## Example

```
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
```
