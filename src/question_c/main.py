#add import

from question_c import Stock

def main():
    # Create instances of Stock class for each stock
    aapl = Stock("AAPL", "Apple Inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")
    
    # Display symbol and company name for each stock
    print("Stock Report")
    print("{:<15} {}".format("Company", "Symbol"))
    print("{:<15} {}".format(aapl.get_company_name(), aapl.get_symbol()))
    print("{:<15} {}".format(cat.get_company_name(), cat.get_symbol()))
    print("{:<15} {}".format(ek.get_company_name(), ek.get_symbol()))
    print("{:<15} {}".format(goog.get_company_name(), goog.get_symbol()))
    print("{:<15} {}".format(msft.get_company_name(), msft.get_symbol()))

if __name__ == "__main__":
    main()
