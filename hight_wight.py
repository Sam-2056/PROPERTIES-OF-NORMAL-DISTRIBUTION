import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv

df = pd.read_csv("height-weight.csv")

height = df["Height(Inches)"].to_list()
weight = df["Weight(Pounds)"].to_list()

h_mean = statistics.mean(height)
w_mean = statistics.mean(weight)
h_median = statistics.median(height)
w_median = statistics.median(weight)
h_mode = statistics.mode(height)
w_mode = statistics.mode(weight)
h_stdev = statistics.stdev(height)
w_stdev = statistics.stdev(weight)

#fig = ff.create_distplot([height], ["Result"], show_hist=False)

first_std_deviation_start, first_std_deviation_end = h_mean-h_stdev, h_mean+h_stdev
second_std_deviation_start, second_std_deviation_end = h_mean-(2*h_stdev), h_mean+(2*h_stdev)
third_std_deviation_start, third_std_deviation_end = h_mean-(3*h_stdev), h_mean+(3*h_stdev)

#fig = ff.create_distplot([weight], ["Result"], show_hist=False)

###

#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

#fig.show()

list_of_data_within_1_std_deviation = [result for result in height if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in height if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in height if result > third_std_deviation_start and result < third_std_deviation_end]

print("height mean: ", h_mean)
print("weight mean: ", w_mean)
print("height median: ", h_median)
print("weight median: ", w_median)
print("height mode: ", h_mode)
print("weight mode: ", w_mode)
print("height stdev: ", h_stdev)
print("weight stdev: ", w_stdev)

print(" ")

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(height)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(height)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(height)))