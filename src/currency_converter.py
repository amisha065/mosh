# exchange_rates - 2D dict (new concep)

def convert(amount, source_currency, target_curreny):
    USD2CAD = 2
    USD2EUR = 3
    
    # This is the main learning in this project (2d dict)
    exchange_rates = {
    'USD' : {'CAD' : USD2CAD, 'EUR' : USD2EUR},
    'CAD' : {'USD' : 1/USD2CAD, 'EUR' : USD2EUR/USD2CAD},
    'EUR' : {'USD' : 1/USD2EUR, 'CAD' : USD2CAD/USD2EUR}}

    if source_currency == target_curreny:
        return amount

    return amount * exchange_rates[source_currency][target_curreny]

 
def enter_amount():
    while True:
        amount = input('Enter the amount: ')
        try:
            number = float(amount)  # Convert input to float
            if number > 0:  # Check if the number is positive
                return number  # Return the positive number
            else:
                raise ValueError()
        except ValueError:
            print("Invalid amount")


def enter_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if currency in currencies:
            return currency
        else:
            print('Invalid currency')

def currency_converter_app():
    amount = enter_amount()
    source_currency = enter_currency('Source')
    target_currency = enter_currency('Target')
    converted_amount =  convert(amount, source_currency,target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount} {target_currency}')


if __name__ == "__main__":
  currency_converter_app()