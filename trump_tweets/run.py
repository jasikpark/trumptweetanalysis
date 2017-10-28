import pandas as pd
import numpy as np

df = pd.read_csv("./realdonaldtrump.csv")
df = df[df['source'] == 'Twitter for Android']
df['text'] = [np.nan if y.startswith('"') else y for y in df['text']]
tweets = df['text']
tweets = tweets.dropna(how="any")
tweets.to_csv("./tweets.txt", header=None, index=None, sep=" ")

