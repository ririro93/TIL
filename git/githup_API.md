# Github_API
> need to authenticate for rate limit to be 5000 not 60

## using python requests
```python
import requests

URL = ''
username = ''
token = ''

res = requests.get(URL, auth=(username, token))
```

## using PyGithub library
>[PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)
```python
from github import Github

token = ''

g = Github(token)
```