import yfinance as yf
import pandas as pd

class Stocks():
    def __init__(self):
        self.returnData()

    def getTickers(self):
        tickersList = [
                    "AAPL", "MSFT", "NVDA", "GOOGL", "GOOG", "MMM", "AOS", "ABT", "ABBV", "ACN", "ATVI", "ADM",
                    "ADBE", "ADP", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL",
                    "GOOGL", "GOOG", "AMZN", "AMCR", "AMD", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME",
                    "AMGN", "APH", "ADI", "ANSS", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG", "AIZ", "T", "ATO",
                    "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BALL", "BAC", "BBWI", "BAX", "BDX", "WRB", "BRK.B", "BBY",
                    "BIO", "TECH", "BIIB", "BK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BRO", "BF.B", 
                    "CHRW", "CDNS", "CZR", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE",
                    "CDW", "CE", "CNC", "CNP", "CDAY", "CF", "CRL", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", 
                    "CINF", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", 
                    "CAG", "COP", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CTRA", "CCI", "CSX", "CMI",
                    "CVS", "DHI", "DHR", "DRH", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLTR", "D",
                    "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD", "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX",
                    "EW", "EA", "ELV", "ETR", "EOG", "EPAM", "EQIX", "EQT", "EF", "ESS", "EL", "ETSY", "RE",
                    "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FDS", "FAST", "FRT", 
                    "FITB", "FRC", "FE", "FIS", "FISV", "FLT", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA",
                    "FOX", "BEN", "FCX", "GRMN", "IT", "GE", "GNRC", "GD", "GEHC", "GIS", "GM", "GPC", "GILD",
                    "GL", "GPN", "GS", "HAL", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE",
                    "HL", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUM", "HBAN", "HII",
                    "IBM", "IEX", "IDXX", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IP",
                    "IPG", "IFF", "INTU", "ISRG", "IVZ", "INVH", "IQV", "IRM", "JKHY", 
                    "J", "JBHT", "JNJ", "JCI", "JPM", "JNPR", "K", "KDP", "KEY", "KEYS", 
                    "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW",
                    "LVS", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ", "LMT", "L",
                    "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "ML",
                    "MAS", "MA", "MTCH", "MKC", "MCD", "MCK", "MDT", "MRK", "META", "MET", 
                    "MTD", "MGM", "MCHP", "MU", "MSFT", "MA", "MAA", "MRNA", "MHK", "TAP", 
                    "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI", "MS", "MSCI", "NDAQ", 
                    "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NDSN",
                    "NSC", "NTRS", "NOC", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", 
                    "ODFL", "OMC", "ON", "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PAR", "PAYX", 
                    "PAYC", "PYPL", "PNR", "PBCT", "PEP", "PKI", "PFE", "PM", "PNW", "PXD", 
                    "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PSA",
                    "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG",
                    "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM",
                    "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SBNY", "SPG", "SWKS", "SJM", "SNA", 
                    "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK", "SIVB", "SYF", "SNPS", "SYY", "TMUS", "TROW", 
                    "TTWO", "TPR", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "T",
                    "DG", "TRV", "TRMB", "TFC", "TWTR", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UPS", "URI", 
                    "UNH", "UHS", "VLO", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VFC", "VTRS", "VICI", "V", "VNO", "VMC", "WRB",
                    "WAB", "WBA", "WMT", "WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU", "WRK", "WY", "WHR", "WMB",
                    "WTW", "WYNN", "XEL", "XYL", "YUM", "ZBRA", "ZBH", "ZION"]
        return tickersList
    
    def returnData(self):
        data = []

        for ticker in self.getTickers():
            stock = yf.Ticker(ticker)
            info = stock.info
            pe_ratio = info.get('trailingPE') if info else None
            data.append({'Ticker': ticker, 'P/E Ratio': pe_ratio})

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="P/E Ratio", na_position='last')  # Sort by P/E Ratio, placing NaNs at the end
        df_sorted.to_excel('sp500_pe_ratios.xlsx', index=False)

Stocks()
