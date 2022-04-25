# def DataCollection(keyword, result_num = 10, apply_filter = 1):
    # # Write the feature names to the first line of csv file
    # feature_names = ['Keyword', 'index', 'url', 'org', 'edu', 'com', 'else', 'keyword in entry', 'entry length',
    #                 'tutorial', 'wiki',
    #                 'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram', 'book', 'keyword_count',
    #                 'content_length',
    #                 'content_diagram', 'content_example', 'content_formula', 'content_graph', 'content_code',
    #                 'content_video', 'content_book', 'label']

    # final_feature_names = []
    # final_feature_names.append(feature_names)

    # output_path = 'features.csv'

    # with open(output_path, 'a', encoding="utf-8", newline='') as file:
    #     writer = csv.writer(file)
    #     for i in final_feature_names:
    #         writer.writerow(i)

    # print('Write feature name done!\n')

#     keyword = keyword.lower()
#     query = str(keyword)
#     first_results_list = []
#     final_results_list = []
#     temp = []
#     for i in search(query,  # The query you want to run
#                     tld='com',  # The top level domain
#                     lang='en',  # The language
#                     num = 10,     # Number of results per page
#                     start=0,  # First result to retrieve
#                     stop=2*result_num,  # Last result to retrieve
#                     pause=2.0,  # Lapse between HTTP requests
#                     ):
#         first_results_list.append(i)

#     for web in first_results_list:
#         if len(final_results_list) == result_num:
#             break

#         if apply_filter == 1:
#             main_part = web.split("//")[1]
#             main_part_1 = main_part.split("/")[0]

#             if main_part_1 not in temp:
#                 temp.append(main_part_1)
#                 final_results_list.append(web)

#         if apply_filter == 0:
#             final_results_list.append(web)

#     # print out the results
#     print('websites for keyword ',keyword,' :',final_results_list)

#     # First webpage data collection

#     idx = 1
#     for website in final_results_list:
#         url = "https://google.com/search?q="
#         url += website

#         header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
#         time.sleep(randint(5, 30))  # from 5 to 30 seconds

#         # Perform the request
#         request = urllib.request.Request(url, headers=header)
#         raw_response = urllib.request.urlopen(request).read()

#         # Read the repsonse as a utf-8 string
#         html = raw_response.decode("utf-8")

#         # Construct the soup object
#         soup = BeautifulSoup(html, 'html.parser')

#         # Find all the search result divs
#         divs = soup.select("#search div.g")

#         div = divs[0]
#         div_text = div.get_text()
#         # print(div_text + "\n")
#         print('Success for stage 1 with idx = ',idx)

#         # feature = [org?,edu?,com?,else?,keyword in entry?,entry length,10 types,label]
#         feature = []
#         feature.append(keyword)
#         feature.append(idx)
#         idx += 1

#         # write the corresponding url into csv for convenience of labelling data
#         feature.append(website)

#         flag = True
#         if '.org' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if '.edu' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if '.com' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if flag and '.' in div_text:
#             feature.append(1)
#         else:
#             feature.append(0)

#         if keyword in div_text:
#             feature.append(1)
#         else:
#             feature.append(0)

#         feature.append(len(div_text))

#         type_words = ['tutorial', 'wiki', 'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram',
#                       'book']

#         for word in type_words:
#             if word in div_text:
#                 feature.append(1)
#             else:
#                 feature.append(0)


#         # Secondary webpage data collection
#         tmp_text = ""
#         original_text = []


#         header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
#         request = urllib.request.Request(website, headers = header)
#         response = urllib.request.urlopen(request).read()


#         # store the website into the temporary file
#         file = open(path, "wb")
#         file.write(response)
#         file.close()

#         # fetch the appropriate text from the website
#         soup = BeautifulSoup(open(path,'rb'), features="lxml")
#         for p_idx in soup.select("p"):
#             tmp_text += p_idx.get_text()

#         original_text.append(tmp_text)

#         print('Success for stage 2 with idx = ', idx - 1)
#         # print('original_text:',original_text)
#         # print('original_text_2:',original_text_2)

#         # feature: the number of times keyword appear in the text
#         if keyword in original_text[0]:
#             feature.append(original_text[0].count(keyword))
#         else:
#             feature.append(0)

#         # feature: content length
#         feature.append(len(original_text[0]))

#         # feature: various content detection
#         content_words = ['diagram', 'example', 'formula', 'graph', 'code', 'video', 'book']

#         for word in content_words:
#             feature.append(original_text[0].count(word))

#         # default label
#         feature.append(1)

#         final_features = []
#         final_features.append(feature)

#         with open(output_path, 'a', encoding="utf-8", newline='') as file:
#             writer = csv.writer(file)
#             for j in final_features:
#                 writer.writerow(j)






