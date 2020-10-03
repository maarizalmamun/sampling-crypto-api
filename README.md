# sampling-crypto-api

## Description

This program utilizes the Covalent API to access ticker data of numerous cryptocurrencies to analyze a data corruption error within the API. Ticker data is sampled and the null-errors are summed and graphed on a histogram. 

The program is paired with a test file containing unit tests for all the major functions called in the main program.

[Find the Covalent API Here](https://www.covalenthq.com/docs/api/#get-spot-prices)

The http request is made to:
```console
https://api.covalenthq.com/v1/ticker/
```

## Pre-requisites

THe following external libraries are required for the functionality of this program:
- Matplotlib 3.3.2
- Requests 2.22.0

Additionally virtualenv 20.0.32 was used to create a virtual environment for this project.

## Installation

After opening terminal to project directory install from the virtual environment utilizing the requirements.txt file:
```python
pip install -r requirements.txt
```
Alternatively, matplotlib and requests can also be manually installed locally or globally on users system. It is assumed pip is already installed (If not [access here](https://pip.pypa.io/en/stable/installing/)).
```python
$python -m pip install matplotlib
$python -m pip install requests
```

## Logic 

High level logic overview - An API GET request and data is stored locally into an array. Important data (ticker name and address) field is extracted and stored in a new array keeping track of null_address occurances. Ticker data is sampled once a minute and updates the null_array appropriately. Once 60 samples have been obtained after an hour, the array data is filtered so that only tickers with null addresses detected remains. This filtered data is graphed for further analysis and the termination of this program.

## Relevant Files

- **tickers.py** - The heart of the program.
- **test_tickers.py** - Unit testing for the main program.
- **results/histogram1hr-result.png** - Example output of program from personal test - Histogram outlining frequencies of null address detection
- **results/null-count.txt** -  Example resultant array after filtering for tokens with occurances of a null address. All of these tickers are printed and their count is displayed.

## Citation

THis code was written by Maariz Almamun as an exercise utilizing Covalents API.



