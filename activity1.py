from os import stat
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()
def random_set_of_means(counter): 
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data [random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range (0,1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)
mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print ("Mean of Sampling Distribution is ", mean)
print ("Standard Deviation of Sampling Distribution is ", std_deviation)
df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print ("Mean of Sample 1 is ", mean_of_sample1)
df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print ("Mean of Sample 2 is ", mean_of_sample2)
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print ("Mean of Sample 3 is ", mean_of_sample3)
z_score1 = (mean-mean_of_sample1)/std_deviation
print ("z score of sample1 is ", z_score1)
z_score2 = (mean-mean_of_sample2)/std_deviation
print ("z score of sample2 is ", z_score2)
z_score3 = (mean-mean_of_sample3)/std_deviation
print ("z score of sample3 is ", z_score3)
