import argparse

#
cmd_atgs_list = " add ".split()

# setup
parser = argparse.ArgumentParser()
parser.add_argument("echo")

# args parser
args = parser.parse_args(cmd_atgs_list)

# handle
if args.echo:
    print(args.echo)