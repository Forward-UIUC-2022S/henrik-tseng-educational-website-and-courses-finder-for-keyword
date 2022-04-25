import urllib.request
import urllib.parse
from googlesearch import search
from bs4 import BeautifulSoup
from random import randint
import time
import csv
import requests, PyPDF2
#from PyPDF2 import PdfFileReader

path = "./tmp_website.html"
timeout_seconds = 2
'''
Function: DataSearch

Introduction:
    For a certain keyword, collect its features as data from first result page and secondary result page of google search.
    Similar functionality to DataSearch, but this one used for user input data collection, working on a much smaller scale.

Parameters:
    keyword (string): a given keyword that would be featured
    result_num(integer): expected number of returned search results from user, default set to 10
    apply_filter(0 or 1): indicate whether to apply the filter to clear out similar results, 1 for yes, 0 for no.
                                  Input by user, default set to 1
                    
Outputs:
    final_results_list(list): satisfied websites list
    final_features(list): all features collected from corresponding websites in 'final_results_list' for later classifier prediction
'''

def DataSearch(keyword,result_num,apply_filter,user_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"):

    keyword = keyword.lower()
    query = str(keyword)
    first_results_list = []
    final_results_list = []
    final_features = []
    temp = []

    # print("cp1")

    # for i in search(query,  # The query you want to run
    #                 tld='com',  # The top level domain
    #                 lang='en',  # The language
    #                 # num = 10,     # Number of results per page
    #                 start=0,  # First result to retrieve
    #                 stop=2*result_num + 5,  # Last result to retrieve
    #                 pause=2.0,  # Lapse between HTTP requests
    #                 ):
    #     first_results_list.append(i)
    
    for i in search(query,  # The query you want to run
                    tld='com',  # The top level domain
                    lang='en',  # The language
                    num = 10,     # Number of results per page
                    start=0,  # First result to retrieve
                    stop=2*result_num + 5,  # Last result to retrieve
                    pause=2.0,  # Lapse between HTTP requests
                    ):
        first_results_list.append(i)

    # print("cp2")

    for web in first_results_list:
        if len(final_results_list) == result_num:
            break

        if apply_filter == 1:
            print(web)
            main_part = web.split("//")[1]
            main_part_1 = main_part.split("/")[0]

            if main_part_1 not in temp:
                temp.append(main_part_1)
                final_results_list.append(web)

        if apply_filter == 0:
            final_results_list.append(web)

    # print out the results
    print('websites for keyword ',keyword,' :',final_results_list)


    for website in final_results_list:
        # feature = [org?,edu?,com?,else?,keyword in entry?,entry length,10 types,label]
        feature = []

        tmp_text = ""
        original_text = []

        header = {"User-Agent": user_header}
        request = urllib.request.Request(website, headers = header)
        print(website)
        time.sleep(randint(1,3))  # from 5 to 30 seconds
        
        try:
            response = urllib.request.urlopen(request, timeout=timeout_seconds).read()
            #print(type(response))
        except Exception as e:
            print("Unable to access website, error " + str(e))
            response = b''

        # store the website into the temporary file
        file = open(path, "wb")
        file.write(response)
        file.close()

        # fetch the appropriate text from the website
        soup = BeautifulSoup(open(path,'rb'), features="lxml")
        for p_idx in soup.select("p"):
            tmp_text += p_idx.get_text()

        original_text.append(tmp_text)
        #print("Original Text")
        #print(original_text)
        # print("cp3")

        ### Adding new features to include website URL checking
        url = "https://google.com/search?q="
        url += website

        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        #time.sleep(randint(5, 10))  # from 1 to 3 seconds

        # Perform the request
        request = urllib.request.Request(url, headers=header)
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")

        # Construct the soup object
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the search result divs
        divs = soup.select("#search div.g")

        div = divs[0]
        div_text = div.get_text()
 

        # feature = [org?,edu?,com?,else?,keyword in entry?,entry length,10 types,label]

        # write the corresponding url into csv for convenience of labelling data
        feature.append(website)

        flag = True
        if '.org' in div_text:
            flag = False
            feature.append(1)
        else:
            feature.append(0)

        if '.edu' in div_text:
            flag = False
            feature.append(1)
        else:
            feature.append(0)

        if '.com' in div_text:
            flag = False
            feature.append(1)
        else:
            feature.append(0)

        if flag and '.' in div_text:
            feature.append(1)
        else:
            feature.append(0)

        if keyword in div_text:
            feature.append(1)
        else:
            feature.append(0)

        feature.append(len(div_text))

        type_words = ['tutorial', 'wiki', 'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram',
                      'book']

        for word in type_words:
            if word in div_text:
                feature.append(1)
            else:
                feature.append(0)


        # header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        # request = urllib.request.Request(website, headers = header)
        # response = urllib.request.urlopen(request).read()


        # store the website into the temporary file
        # file = open(path, "wb")
        # file.write(response)
        # file.close()

        # fetch the appropriate text from the website
        # soup = BeautifulSoup(open(path,'rb'), features="lxml")
        # for p_idx in soup.select("p"):
        #     tmp_text += p_idx.get_text()

        # original_text.append(tmp_text)
        
        # testing specific websites
        # print()
        # print()
        # print("div text!!!!!")
        # print(div_text)
        # #if "pdf" in div_text or "PDF" in div_text:
        # print("!!!   Printing text of website   !!!")
        # print(original_text[0])
        # print()
        
        text = original_text[0]
        if website.endswith(".pdf"):
            text = parsePDF(website)
        
        # feature: the number of times keyword appear in the text
        if keyword in text:
            feature.append(text.count(keyword))
        else:
            feature.append(0)

        # feature: content length
        feature.append(len(text))

        # feature: various content detection
        content_words = ['diagram', 'example', 'formula', 'graph', 'code', 'video', 'book']

        for word in content_words:
            feature.append(text.count(word))

        final_features.append(feature)
        

        # # feature: content length
        # feature.append(len(original_text[0]))

        # # feature: various content detection
        # content_words = ['diagram', 'example', 'formula', 'graph', 'code', 'video', 'book']

        # for word in content_words:
        #     feature.append(original_text[0].count(word))
        # print(original_text)
        # final_features.append(feature)
    #print("final feature")
    #print(final_features)
    return final_results_list, final_features

def DataCollectionList(keyword_list, output_path, result_num = 10, apply_filter = 1, write_feature_names = False):

    # Write the feature names to the first line of csv file
    feature_names = ['Keyword', 'index', 'url', 'org', 'edu', 'com', 'else', 'keyword in entry', 'entry length',
                     'tutorial', 'wiki',
                     'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram', 'book', 'keyword_count',
                     'content_length',
                     'content_diagram', 'content_example', 'content_formula', 'content_graph', 'content_code',
                     'content_video', 'content_book', 'label']

    final_feature_names = []
    final_feature_names.append(feature_names)
    user_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

    with open(output_path, 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        for i in final_feature_names:
            writer.writerow(i)

    print('Write feature name done!\n')

    for keyword in keyword_list:
        final_results_list, final_features = DataSearch(keyword, result_num, apply_filter)
        index = 0
        # print out the results
        print('websites for keyword',keyword,':',final_results_list)
        print("final_features", final_features)
        with open(output_path, 'a', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            for i in final_features:
                index += 1
                i.insert(0, index)
                i.insert(0,keyword)
                writer.writerow(i)
        

def parsePDF(url):
    response = requests.get(url)
    my_raw_data = response.content

    with open("my_pdf.pdf", 'wb') as my_data:
        my_data.write(my_raw_data)

    open_pdf_file = open("my_pdf.pdf", 'rb')
    read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
    number_of_pages = read_pdf.numPages
    result = ""
    
    if read_pdf.isEncrypted:
        read_pdf.decrypt("")
    for i in range(number_of_pages):
        cur_page = read_pdf.getPage(i).extractText()
        result += ''.join(cur_page.splitlines())
    #print(result)
    return(result)


# '''
# Function: read_keywords
# Read out all required keywords
#     Parameters: None
# '''

# def read_keywords():
#     # file = open("keyword_list.txt", "r")
#     file = open("evaluation_keyword_list.txt", "r")
#     for word in file:
#         keyword = word.replace('\n', '')
#         DataCollection(keyword)

# keyword = 'decision tree'

# Final test 1
# DataCollection('neural network',result_num = 1)
# print('Test ends')

# Final test 2
# read_keywords()
# print('Test ends')


# '''
# Function: DataCollection

# Introduction:
#     For a certain keyword, collect its features as data from first result page and secondary result page of google search
#     Similar functionality to DataSearch, but this one used for large scale data collection to form a data set and train the
#     classifier.

# Parameters:
#     keyword (string): a given keyword that would be featured
#     result_num(integer): expected number of returned search results from user, default set to 10
#     apply_filter(0 or 1): indicate whether to apply the filter to clear out similar results, 1 for yes, 0 for no.
#                                   Input by user, default set to 1
# '''

