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
    graphForStock = soup.find_all('td', attrs={"aria-label": "Day Chart"})

    dataArray = []
    #Array that processes each value seperately
    for i in range (len(stockNames)):
        stock_name = str(stockNames[i].text)
        stock_price = str(stockPrices[i].text)
        up_down = str(gainOrLoss[i].text)
        acronym = str(stockAcronym[i].text)
        graph = str(graphForStock[i])

        up_down = up_down.replace('+', "")
        stock_name = stock_name.replace(" ", "_")

        dataArray.append([acronym, stock_name, stock_price, up_down, graph])

    return dataArray
