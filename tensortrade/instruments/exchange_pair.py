
import math

from tensortrade.instruments.quantity import precise


class ExchangePair:
    """A pair of financial instruments to be traded on a specific exchange."""

    def __init__(self, exchange: 'Exchange', pair: 'TradingPair'):
        self._exchange = exchange
        self._pair = pair

    @property
    def exchange(self) -> 'Exchange':
        return self._exchange

    @property
    def pair(self) -> 'TradingPair':
        return self._pair

    @property
    def price(self) -> float:
        price = self.exchange.quote_price(self.pair)
        # return precise(price, self.pair.base.precision)
        return price

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, ExchangePair):
            if str(self) == str(other):
                return True
        return False

    def __str__(self):
        return "{}:{}".format(self.exchange.name, self.pair)

    def __repr__(self):
        return str(self)