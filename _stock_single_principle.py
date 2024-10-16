# Model and view
# params()



class StockModel:
    def __init__(self, symbol, open_price, close_price,
                 volume, average_volume):
        self.symbol = symbol
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume
        self.average_volume = average_volume

    def is_bullish(self):
        price_ratio = self.close_price / self.open_price
        volume_ratio = self.volume / self.average_volume
        return price_ratio > 1.02 and volume_ratio > 1.1

class StockView:
    def params(self, model):
        if model.is_bullish():
            sentiment = 'Bullish'
        else:
            sentiment = 'Bearish'
        return {
            'name': model.symbol,
            'price': model.close_price,
            'sentiment': sentiment
        }

    def render(self, model):
        params = self.params(model)
        return '{name}: ${price: 0.2f} ({sentiment})'.format_map(params)

class StockHTMLView(StockView):
    def __init__(self, template):
        self.template = template

    def params(self, model):
        params = super().params(model)
        if model.is_bullish():
            icon = 'buy.jpg'
        else:
            icon = 'sell.jpg'
        params['icon'] = icon
        return params

    def render(self, model):
        params = self.params(model)
        return self.template.format_map(params)
STOCK_HTML_TEMPLATE = '''
<html>
    <title>Stock Report for {name}</title>
    <body>
        <dl><dt>Name:</dt><dd>{name}</dd>
            <dt>Closing price:</dt><dd>{price}</dd>
            <dt>Recommendation:</dt><img src='{icon}'/><dd></dd>
        </dl></body></html>
        '''.strip()
model = StockModel('AAPL', 159.29, 163.05, 44035531, 22509937)
view = StockView()
model1 = StockModel('FB', 172.06, 183.37, 76670183, 25219450)
view = StockHTMLView(STOCK_HTML_TEMPLATE)
print()
print(view.render(model))