import argparse
import sys
import requests
import json
import csv
from datetime import datetime, timedelta
from tabulate import tabulate


def get_exchange_rate(date, from_currency, to_currency, amount):
    """Get exchange data from the web page"""
    API_URL = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "date": date,
    }
    data = requests.get(API_URL, params=params).json()
    return data["date"], data["info"]["rate"], data["result"]


def validate_currency(currency_from, currency_to):
    """Check the given currency with currency from symbols.json"""
    with open("symbols.json", "r") as symbols_file:
        symbols_data = json.load(symbols_file)
    if currency_from not in symbols_data["symbols"] or currency_to not in symbols_data["symbols"]:
        print("Invalid currency codes.")
        sys.exit()
    else:
        return symbols_data


def main():
    """Define the parameters for cmd"""
    parser = argparse.ArgumentParser(description="Online Currency Converter")
    parser.add_argument("currency_from", type=str, default="USD", help="Source currency")
    parser.add_argument("currency_to", type=str, default="UAH", help="Target currency")
    parser.add_argument("amount", type=float, default=100.00, help="Amount to convert")
    parser.add_argument("--start_date", type=str, default=datetime.now().strftime("%Y-%m-%d"),
                        help="Start date for conversion (format: YYYY-MM-DD)")
    parser.add_argument("--save_to_file", action="store_true", help="Save results to a CSV file")

    args = parser.parse_args()

    validate_currency(args.currency_from, args.currency_to)

    """Checking the correctness of the date"""
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    current_date = datetime.now()
    if start_date > current_date:
        start_date = current_date

    results = []
    columns = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    names = ['date', 'from', 'to', 'amount', 'rate', 'result']
    while start_date <= current_date:
        converted_date = start_date.strftime("%Y-%m-%d")
        date, rate, result = get_exchange_rate(converted_date, args.currency_from, args.currency_to, args.amount)
        results.append([date, args.currency_from, args.currency_to, args.amount, rate, result])
        start_date += timedelta(days=1)

    """Saving data to csv file or printing"""
    if args.save_to_file:
        with open("exchange_rates.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(columns)
            csv_writer.writerows(results)
            print("Data saved to exchange_rates.csv")
    else:
        print(tabulate(results, headers=names))


if __name__ == "__main__":
    main()





























