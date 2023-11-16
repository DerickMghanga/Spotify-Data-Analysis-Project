import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Print the first 5 entries from the csv file
df_tracks = pd.read_csv('C:/Users/HomePC/Downloads/archive/tracks.csv')
# x = df_tracks.head()
# print(x)


# # Check Null values >> check number of entries in each column
# x = pd.isnull(df_tracks).sum()
# print(x)


# # Total number of rows & columns, data types and memory usage by the data set
# x = df_tracks.info()
# print(x)


# # Find 10 least popular songs in the Spotify data set using popularity column
# sorted_df = df_tracks.sort_values("popularity", ascending=True).head(10)
# print(sorted_df)


# # Get descriptive statistics(count, mean, median, standard deviation, min) from the data set
# x = df_tracks.describe().transpose()
# print(x)


# # Get 10 songs with popularity greater value than 90 BUT dont change the data frame
# most_popular = df_tracks.query('popularity>90', inplace=False).sort_values('popularity', ascending=False)
# print(most_popular.head(10))
#  OR 
# print(most_popular[:10])


# # Change index(0 > len) to Release date to be used as indexing
# df_tracks.set_index("release_date", inplace=True)
# df_tracks.index = pd.to_datetime(df_tracks.index)
# print(df_tracks.head())


# # Check artist name on the 18th row from the data set
# y = df_tracks[["artists"]].iloc[18]
# print(y)


# Convert song duration from Milliseconds to seconds
df_tracks["duration"] = df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace=True, axis=1)
print(df_tracks.duration.head())



# Visualization and drop unwanted columns from the data