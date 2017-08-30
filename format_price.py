def format_price(price):
    if type(price) == int:
        return '{0:,}'.format(price).replace(',', ' ')
    else:
        return 'Argument must be integer!'

if __name__ == '__main__':
    pass