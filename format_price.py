import argparse


def format_price(price):
    try:
        price = int(price)
        return '{0:,}'.format(price).replace(',', ' ')
    except ValueError:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("price", help='Price for formatting')
    args = parser.parse_args()
    print(format_price(args.price))