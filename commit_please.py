import datetime
import json
import requests
import pathlib

from config import students

with open('{home}/.credentials/GITHUB.txt'.format(home=pathlib.Path.home())) as cred:
    TOKEN = cred.read().strip()

def githubAPI(user):
    '''
    API call that returns JSON from GitHub GraphQL V4 API
    '''
    variables = {'user' : user}
    headers = {"Authorization": "Bearer %s" % TOKEN}

    query = """
        query ($user: String!) {
            user(login: $user) {
                name
                repositoriesContributedTo(contributionTypes: COMMIT, orderBy: {field: CREATED_AT, direction: ASC}, first: 100, includeUserRepositories: true) {
                edges {
                    node {
                    name
                    isArchived
                    pushedAt
                    }
                }
                }
            }
            }
        """

    r = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)
    if r.status_code != 200:
        raise Exception("Query failed with code of {} and returned {}".format(r.status_code, r.json()))
    else:
        # with open('repos.json', 'w') as f:
        #     json.dump(r.json(), f, indent=4, sort_keys=True)
        return r.json()

def parse_dates(json_obj):
    '''
    Extract dates from json and determine latest commit
    '''
    date_list = []
    for item in json_obj['data']['user']['repositoriesContributedTo']['edges']:
        date_list.append(datetime.datetime.strptime(item['node']['pushedAt'][0:10], '%Y-%m-%d'))
    date_list.sort()

    return date_list

def main(student):
    repos = githubAPI(student)
    dates = parse_dates(repos)

    now = datetime.datetime.now()

    return (now - dates[-1]).days

if __name__ == '__main__':
    # j = githubAPI(query, variables)
    # print(parse_dates(j))
    print("Days since last commit:")
    print("")
    for s in students:
        try:
            print("{} : {}".format(s, int(main(students[s]))))
        except TypeError as e:
            print(s, e)