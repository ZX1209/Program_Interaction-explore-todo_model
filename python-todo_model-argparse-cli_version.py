import argparse
import sqlite3

# setup
parser = argparse.ArgumentParser()


parser.add_argument("action", type=str,
                    choices=[
                        'todo',
                        'done',
                        'show',
                        'update',
                        'del',
                        'create'
                    ])
parser.add_argument("object", type=str,nargs='+')

# args parser
args = parser.parse_args()

# handle
if args.action:
    if args.action == "todo":
        print("todo", args.object)
    elif args.action == "done":
        print("done", args.object)
    elif args.action == "show":
        print("show", args.object)
    elif args.action == "update":
        if args.to:
            print("update", args.object,'to',args.to)
    else:
        print('not difined')
