"""
Coded solely by: Maariz Almamun
No templates were followed in the creation of this software

HIGH LEVEL OVERVIEW OF CODE LOGIC
1. waitAnHour() executes through several function calls: it initializes GET from API and stores data
2. Data transferred to a null_array, extracting important data (ticker_symbol and null address frequency) and storing locally in an array
3. This sampling and updating of null_array occurs at a sampling rate of 60s for 60 times.. totalling 1hour
   Result is array with count of null addresses of every ticker through 1 hour 
4. Tickers without occurances removed and array reformatted via filteredArray(null_array)
5. filteredArray passed to displayHist() and the data is graphed on a histogram!
"""

import requests
import time
from matplotlib import pyplot as plt

print("Program beginning - standby")
key = "ckey_be61e76bc0dd4012890ecdc3564"
url = "https://api.covalenthq.com/v1/ticker/"
sample_rate = 60 #In seconds
sample_quantity = 60 #Total samples taken

def main():
    null_array = waitAnHour(sample_rate, sample_quantity)   #Sample once per minute for an hour to obtain the null address frequencies of each ticker
    corrupted_tickers = filteredArray(null_array)           #Filter out tickers without any null addresses
    printFilteredArray(corrupted_tickers)           
    displayHist(corrupted_tickers)
    return

#GET API data and return JSON object's "ticker" key value pair containing all ticker data
def getAPI():
    req = requests.get(url + "?key=" + key)
    if req.ok:
        return req.json()['data']['ticker']
    else:
        return 'Bad Response'

#Generate null_array by iterating through every ticker in dataset and initializing count to 0 or 1 if currently null
def createNullArray(ticker_data):
    null_array = []
    for ticker in ticker_data:
        if ticker['address'] == None:
            null_array.append({"ticker_symbol": ticker["ticker_symbol"], "null_count": 1} )
        else:
            null_array.append({"ticker_symbol": ticker["ticker_symbol"], "null_count": 0} )
    return null_array

#Iterates through the ticker_data array and increments null addresses counter
def updateNullAddressCount(null_array, ticker_data):
    for i in range(len(ticker_data)):
        if(ticker_data[i]["address"] == None):
            null_array[i]["null_count"]+=1
    return null_array

#Collect and Record Null Address Data once a minute x60
def waitAnHour(sample_rate, sample_quantity):
    ticker_data = getAPI()
    null_array = createNullArray(ticker_data)   #Initialize null array for first time
    iterations = 1
    while(iterations < sample_quantity):                     #Total 60 samples collected in 60min
        time.sleep(sample_rate)                           #Wait for 60seconds before resampling data from API
        print("Time elapsed: %d minutes" %iterations)
        ticker_data = getAPI()                  #Repeatedly get data from API and updateNullAddressCount
        null_array = updateNullAddressCount(null_array, ticker_data)
        iterations += 1
    #printNullArray(null_array)
    return null_array

def filteredArray(null_array):
    filtered_array = [[],[]]
    for nullElement in null_array:
        if(nullElement['null_count']> 0):
            filtered_array[0].append(nullElement['ticker_symbol'])
            filtered_array[1].append(nullElement['null_count'])
    return filtered_array

def displayHist(corrupt_ticker):
    bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    plt.hist(corrupt_ticker[1], bins, histtype="bar", edgecolor='black')    
    plt.xlabel("Null Frequency")
    plt.ylabel("# of Tickers")
    plt.title("Histogram of Null Address Frequencies")
    plt.show()

#Print All Tickers neatly formatted with relevant data aka symbol, price, and address (debugging)
def printTickers(ticker_data):
    for entry in ticker_data:
        print("%s Price: %f Address: %s" %(entry['ticker_symbol'],entry['quote_rate'],entry['address']))

#Print null array and current count of null addresses of each ticker
def printNullArray(null_array):
    for nullElement in null_array:
        print("%s Null Count: %d"%(nullElement["ticker_symbol"],nullElement["null_count"]))

#Print array of potentially corrupted tickers and the frequency of their null addresses
def printFilteredArray(filtered_array):
    for i in range(len(filtered_array[0])):
        print("%s Null Count: %d"%(filtered_array[0][i], filtered_array[1][i]))

if __name__ == "__main__":
    main()