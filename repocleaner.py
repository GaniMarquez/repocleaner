import os
import argparse
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--cleanup', '-c',
                        action='store_true',
                        help='')
    parser.add_argument('--file', '-f',
                        default='repos',
                        help='')
    parser.add_argument('--token', '-t',
                        default=None,
                        help='')
    args = parser.parse_args()
    return args

def delete_repositories(token, file):
    headers = {'Authorization': 'token {token}'.format(token=token)}
    with open(file) as file:
        repos = map(lambda x: x.strip(), file.readlines())
        for repo in repos:
            url = 'https://api.github.com/repos/{repo}'.format(repo=repo)
            requests.delete(url, headers=headers)
            print 'Succesfully deleted {repo}'.format(repo=repo)
    os.system('rm {file}'.format(file=file))

def main():
    args = parse_arguments()
    delete_repositories(args.token, args.file)

if __name__ == '__main__':
    main()