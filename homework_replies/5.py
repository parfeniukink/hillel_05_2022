class Price:
    def __init__(self, price: int, currency: str) -> None:
        self.price: int = price
        self.currency: str = currency

    def currency_checker(self, currency: str, other_currency: str):
        if currency == other_currency:
            current_currency = self.currency
        return current_currency

    def __str__(self):
        return f"Data: ({self.price}, {self.currency})"

    def __add__(self, other: "Price") -> "Price":
        current_currency = self.currency_checker(self.currency, other.currency)
        addition = Price(self.price + other.price, currency=current_currency)
        return addition

    def __sub__(self, other: "Price") -> "Price":
        current_currency = self.currency_checker(self.currency, other.currency)
        subtraction = Price(self.price - other.price, currency=current_currency)
        return subtraction


def main():
    rice = Price(100, "UAH")
    # NOTE: Через наступну строку виникне помилка оскільки current_currency буде недоступним
    buckwheat = Price(90, "USD")
    add = rice + buckwheat  # noqa: F841
    sub = rice - buckwheat  # noqa: F841


if __name__ == "__main__":
    main()
