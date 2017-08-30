import argparse


def format_price(price):
    if type(price) == int:
        return '{0:,}'.format(price).replace(',', ' ')
    else:
        return 'Argument must be integer!'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=int, help='Price for formatting')
    args = parser.parse_args()
    print(format_price(args.price))