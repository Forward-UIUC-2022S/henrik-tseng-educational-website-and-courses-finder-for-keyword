import sys
sys.path.append(r"E:\Learning\undergraduate\2021 Fall\CS397\Educational-website-and-courses-finder-for-keyword\code")
#from code import webpage_crawler, rf_classifier
#import webpage_crawler, rf_classifier
import urllib.request
import urllib.parse
from googlesearch import search
from bs4 import BeautifulSoup
from random import randint
# import time
# import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
# import itertools

import sys
import numpy
# import modify_data
# import rf_classifier
import webpage_crawler

numpy.set_printoptions(threshold=sys.maxsize)

input_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling_modified.xlsx"
input_sheet = "Sheet1"
output_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling_modified_out.xlsx"
output_sheet = "output_sheet"

# running on modified data
#modify_data.add_sum(input_path,input_sheet,output_path,output_sheet)



# # default_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
# #                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

# # user_header = default_header
# # website = "https://www.betterworldbooks.com/"
# # timeout_seconds = 2
# # header = {"User-Agent": user_header}

# # user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# # header = {'User-Agent': 'Mozilla/5.0'}


# # feature = []
# # tmp_text = ""
# # original_text = []


# # request = urllib.request.Request(website, headers = header)
# # print(website)
# # time.sleep(randint(1,5))  # from 5 to 30 seconds
# # try:
# #     response = urllib.request.urlopen(request, timeout=timeout_seconds).read()
# # except Exception as e:
# #     print("Unable to access website response")

# data_labeling_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling.xlsx"

# df = pd.read_excel(data_labeling_path, sheet_name='dataset')
# x = df.iloc[:, [0,1,2,3,4,5,6,7]].values
# labels = df.iloc[:, 8].values
# random_seed = 5
# print("x")
# print(x)
# print("labels")
# print(labels)

# model = RandomForestClassifier(n_estimators=100,
#                                 random_state=random_seed,
#                                 max_features='sqrt')

#rf_classifier.training()


# DataCollection, will initialize the data
# keyword_list = ["markov chain", "image segmentation", "recurrent neural network",
#                 "protocol hierarchy", "backup system", "requirement analysis", "link layer",
#                 "congestion window", "binary tree", "big o notation", "application programming interface",
#                 "computer science", "floating point", "dijkstra algorithm", "user interface", "virtual machine",
#                 "web crawler", "data structure", "quick sort"]
keyword_list = ["data structure", "quick sort"]
output_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_collection_out.csv"
webpage_crawler.DataCollectionList(keyword_list, output_path, 10, 1)
# output_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_training.csv"


#webpage_crawler.DataCollection("binary tree", 2, 1)
# url = "https://web.mit.edu/16.070/www/lecture/big_o.pdf"
# result = webpage_crawler.parsePDF(url)
# print(result)
