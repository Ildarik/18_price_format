import argparse


def format_price(price):
    try:
        price = float(price)
        price = '{0:,.2f}'.format(price).replace(',', ' ').replace('.00', '')
    except (ValueError, TypeError):
        raise ValueError('Given value cannot be converted into a number!')
    if price[0] == '-' or price == '0':
        raise ValueError('Price must be greater then 0!')
    return price

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("price", help='Price for formatting')
    args = parser.parse_args()
    print(format_price(args.price))