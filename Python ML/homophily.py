import networkx as nx
import pandas as pd
import numpy as np

def marginal_prob(ind_chars):
    char_list = list(ind_chars.values())
    total = len(char_list)
    
    char_freq = {}
    for char in set(char_list):
        char_freq[char] = char_list.count(char) / total
    return char_freq

def chance_homophily(ind_chars):
    frequencies = list(marginal_prob(ind_chars).values())
    homophily = np.sum(np.square(frequencies))
    return homophily

#def chance_homophily(ind_chars):
    
    
data = pd.read_csv('C:\\Users\\mishal\\Desktop\\individual characteristics.csv')

village1_data = pd.DataFrame(data[data.village==1])
village2_data = pd.DataFrame(data[data.village==2])

def df_to_dict(dataframe, keys, values):
    df = pd.DataFrame()
    df[keys] = dataframe[keys]
    df[values] = dataframe[values]
    return dict(df.values)
    

vil1_sex = df_to_dict(village1_data,'pid','resp_gend')
vil2_sex = df_to_dict(village2_data,'pid','resp_gend')
vil1_religion = df_to_dict(village1_data,'pid','religion')
vil2_religion = df_to_dict(village2_data,'pid','religion')
vil1_caste = df_to_dict(village1_data,'pid','caste')
vil2_caste = df_to_dict(village2_data,'pid','caste')

ch_sex1 = chance_homophily(vil1_sex)
ch_sex2 = chance_homophily(vil2_sex)
ch_religion1 = chance_homophily(vil1_religion)
ch_religion2 = chance_homophily(vil2_religion)
ch_caste1 = chance_homophily(vil1_caste)
ch_caste2 = chance_homophily(vil2_caste)

def homophily(G, chars, node_IDs):
    num_of_ties = 0
    num_of_same_ties = 0
    
    for n1,n2 in G.edges():
        if node_IDs[n1] in chars and node_IDs[n2] in chars:
            num_of_ties += 1
            if chars[node_IDs[n1]]==chars[node_IDs[n2]]:
                num_of_same_ties += 1
    return (num_of_same_ties/num_of_ties)

A1 = np.array(pd.read_csv('C:\\Users\\mishal\\Desktop\\village_relationships1.csv', index_col=0))            
A2 = np.array(pd.read_csv('C:\\Users\\mishal\\Desktop\\village_relationships2.csv', index_col=0))         
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = pd.read_csv('C:\\Users\\mishal\\Desktop\\pid village1.csv')['0'].to_dict()
pid2 = pd.read_csv('C:\\Users\\mishal\\Desktop\\pid village2.csv')['0'].to_dict()

print(homophily(G1, vil1_caste, pid1))
