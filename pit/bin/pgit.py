#!/usr/bin/env python
import os
import sys
import pathlib
import argparse
from datetime import datetime

from pit.workspace import WorkSpace
from pit.database import Database
from pit.entry import Entry
from pit.tree import Tree
from pit.commit import Commit
from pit.refs import Refs
from pit.blob import Blob
from pit.author import Author


parser = argparse.ArgumentParser(prog='pit',
                                 usage='same as git(my big bro!)')
subparsers = parser.add_subparsers(dest='command', required=True)
init_parser = subparsers.add_parser('init',
                                    help='Initialize an empty pit repo')
init_repo_path = init_parser.add_argument('path', default=os.getcwd(), nargs='?')
commit_parser = subparsers.add_parser('commit',
                                      help='Create a commit')

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
    refs = Refs(git_path)

    entries = []
    for file_name in workspace.list_files():
        data = workspace.read_file(file_name)
        blob = Blob(data)

        database.store(blob)
        is_executable = workspace.is_executable(file_name)
        entry = Entry(file_name, blob.oid, stat)
        entries.append(entry)

    tree = Tree(entries)
    database.store(tree)

    name = os.environ.get('GIT_AUTHOR_NAME', 'DefaultAuthor')
    email = os.environ.get('GIT_AUTHOR_EMAIL', 'mail@example.com')
    time_now = datetime.now().astimezone()
    author = Author(name, email, time_now)
    parent = refs.read_head()
    message = sys.stdin.readline(100)

    commit = Commit(parent, tree.oid, author, message)
    database.store(commit)
    refs.update_head(commit.oid)

    is_root = '(root-commit) ' if not parent else ''
    print(f'[{is_root} {commit.oid}] {message.strip()}')
    sys.exit(0)

def main():
    command_map = {
        'init': do_init,
        'commit': do_commit
    }
    command_function = command_map[args.command]
    command_function()

if __name__=='__main__':
    main()
