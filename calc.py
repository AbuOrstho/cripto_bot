import json

bitmark_prices = json.load(open(r'BitMart\response_1.json', 'r', encoding="UTF-8"))["data"]["tickers"]
coinex_prices = json.load(open(r'Coinex\response_1.json', 'r', encoding="UTF-8"))["data"]["ticker"]
huobi_prices = json.load(open(r'Huobi\response_1.json', 'r', encoding="UTF-8"))["data"]
lbank_prices = json.load(open(r'LBank\response_1.json', 'r', encoding="UTF-8"))["data"]
mexc_prices = json.load(open(r'MEXC\response_1.json', 'r', encoding="UTF-8"))["symbols"]

bitmark_symbols = []
coinex_symbols = list(coinex_prices.keys())
huobi_symbols = []
lbank_symbols = []
mexc_symbols = []

for i in bitmark_prices:
    bitmark_symbols.append(i["symbol"])

for i in huobi_prices:
    huobi_symbols.append(i["symbol"])

for i in lbank_prices:
    lbank_symbols.append(i["symbol"])

for i in mexc_prices:
    mexc_symbols.append(i["symbol"])


print(mexc_symbols)

f = []
coin = ['BTC', 'ETH', 'BNB', 'SOL', 'XRP', 'USDC', 'ADA', 'AVAX', 'LINK', 'DOGE', 'TRX', 'DOT', 'MATIC', 'TON', 'ICP',
        'BCH', 'SHIB', 'DAI', 'LTC', 'IMX', 'UNI', 'LEO', 'ETC', 'ATOM', 'OP', 'NEAR', 'KAS', 'TIA', 'XLM', 'APT',
        'INJ', 'OKB', 'STX', 'FDUSD', 'FIL', 'LDO', 'HBAR', 'ARB', 'VET', 'XMR', 'CRO', 'MNT', 'SUI', 'MKR', 'RUNE',
        'RNDR', 'SEI', 'GRT', 'BSV', 'EGLD', 'BEAM', 'ORDI', 'MINA', 'ALGO', 'AAVE', 'HNT', 'QNT', 'FLOW', 'TUSD',
        'FTM', 'FLR', 'SNX', 'DYM', 'SAND', 'AXS', 'THETA', 'ASTR', 'KCS', 'XTZ', '1000SATS', 'BTT', 'ETHDYDX', 'BGB',
        'MANA', 'CHZ', 'PYTH', 'NEO', 'EOS', 'BLUR', 'CFX', 'BONK', 'ROSE', 'RON', 'OSMO', 'IOTA', 'WEMIX', 'KLAY',
        'KAVA', 'PENDLE', 'AKT', 'WOO', 'USDD', 'MANTA', 'GNO', 'ENS', 'FXS', 'LUNC', 'JUP', 'GALA', 'XEC', 'XDC',
        'AXL', 'CAKE', 'FTT', 'RPL', 'AR', 'CRV', 'NEXO', 'FET', 'APE', 'SC', '1INCH', 'XAUt', 'TWT', 'METIS', 'ZETA',
        'CORE', 'COMP', 'PEPE', 'GMT', 'BTG', 'GT', 'SUPER', 'LUNA', 'NFT', 'ELF', 'ENJ', 'IOTX', 'XRD', 'SKL', 'GMX',
        'PAXG', 'CSPR', 'GAS', 'GELO', 'ALT', 'AGIX', 'DESO', 'ZIL', 'KSM', 'WIF', 'USDP', 'ILV', 'BAT', 'UMA', 'MASK',
        'HOT', 'ZEC', 'ONDO', 'LRC', 'MAGIC', 'SFP', 'NTRN', 'DASH', 'WLD', 'XEM', 'XCH', 'GLMR', 'QTUM', 'API3', 'TRB',
        'CVX', 'SSV', 'ETHW', 'FLOLI', 'TRAC', 'CFG', 'PYUSD', 'KDA', 'XAI', 'JASMY', 'ANT', 'ID', 'RAY', 'TFUEL', 'JST',
        'ZRX', 'MX', 'CHR', 'OCEAN', 'SUSHI', 'BAND', 'RVN', 'STORJ', 'T', 'DCR', 'YFI', 'WAVES', 'PRIME', 'ANKR',
        'GAL', 'MEME', 'BICO', 'RBN', 'CKB', 'JTO', 'OM', 'OAS', 'HT']
x = 0
e = []
for i in coin:
    x += 1
    if i + "USDT" in mexc_symbols:
        f.append(i + "USDT")
    else:
        e.append(f"{x} {i + 'USDT'}")
        print(x+1, f"Пары {i + 'USDT'} нет в mexc")

json_string = json.dumps(f)
print(len(f), json_string)