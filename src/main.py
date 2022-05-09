import sys
sys.path.append(r"E:\Learning\undergraduate\2021 Fall\CS397\Educational-website-and-courses-finder-for-keyword\code")
#from code import webpage_crawler, rf_classifier
import webpage_crawler, rf_classifier

output = []
output_ranking = []

default_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

# rf_classifier.training()
keyword = input("Please enter your search keyword:")

website_num = input("Please enter your expected number(integer) of search results:")
while not (website_num.isdigit()):
    print("Please enter an integer!")
    website_num = input("Please enter your expected number(integer) of search results:")
website_num = int(website_num)

apply_filter = int(input("Do you want to apply the filter to clear similar results?(1 for yes, 0 for no):"))
while (apply_filter != 0) and (apply_filter != 1):
    print("Please enter 0 or 1!")
    apply_filter = int(input("Do you want to apply the filter to clear similar results?(1 for yes, 0 for no):"))

# user_header = input("Please enter the 'User-Agent' of your computer:")
sleep_floor = int(input("Please enter a minimum and maximum range of how long to wait between each search result in seconds (recommended 1 to 3 seconds):"))
while (not isinstance(sleep_floor, int)):
    print("Please enter an integer")
    sleep_floor = int(input("Please enter a minimum and maximum range of how long to wait between each search result in seconds (recommended 1 to 3 seconds):"))

sleep_ceiling = int(input("Max:"))
while (not isinstance(sleep_ceiling, int)):
    print("Please enter an integer")
    sleep_ceiling = int(input("Max:"))


print("Program is collecting search results, please wait...")
websites, features = webpage_crawler.DataSearch(keyword, website_num, apply_filter, user_header= default_header, sleep_floor=sleep_floor, sleep_ceiling=sleep_ceiling)
print("features")
print(features)

# print(features)
print("Program is applying to classifier, please wait...")
predicted_labels = rf_classifier.predict_for_user(features)
print(predicted_labels)
 
print("Program is generating outputs, please wait...")
for i in range(len(predicted_labels[0])):
    if predicted_labels[0][i] == 2:
        output.append(websites[i])
        output_ranking.append(2)

for i in range(len(predicted_labels[0])):
    if predicted_labels[0][i] == 1:
        output.append(websites[i])
        output_ranking.append(1)

for i in range(len(predicted_labels[0])):
    if predicted_labels[0][i] == 0:
        output.append(websites[i])
        output_ranking.append(0)

print(
    "Note: The output websites will be sorted and contained in a list, with the leftmost being most useful and rightmost being least useful")
print("The outputs are as followed:", output)
print("Useful level(larger = better):",output_ranking)
