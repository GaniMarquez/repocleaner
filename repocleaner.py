import argparse
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file', '-f',
                        required=True,
                        help='')
    parser.add_argument('--owner', '-o',
                        required=True,
                        help='')
    parser.add_argument('--token', '-t',
                        required=True,
                        help='')
    args = parser.parse_args()
    return args

def delete_repositories(owner, token, file):
    headers = {'Authorization': 'token {token}'.format(token=token)}
    with open(file) as file:
        repos = map(lambda x: x.strip(), file.readlines())
        for repo in repos:
            url = 'https://api.github.com/repos/{owner}/{repo}'.format(owner=owner, repo=repo)
            requests.delete(url, headers=headers)
            print('Succesfully deleted {repo}'.format(repo=repo))

def main():
    args = parse_arguments()
    delete_repositories(args.owner, args.token, args.file)

if __name__ == '__main__':
    main()