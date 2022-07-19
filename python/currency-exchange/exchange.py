def exchange_money(budget, exchange_rate):
    """Translated the amount of foreign money to exchange money"""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """The money taken from the budget"""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Returns the total whole number amount of the bills you have"""
    return number_of_bills * denomination


def get_number_of_bills(budget, denomination):
    """The ammount of set value of whole bills you will get based on the budget you have"""
    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    budget - the money given for trip
    exchange rate - the normal rate money is exchanged for into the new currency
    spread - the percentage taken of the exchange rate as the money given for the company,
    it needs to be divided by 100 to be in a decimal first,
    (and then added onto the normal exchange rate for the total exchange rate with the fee included)
    denomination - the the amount of groups of integers the bills are split into

    This figures out the denomination of exchanged currency with the fee (spread) included.
    """
    total_exchange_rate = exchange_rate + (spread / 100 * exchange_rate)
    value_of_the_new_currency = budget / total_exchange_rate
    number_of_bills = int(value_of_the_new_currency / denomination)
    maximum_value_of_the_new_currency = number_of_bills * denomination
    return maximum_value_of_the_new_currency


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This figures out the exchanged value with the fee but figures out the amount that is lost
    from the original exchanged value with the fee and the one that got the bills split into
    denominations.
    """
    total_exchange_rate = exchange_rate + (spread / 100 * exchange_rate)
    value_of_the_new_currency = budget / total_exchange_rate
    number_of_bills = int(value_of_the_new_currency / denomination)
    maximum_value_of_the_new_currency = number_of_bills * denomination
    non_exchangeable_money = int(
        value_of_the_new_currency - maximum_value_of_the_new_currency
    )
    return non_exchangeable_money
