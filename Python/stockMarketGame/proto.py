import numpy as np
# import panda as pd
import yfinance as yf
import plotly.graph_objs as go
import csv
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt

tickList = ["AAPL", "MSFT", "AMZN", "TSLA", "GOOG", "GOOGL", "META", "NVDA", "PEP", "COST", "AVGO", "TMUS", "CSCO",
            "TXN", "QCOM", "ADBE", "CMCSA", "AMGN", "HON", "INTU", "INTC", "PYPL", "NFLX", "SBUX", "ADP", "AMD", "GILD",
            "REGN", "MDLZ", "VRTX", "ADI", "AMAT", "ISRG", "BKNG", "FISV", "MU", "ATVI", "CSX", "KDP", "LRCX", "PANW",
            "CHTR", "MNST", "SNPS", "MRNA", "MAR", "ORLY", "KLAC", "MELI", "CDNS", "ABNB", "AEP", "ADSK", "CTAS",
            "FTNT", "KHC", "DXCM", "NXPI", "PAYX", "BIIB", "ASML", "CRWD", "EXC", "LULU", "MRVL", "MCHP", "EA", "TEAM",
            "AZN", "XEL", "ILMN", "DLTR", "WDAY", "PCAR", "ROST", "CTSH", "PDD", "ODFL", "IDXX", "CEG", "VRSK", "WBA",
            "FAST", "CPRT", "DDOG", "JD", "SGEN", "ZS", "SIRI", "LCID", "BIDU", "EBAY", "ZM", "VRSN", "ANSS", "ALGN",
            "SWKS", "MTCH", "NTES", "SPLK", "DOCU", "OKTA"]

dateNow = datetime.now().date()
date1Month = dateNow - timedelta(weeks=4)
date3Month = dateNow - timedelta(weeks=12)


def date(string):
    return datetime.strptime(string, "%Y-%m-%d").date()


def progress(max, i):
    percent = str(round((100 * i) / max)) + "%"
    fill = "█" * round((32 * i) / max) + "∙" * (32 - round((32 * i) / max))
    print(fill, percent)


def graph(ticker, data):
    x = []
    y = []
    for i in data:
        x.append(abs((date3Month - i[0]).days))
        y.append(i[1])
    plt.figure()
    plt.plot(x, y, color='#000000')
    plt.title(ticker + "Evaluation", color='#ACACAC')
    plt.xlabel("Days", color='#ACACAC')
    plt.ylabel("Close", color='#ACACAC')
    plt.savefig(ticker + ".png")


def test(ticker):
    file = open(ticker + '.csv')
    csvreader = csv.reader(file)
    next(csvreader)  # Avoid header
    data = []
    max3Month = [0, 0]
    max1Month = [0, 0]
    for row in csvreader:
        data.append(row)
        if date(data[len(data) - 1][0]) >= date3Month:
            if float(data[len(data) - 1][5]) > max3Month[1]:
                max3Month[0] = date(data[len(data) - 1][0])
                max3Month[1] = float(data[len(data) - 1][5])
        if date(data[len(data) - 1][0]) >= date1Month:
            if float(data[len(data) - 1][5]) > max1Month[1]:
                max1Month[0] = date(data[len(data) - 1][0])
                max1Month[1] = float(data[len(data) - 1][5])

    currentClose = [date(data[len(data) - 1][0]), float(data[len(data) - 1][5])]
    firstClose = [date(data[0][0]), float(data[0][5])]
    localMin = [0, max1Month[1]]
    for i in data:
        if max1Month[0] <= date(i[0]) <= currentClose[0]:
            if float(i[5]) < localMin[1]:
                localMin[0] = date(i[0])
                localMin[1] = float(i[5])
    localMax = [0, 0]
    for i in data:
        if localMin[0] <= date(i[0]) <= currentClose[0]:
            if float(i[5]) > localMax[1]:
                localMax[0] = date(i[0])
                localMax[1] = float(i[5])
    # print(firstClose)
    # print(max3Month)
    # print(max1Month)
    # print(localMin)
    # print(localMax)
    # print(currentClose)

    # graph(ticker, [firstClose, max3Month, max1Month, localMin, localMax, currentClose])

    if max3Month != max1Month:
        return False
    if max1Month == currentClose:
        return False
    if abs((localMin[0] - currentClose[0]).days) > 10:
        return False
    if abs((localMax[0] - currentClose[0]).days) > 3:
        return False
    return True


def figure(ticker, data):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name="Market Data"))

    fig.update_layout(
        title=ticker,
        yaxis_title="Stock Price USD"
    )

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1mo", step="month", stepmode="backward"),
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=1, label="HTD", step="minute", stepmode="todate"),
                dict(count=1, label="2h", step="minute", stepmode="backward"),
                dict(step="all"),
            ])
        )
    )

    fig.write_html(ticker + ".html")


buy = []
for i in tickList:
    data = yf.download(tickers=i, period='3mo', interval='1d')
    data.to_csv(i + ".csv")

    # figure(i, data)

    if test(i):
        buy.append(i)
        print("BUY " + i)

    progress(len(tickList), tickList.index(i))

print(buy)
