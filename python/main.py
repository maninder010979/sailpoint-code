'''from github import Github

#
g = Github("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")

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/psf/requests-html.git", login_or_token="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")

print(g)
for repo in g.get_repos():
    print(repo.name)'''

import requests
r = requests.get('https://github.com/maninder010979/samples.git')
print(r)
print(r.text)
