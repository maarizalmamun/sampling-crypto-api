# sampling-crypto-api

##Description

This program utilizes the Covalent API to access ticker data of numerous cryptocurrencies to analyze a data corruption error within the API. Ticker data is sampled and the null-errors are summed and graphed on a histogram. 

The program is paired with a test file containing unit tests for all the major functions called in the main program.

[Find the Covalent API Here] (https://www.covalenthq.com/docs/api/#get-spot-prices)

The http request is made to:
```console
https://api.covalenthq.com/v1/ticker/
```

##Pre-requisites

THe following external libraries are required for the functionality of this program:
- Matplotlib 3.3.2
- Requests 2.22.0

Additionally virtualenv 20.0.32 was used to create a virtual environment for this project.

##Pre-requisites

After opening terminal to project directory install from the virtual environment utilizing the requirements.txt file:
```python
pip install -r requirements.txt
```
Alternatively, matplotlib and requests can also be manually installed locally or globally on users system. It is assumed pip is already installed (If not [access here](https://pip.pypa.io/en/stable/installing/)).
```console
$python -m pip install matplotlib
$python -m pip install requests
```


