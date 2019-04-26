import argparse

#
cmd_atgs_list = " add ".split()

# setup
parser = argparse.ArgumentParser()
parser.add_argument("action" ,type=str,choices=['add','del','show'])
parser.add_argument("arg",type=str)

# args parser
args = parser.parse_args()

# handle
if args.action:
    if args.action == "add":
        print("add",args.arg)
    elif args.action == "del":
        print("del",args.arg)
    elif args.action == "show":
        print("show",args.arg)