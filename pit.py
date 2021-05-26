import os
import sys
import pathlib
import argparse

from workspace import WorkSpace
from database import Database


parser = argparse.ArgumentParser(prog='pit',
                                 usage='same as git(my big bro!)')
subparsers = parser.add_subparsers(dest='command', required=True)
init_parser = subparsers.add_parser('init',
                                    help='Initialize an empty pit repo')
init_repo_path = init_parser.add_argument('path', default=os.getcwd(), nargs='?')
commit_parser = subparsers.add_parser('commit',
                                      help='Initialize an empty pit repo')

args = parser.parse_args()


def do_init():
    git_path = os.path.join(
        os.path.abspath(args.path),
        '.git'
    )
    for directory in ['objects', 'refs']:
        git_subdirectory = os.path.join(git_path, directory)
        try:
            pathlib.Path(git_subdirectory).mkdir(parents=True, exist_ok=True)
        except PermissionError as e:
            print(f'fatal: Permission Error {e.filename}')
            sys.exit(1)
    print(f'Initialized empty pit repository in {git_path}')


def do_commit():
    root_path = os.getcwd()
    git_path = os.path.join(
        root_path,
        '.git'
    )
    db_path = os.path.join(
        git_path,
        'objects'
    )
    workspace = WorkSpace(root_path)
    database = Database(db_path)

    for file in workspace.list_files():
        data = workspace.read_file(file)
        blob = Blob(data)
        database.store(blob)
    print(workspace.list_files())

def main():
    command_map = {
        'init': do_init,
        'commit': do_commit
    }
    command_function = command_map[args.command]
    command_function()

if __name__=='__main__':
    main()
