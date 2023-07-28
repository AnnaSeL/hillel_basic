"""Calculator"""
import argparse
import operator


def multiply(a: int, b: int):
    return a*b


def div(a: int, b: int) -> int:
    return a//b

def main(args):
    calc_map = {'mul':operator.mul,
                'div':operator.truediv,
                'add':operator.add,
                'sub':operator.sub}
    result = calc_map[args.operation](args.op_1, args.op_2)
    print(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Basic calculator')
    parser.add_argument('op_1', type=int, help='First operator')
    parser.add_argument('op_2', type=int, help='Second operator')
    parser.add_argument('operation', choices=('mul', 'div', 'add', 'sub'))
    main(parser.parse_args())
