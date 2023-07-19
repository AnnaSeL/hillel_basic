coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def concat(tuple1, tuple2):
    res = dict(zip(tuple1, tuple2))
    print(res)
    return res


concat(coin, code)
