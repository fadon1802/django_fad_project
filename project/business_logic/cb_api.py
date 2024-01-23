import requests
import dateutil.parser
import xml.etree.ElementTree as ET


def get_currency_coeff_rur(currency: str, published_at: str):
    if currency == "RUR":
        return 1.0

    datetime = dateutil.parser.isoparse(published_at)
    year = datetime.year
    month = datetime.month

    if (year < 2023 or year == 2023 and month == 1) and currency == "GEL":
        year = 2023
        month = 2

    if (year == 2016 and month <= 6 or year < 2016) and currency == "BYN":
        currency = "BYR"

    if (year == 2016 and month > 6 or year >= 2017) and currency == "BYR":
        currency = "BYN"

    if year not in currencies_by_date:
        currencies_by_date[year] = {
            month: {
                currency: get_currency_coeff_from_cb(currency, month, year)
            }
        }
    if month not in currencies_by_date[year]:
        currencies_by_date[year][month] = {
            currency: get_currency_coeff_from_cb(currency, month, year)
        }
    if currency not in currencies_by_date[year][month]:
        currencies_by_date[year][month][currency] = get_currency_coeff_from_cb(currency, month, year)

    return currencies_by_date[year][month][currency]


def get_currency_coeff_from_cb(currency: str, month: int, year: int):
    if month < 10:
        month = f"0{str(month)}"
    date = f"01/{month}/{year}"
    response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        valute = root.find(f".//Valute[CharCode='{currency}']")

        if valute is not None:
            multiplier = valute.find('VunitRate').text
            multiplier_float = float(multiplier.replace(",", "."))
            return multiplier_float


currencies_by_date = {}
