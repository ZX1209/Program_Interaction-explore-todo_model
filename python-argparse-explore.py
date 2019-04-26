# import ArgumentParser() parse_args
# import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()

# add_argumnet
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)

# add_argument help
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# add_argument type
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument(
#                     "square",
#                     help="display a square of a given number",
#                     type=int
#                     )
# args = parser.parse_args()
# print(args.square**2)


# # action 指定和不指定 默认值
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#    print("verbosity turned on")

# # 简写
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# # add_argument choice
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print "the square of {} equals {}".format(args.square, answer)
# elif args.verbosity == 1:
#     print "{}^2 == {}".format(args.square, answer)
# else:
#     print answer


