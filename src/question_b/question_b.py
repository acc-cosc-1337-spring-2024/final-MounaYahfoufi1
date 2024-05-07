#write functions here, don't add input('') statements here!
# stocks.py
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stock_list = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft")
    }
    
    print("Stock Purchase History:")
    print("{:<10} {:<15}".format("Symbol", "Company Name"))
    for symbol, stock in stock_list.items():
        print("{:<10} {:<15}".format(stock.get_symbol(), stock.get_company_name()))
