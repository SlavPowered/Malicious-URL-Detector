import pandas as pd
import extract_attrs

data = pd.read_csv('./urldata.csv')
new = pd.DataFrame()
new[['url_length', 'domain_length', 'has_https','has_ipv4', 'parameter_count',
     'letter_count', 'nb_count', 'non_alpha_count', 'ques', 'slashes',
     'dashes', 'underscores', 'dots', 'has_php', 'has_html']] = data['url'].apply(lambda x: pd.Series(extract_attrs.get_attributes(x, True)))

new['result'] = data['result']
new.to_csv("./prepareddata2.csv")
