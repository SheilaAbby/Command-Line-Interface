# Exampe 1

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('name')
# parser.add_argument('num', type=int)

# args = parser.parse_args()

# for _ in range(args.num):
#     print(f"I'm sorry {args.name}, I'm afraid I can't do that")

# Example 2
# tries = 0
# while True:
#     name = input("What's your name?\n")
#     if name != None or name != " ":
#         break
#     else:
#         tries +=1
#     if tries > 10:
#         break
#     else:
#         continue
# print("Hello", name)


# Example 3 : Prints sum of int values entered on the terminal.
import argparse
def my_const_fun(*args, **kwargs):
    print("Const", args, kwargs)
 
def my_default_fun(*args, **kwargs):
    print("Default", args, kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+")
    parser.add_argument("--sum", dest='accumulate', action='store_const', const=sum, default=max)
    parser.add_argument("--math", dest='math_is_fun', action='store_const', const=my_const_fun, default=my_default_fun)
    args = parser.parse_args()
    print(sum(args.integers))
    # print(args.accumulate(args.integers))
    # print(max(args.integers)) returns the highest value in the list
    # print(args.accumulate(args.integers))