# def DataCollectionKeyword(keyword, path, result_num = 10, apply_filter = 1, write_first_row = False):
#     # output_path = 'features.csv'
#     output_path = path
#     if write_first_row:
#         # Write the feature names to the first line of csv file
#         feature_names = ['Keyword', 'index', 'url', 'org', 'edu', 'com', 'else', 'keyword in entry', 'entry length',
#                         'tutorial', 'wiki',
#                         'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram', 'book', 'keyword_count',
#                         'content_length',
#                         'content_diagram', 'content_example', 'content_formula', 'content_graph', 'content_code',
#                         'content_video', 'content_book', 'label']

#         final_feature_names = []
#         final_feature_names.append(feature_names)

#         with open(output_path, 'a', encoding="utf-8", newline='') as file:
#             writer = csv.writer(file)
#             for i in final_feature_names:
#                 writer.writerow(i)

#         print('Write feature name done!\n')

#     keyword = keyword.lower()
#     query = str(keyword)
#     first_results_list = []
#     final_results_list = []
#     temp = []
#     for i in search(query,  # The query you want to run
#                     tld='com',  # The top level domain
#                     lang='en',  # The language
#                     num = 10,     # Number of results per page
#                     start=0,  # First result to retrieve
#                     stop=2*result_num,  # Last result to retrieve
#                     pause=2.0,  # Lapse between HTTP requests
#                     ):
#         first_results_list.append(i)

#     for web in first_results_list:
#         if len(final_results_list) == result_num:
#             break

#         if apply_filter == 1:
#             main_part = web.split("//")[1]
#             main_part_1 = main_part.split("/")[0]

#             if main_part_1 not in temp:
#                 temp.append(main_part_1)
#                 final_results_list.append(web)

#         if apply_filter == 0:
#             final_results_list.append(web)

#     # print out the results
#     print('websites for keyword ',keyword,' :',final_results_list)

#     # First webpage data collection

#     idx = 1
#     for website in final_results_list:
#         url = "https://google.com/search?q="
#         url += website

#         header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
#         time.sleep(randint(5, 30))  # from 5 to 30 seconds

#         # Perform the request
#         request = urllib.request.Request(url, headers=header)
#         raw_response = urllib.request.urlopen(request).read()

#         # Read the repsonse as a utf-8 string
#         html = raw_response.decode("utf-8")

#         # Construct the soup object
#         soup = BeautifulSoup(html, 'html.parser')

#         # Find all the search result divs
#         divs = soup.select("#search div.g")

#         div = divs[0]
#         div_text = div.get_text()
#         # print(div_text + "\n")
#         print('Success for stage 1 with idx = ',idx)

#         # feature = [org?,edu?,com?,else?,keyword in entry?,entry length,10 types,label]
#         feature = []
#         feature.append(keyword)
#         feature.append(idx)
#         idx += 1

#         # write the corresponding url into csv for convenience of labelling data
#         feature.append(website)

#         flag = True
#         if '.org' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if '.edu' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if '.com' in div_text:
#             flag = False
#             feature.append(1)
#         else:
#             feature.append(0)

#         if flag and '.' in div_text:
#             feature.append(1)
#         else:
#             feature.append(0)

#         if keyword in div_text:
#             feature.append(1)
#         else:
#             feature.append(0)

#         feature.append(len(div_text))

#         type_words = ['tutorial', 'wiki', 'introduction', 'course', 'class', 'lecture', 'video', 'graph', 'diagram',
#                       'book']

#         for word in type_words:
#             if word in div_text:
#                 feature.append(1)
#             else:
#                 feature.append(0)


#         # Secondary webpage data collection
#         tmp_text = ""
#         original_text = []


#         header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
#         request = urllib.request.Request(website, headers = header)
#         response = urllib.request.urlopen(request).read()


#         # store the website into the temporary file
#         file = open(path, "wb")
#         file.write(response)
#         file.close()

#         # fetch the appropriate text from the website
#         soup = BeautifulSoup(open(path,'rb'), features="lxml")
#         for p_idx in soup.select("p"):
#             tmp_text += p_idx.get_text()

#         original_text.append(tmp_text)

#         print('Success for stage 2 with idx = ', idx - 1)
#         # print('original_text:',original_text)
#         # print('original_text_2:',original_text_2)

#         # feature: the number of times keyword appear in the text
#         if keyword in original_text[0]:
#             feature.append(original_text[0].count(keyword))
#         else:
#             feature.append(0)

#         # feature: content length
#         feature.append(len(original_text[0]))

#         # feature: various content detection
#         content_words = ['diagram', 'example', 'formula', 'graph', 'code', 'video', 'book']

#         for word in content_words:
#             feature.append(original_text[0].count(word))

#         # default label
#         feature.append(1)

#         final_features = []
#         final_features.append(feature)

#         with open(output_path, 'a', encoding="utf-8", newline='') as file:
#             writer = csv.writer(file)
#             for j in final_features:
#                 writer.writerow(j)
