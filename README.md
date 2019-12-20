# Please Commit
Script that returns number of days since last commit for each user in list of github users.

## CONTENTS
1. [Requirements](#requirements)
2. [Token](#github-token)
3. [Local Setup](#local-setup)

## REQUIREMENTS
* Github Personal Access Token
* Python 3.x
* Python's `requests` library installed system wide
* This might require some modification to the token path to work in windows

## Github Token
Create a GitHub Personal Access Token [here](https://github.com/settings/tokens)

## Local Setup
1. Create a `.credentials` folder in your home directory
2. Create a `GITHUB.txt` file inside that folder and add your token.
3. Create `config.py` file in project root and add dict of students:

```
students = {
    'Bob'       :   'bobsgithubusername',
    'Jim'       :   'jimsgithubusername',
    ...  
}
```