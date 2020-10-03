import unittest
import tickers

class TestMain(unittest.TestCase):

    """
    The following 5 sample data points are utilized for testing general cases of functionality:
    ticker_valtest1 (original ticker values from API at time 0)
    ticker_valtest2 (new ticker values from API at time of next sampling)
    null_valtest1 (original null_array after initialization from ticker_valtest1)
    null_valtest2 (new ticker values after update from ticker_valtest2)
    filtered_valtest (obtained after filtering function on null_valtest3)
    """
    def setUp(self):
        self.ticker_valtest1 = [
            {'ticker_symbol': 'BTC', 'quote_rate': 10531.22, 'decimals': 8, 'address': '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599', 'name': 'Wrapper BTC', 'logo_url': 'https://logos.covalenthq.com/tokens/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599.png'},
            {'ticker_symbol': 'ETH', 'quote_rate': 346.11, 'decimals': 18, 'address': None, 'name': 'Ether', 'logo_url': 'https://logos.covalenthq.com/tokens/0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.png'},
            {'ticker_symbol': 'USDT', 'quote_rate': 1.0, 'decimals': 6, 'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'name': 'Tether USD', 'logo_url': 'https://logos.covalenthq.com/tokens/0xdac17f958d2ee523a2206206994597c13d831ec7.png'},
            {'ticker_symbol': 'XRP', 'quote_rate': 0.233056, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'BCH', 'quote_rate': 218.42, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'BNB', 'quote_rate': 27.14, 'decimals': 18, 'address': '0xb8c77482e45f1f44de1745f52c74426c631bdd52', 'name': 'Binance', 'logo_url': 'https://logos.covalenthq.com/tokens/0xb8c77482e45f1f44de1745f52c74426c631bdd52.png'},
            {'ticker_symbol': 'DOT', 'quote_rate': 4.1, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'LINK', 'quote_rate': 9.23, 'decimals': 18, 'address': '0x514910771af9ca656af840dff83e8264ecf986ca', 'name': 'ChainLink Token', 'logo_url': 'https://logos.covalenthq.com/tokens/0x514910771af9ca656af840dff83e8264ecf986ca.png'},
            {'ticker_symbol': 'CRO', 'quote_rate': 0.146772, 'decimals': 8, 'address': '0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b', 'name': 'CRO', 'logo_url': 'https://logos.covalenthq.com/tokens/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b.png'},
            {'ticker_symbol': 'BSV', 'quote_rate': 160.19, 'decimals': None, 'address': None, 'name': None, 'logo_url': None}, 
            {'ticker_symbol': 'LTC', 'quote_rate': 44.95, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'ADA', 'quote_rate': 0.094014, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'USDC', 'quote_rate': 1.0, 'decimals': 6, 'address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'name': 'USD//C', 'logo_url': 'https://logos.covalenthq.com/tokens/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png'},
            {'ticker_symbol': 'EOS', 'quote_rate': 2.47, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'TRX', 'quote_rate': 0.02599483, 'decimals': None, 'address': None, 'name': None, 'logo_url': None}
        ]
        self.ticker_valtest2 = [
            {'ticker_symbol': 'BTC', 'quote_rate': 10531.22, 'decimals': 8, 'address': None, 'name': 'Wrapper BTC', 'logo_url': 'https://logos.covalenthq.com/tokens/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599.png'},
            {'ticker_symbol': 'ETH', 'quote_rate': 346.11, 'decimals': 18, 'address': None, 'name': 'Ether', 'logo_url': 'https://logos.covalenthq.com/tokens/0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.png'},
            {'ticker_symbol': 'USDT', 'quote_rate': 1.0, 'decimals': 6, 'address': None, 'name': 'Tether USD', 'logo_url': 'https://logos.covalenthq.com/tokens/0xdac17f958d2ee523a2206206994597c13d831ec7.png'},
            {'ticker_symbol': 'XRP', 'quote_rate': 0.233056, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'BCH', 'quote_rate': 218.42, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'BNB', 'quote_rate': 27.14, 'decimals': 18, 'address': None, 'name': 'Binance', 'logo_url': 'https://logos.covalenthq.com/tokens/0xb8c77482e45f1f44de1745f52c74426c631bdd52.png'},
            {'ticker_symbol': 'DOT', 'quote_rate': 4.1, 'decimals': None, 'address': None, 'name': None, 'logo_url': None},
            {'ticker_symbol': 'LINK', 'quote_rate': 9.23, 'decimals': 18, 'address': None, 'name': 'ChainLink Token', 'logo_url': 'https://logos.covalenthq.com/tokens/0x514910771af9ca656af840dff83e8264ecf986ca.png'},
            {'ticker_symbol': 'CRO', 'quote_rate': 0.146772, 'decimals': 8, 'address': None, 'name': 'CRO', 'logo_url': 'https://logos.covalenthq.com/tokens/0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b.png'},
            {'ticker_symbol': 'BSV', 'quote_rate': 160.19, 'decimals': None, 'address': None, 'name': None, 'logo_url': None}, 
            {'ticker_symbol': 'LTC', 'quote_rate': 44.95, 'decimals': None, 'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'name': None, 'logo_url': None},
            {'ticker_symbol': 'ADA', 'quote_rate': 0.094014, 'decimals': None, 'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'name': None, 'logo_url': None},
            {'ticker_symbol': 'USDC', 'quote_rate': 1.0, 'decimals': 6, 'address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'name': 'USD//C', 'logo_url': 'https://logos.covalenthq.com/tokens/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png'},
            {'ticker_symbol': 'EOS', 'quote_rate': 2.47, 'decimals': None, 'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'name': None, 'logo_url': None},
            {'ticker_symbol': 'TRX', 'quote_rate': 0.02599483, 'decimals': None, 'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'name': None, 'logo_url': None}
        ]
        self.null_valtest1 = [
            {'ticker_symbol': 'BTC', 'null_count': 0}, 
            {'ticker_symbol': 'ETH', 'null_count': 1}, 
            {'ticker_symbol': 'USDT', 'null_count': 0}, 
            {'ticker_symbol': 'XRP', 'null_count': 1}, 
            {'ticker_symbol': 'BCH', 'null_count': 1}, 
            {'ticker_symbol': 'BNB', 'null_count': 0}, 
            {'ticker_symbol': 'DOT', 'null_count': 1}, 
            {'ticker_symbol': 'LINK', 'null_count': 0}, 
            {'ticker_symbol': 'CRO', 'null_count': 0}, 
            {'ticker_symbol': 'BSV', 'null_count': 1}, 
            {'ticker_symbol': 'LTC', 'null_count': 1}, 
            {'ticker_symbol': 'ADA', 'null_count': 1}, 
            {'ticker_symbol': 'USDC', 'null_count': 0}, 
            {'ticker_symbol': 'EOS', 'null_count': 1}, 
            {'ticker_symbol': 'TRX', 'null_count': 1}
        ]
        self.null_valtest2 = [
            {'ticker_symbol': 'BTC', 'null_count': 1}, 
            {'ticker_symbol': 'ETH', 'null_count': 2}, 
            {'ticker_symbol': 'USDT', 'null_count': 1}, 
            {'ticker_symbol': 'XRP', 'null_count': 2}, 
            {'ticker_symbol': 'BCH', 'null_count': 2}, 
            {'ticker_symbol': 'BNB', 'null_count': 1}, 
            {'ticker_symbol': 'DOT', 'null_count': 2}, 
            {'ticker_symbol': 'LINK', 'null_count': 1}, 
            {'ticker_symbol': 'CRO', 'null_count': 1}, 
            {'ticker_symbol': 'BSV', 'null_count': 2}, 
            {'ticker_symbol': 'LTC', 'null_count': 1}, 
            {'ticker_symbol': 'ADA', 'null_count': 1}, 
            {'ticker_symbol': 'USDC', 'null_count': 0}, 
            {'ticker_symbol': 'EOS', 'null_count': 1}, 
            {'ticker_symbol': 'TRX', 'null_count': 1}
        ]
        self.filtered_valtest = [
            ['BTC', 'ETH', 'USDT', 'XRP', 'BCH', 'BNB', 'DOT', 'LINK', 'CRO'],
            [60, 60, 60, 60, 60, 10, 2, 40, 30]
        ]

    #Test to ensure returned result is a list
    #Test to ensure list compromised of dictionaries
    #Test to ensure dictionary parameters match expected parameters
    def test_getAPI(self):
        result = tickers.getAPI()
        resultKeys = ['ticker_symbol', 'quote_rate', 'decimals', 'address', 'name', 'logo_url']
        self.assertNotEqual("Bad Response",result)
        self.assertIs(list,type(result))
        self.assertIs(dict,type(result[0]))
        self.assertEqual(resultKeys,list(result[0].keys()))        

    #Test: Create Null Array and populate appropriately
    def test_createNullArray(self):
        null_array = tickers.createNullArray(self.ticker_valtest1)
        resultKeys = ["ticker_symbol", "null_count"]

        self.assertIs(dict,type(null_array[0])) #List elements are dictionary
        self.assertEqual(resultKeys,list(null_array[0].keys())) #List element keys match
      
        self.assertEqual(null_array[0]["null_count"],0) #Case: address null > Initialize 0
        self.assertEqual(null_array[1]["null_count"],1) #Case: address notnull > Initialize 1
        self.assertEqual(null_array, self.null_valtest1)

    def test_updateNullAddressCount(self):
        new_null_array = tickers.updateNullAddressCount(self.null_valtest1, self.ticker_valtest2) 
        self.assertEqual(new_null_array,self.null_valtest2) #Check if adding works appropriately assuming input is correct format

    def test_waitAnHour(self):
        null_array = tickers.waitAnHour(1,10) #For sake of testing, ten samples sampled at 1Hz is utilized
        max_frequency = 0
        for elements in null_array:
            if(elements["null_count"] > max_frequency):
                max_frequency = elements["null_count"]
        self.assertIs(list,type(null_array)) #Test for successful return
        self.assertTrue(max_frequency <= 60) #Sanity check

    def test_filteredArray(self):
        null_valtest3 = [
            {'ticker_symbol': 'BTC', 'null_count': 60}, 
            {'ticker_symbol': 'ETH', 'null_count': 60}, 
            {'ticker_symbol': 'USDT', 'null_count': 60}, 
            {'ticker_symbol': 'XRP', 'null_count': 60}, 
            {'ticker_symbol': 'BCH', 'null_count': 60}, 
            {'ticker_symbol': 'BNB', 'null_count': 10}, 
            {'ticker_symbol': 'DOT', 'null_count': 2}, 
            {'ticker_symbol': 'LINK', 'null_count': 40}, 
            {'ticker_symbol': 'CRO', 'null_count': 30}, 
            {'ticker_symbol': 'BSV', 'null_count': 0}, 
            {'ticker_symbol': 'LTC', 'null_count': 0}, 
            {'ticker_symbol': 'ADA', 'null_count': 0}, 
            {'ticker_symbol': 'USDC', 'null_count': 0}, 
            {'ticker_symbol': 'EOS', 'null_count': 0}, 
            {'ticker_symbol': 'TRX', 'null_count': 0}
        ]
        filtered_array = tickers.filteredArray(null_valtest3)
        zero = False
        for element in filtered_array[1]:
            if(element==0):
                zero = True
                break
        self.assertFalse(zero) #Check if all 0 valued tickers have been removed
        self.assertEqual(filtered_array,self.filtered_valtest) #Ensure function retrieves expected result

if __name__ == '__main__':
    unittest.main()