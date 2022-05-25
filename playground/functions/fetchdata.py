def getData():
    import requests
    from bs4 import BeautifulSoup

    url = "https://finance.yahoo.com/trending-tickers"
    response = requests.get(url)

    #This will extract the data that we need
    soup = BeautifulSoup(response.text, 'html.parser')
    stockNames = soup.find_all('td', attrs={"aria-label": "Name"})
    stockPrices = soup.find_all('td', attrs={"aria-label": "Last Price"})
    gainOrLoss = soup.find_all('td', attrs={"aria-label": "Change"})
    stockAcronym = soup.find_all('td', attrs={"aria-label": "Symbol"})

    dataArray = []
    #Array that processes each value seperately
    for i in range (len(stockNames)):
        stock_name = str(stockNames[i].text)
        stock_price = str(stockPrices[i].text)
        up_down = str(gainOrLoss[i].text)
        acronym = str(stockAcronym[i].text)

        dataArray.append([acronym, stock_name.replace("_", " "), stock_price, float(up_down)])

    dataArray = sorted(dataArray,key=lambda x: x[3], reverse=True)
    return dataArray
