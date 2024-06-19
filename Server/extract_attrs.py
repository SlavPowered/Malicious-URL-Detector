import urllib.parse
import ipaddress
import pandas as pd

feature_names = ['url_length', 'domain_length', 'has_https','parameter_count',
     'letter_count', 'nb_count', 'non_alpha_count', 'ques', 'slashes',
     'dashes', 'underscores', 'dots', 'has_php', 'has_html']

def check_ipv4(url: urllib.parse.ParseResult):
    hostname = url.hostname
    if hostname:
        try:
            ip_address = ipaddress.ip_address(hostname)
            if ip_address.version == 4:
                return 1
        except:
            return 0

def count_symbols(url: str) -> tuple:
    letters = 0
    numbers = 0
    non_alpha_numeric = 0
    for char in url:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1
        else:
            non_alpha_numeric += 1
    return letters, numbers, non_alpha_numeric

def count_parameters(url: urllib.parse.ParseResult):
    parameters = url.query.split("&")
    return len(parameters)

def count_chars(url: str) -> tuple:
    ques = 0
    slashes = 0
    dashes = 0
    underscores = 0
    dots = 0
    for char in url:
        if char == "?":
            ques += 1
        elif char == "/":
            slashes += 1
        elif char == ".":
            dots += 1
        elif char == "-":
            dashes += 1
        elif char == "_":
            underscores += 1
    return ques, slashes, dashes, underscores, dots

def get_attributes(url: str, preprocess: bool):
    parsed_url = urllib.parse.urlparse(url)
    new_data = pd.DataFrame()
    url_length = len(url)
    domain_length = len(parsed_url.netloc)

    letter_count, nb_count, non_alpha_count = count_symbols(url)
    ques, slashes, dashes, underscores, dots = count_chars(url)

    has_php = 1 if "php" in url else 0 
    has_html = 1 if "html" in url else 0  
    has_https = 1 if"https" in url else 0
    parameter_count = count_parameters(parsed_url)
    
    if preprocess:
        has_ipv4 = check_ipv4(parsed_url)
        return [url_length, domain_length, has_https,has_ipv4,parameter_count,
            letter_count, nb_count, non_alpha_count, ques, slashes,
            dashes, underscores, dots, has_php, has_html]

    return [url_length, domain_length, has_https,parameter_count,
            letter_count, nb_count, non_alpha_count, ques, slashes,
            dashes, underscores, dots, has_php, has_html]