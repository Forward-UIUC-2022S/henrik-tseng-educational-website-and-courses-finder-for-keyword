# zicheng-ma-educational-website-and-courses-finder-for-keyword
This project will return the filtered useful educational resources based on input keyword and filtering conditions from users
# Setup

## Dependencies
```
pip install -r requirements.txt
```

Alternative:
Manually run line by line in the command prompt for the dependencies listed in manual_requirements.txt

## File Structure
```
zicheng-ma-educational-website-and-courses-finder-for-keyword/
    - requirements.txt
    - README.md
    - dataset/
        -- data_labeling.xlsx
        -- evaluation_keyword_list.txt
        -- features_data.csv
        -- keywords_training.txt
    - src/
        -- __init__.py
        -- main.py
        -- webpage_crawler.py
        -- Train_Classifier.py
        -- rf_classifier.py
     - tests/
        -- sample_result.png
        -- sample_result.txt
```

## File Descriptions

* ```dataset/data_labeling.xlsx```: Data set that used to train classifier
* ```dataset/evaluation_keyword_list.txt```: keyword lists used for classifier evaluation
* ```dataset/features_data.csv```: Primary gathered data
* ```dataset/keywords_training.txt```: keyword lists used for classifier training
* ```src/main.py```: The file connecting all other parts to make them work as a whole for users' convenience.(Users should mainly modify this file)
* ```src/webpage_crawler.py```: Used for websites collecting
* ```src/Train_Classifier.py```: Used to train GaussianNB classifier
* ```src/rf_classifier.py```: Used to train random forest classifier. (Users should modify the path for classifier training in this file)

# Demo Video
Google Drive: https://drive.google.com/file/d/1njDFgL8vB1uZiJqXHRxSSATe9LI4c3yn/view?usp=sharing
Updated Video: https://youtu.be/yFSXfu15QG0

# Functional Design
## Module: DataCollection
1. Function: DataSearch(for user)
   - Description: For a certain keyword, collect its features as data from first result page and secondary result page of google search. Similar functionality to DataSearch, but this one used for user input data collection, working on a much smaller scale.
   - Input:
     - keyword (string): a given keyword that would be featured
     - result_num(integer): expected number of returned search results from user, default set to 10
     - apply_filter(0 or 1): indicate whether to apply the filter to clear out similar results, 1 for yes, 0 for no.
                                  Input by user, default set to 1
   - Output:
     - final_results_list(list): satisfied websites list
     - final_features(list): all features collected from corresponding websites in 'final_results_list' for later classifier prediction

2. Function: DataCollection(for classifier)
   - Description: For a certain keyword, collect its features as data from first result page and secondary result page of google search. Similar functionality to DataSearch, but this one used for large scale data collection to form a data set and train the classifier.
   - Input:
     - keyword (string): a given keyword that would be featured
     - result_num(integer): expected number of returned search results from user, default set to 10
     - apply_filter(0 or 1): indicate whether to apply the filter to clear out similar results, 1 for yes, 0 for no.
                                  Input by user, default set to 1


## Module: UsefulnessRanking
1. Function: predict_for_user(for user)
   - Description: Input the lists of features collected from the websites, this function apply them to a trained random forest classifier and generate prediction for them
   - Input:
     - processed_data:features(list): all features collected from corresponding websites in 'final_results_list' for later classifier prediction
   - Output:
     - predictions(list): predicated labels from rf classifier to corresponding websites in input 'features'

2. Function: training(for classifier)
   - Description: Similar to predict_for_user, but this function is designed to train and evaluate the classifier.


# Algorithm Design
1. Using a crawler to copy down the source code of html page for every individual google search result according to input keyword.</br>
![172eee9c7336938393c2ec712c2ff97](https://user-images.githubusercontent.com/66361320/135891667-90540080-ca48-456f-bb52-f97ef9aeb3da.png)

2. Judge usefulness based on the following features, every single point satisfied will add up score for that result, and different point may provide different score:</br>
![65fcdbba14250f5ec69c0f8a4c3a253](https://user-images.githubusercontent.com/66361320/137957846-cd0070b5-14ce-4db9-b9ce-49b44cf354d7.png)
   - (1) Whether the url of that result is ended with edu, org (Obviously not all resources are provided on .edu or .org, but this should give higher preference）
   - (2) The title label in html，such as'course', 'class' ,'lecture', 'tutorial', 'exercise', 'textbook', 'handout', 'guideline' etc.(But should all contain keyword)
   - (3) The 'audio','video','pdf' labels in html，a resource with picture or video or pdf can be much more useful than plain texts. 
      - Further judgement on the 'source' tag under 'video' tag or others, and check the 'src' string to fing out the name of audio, video or pdf to judge whether it is useful(based on the comparison to keyword)
      - Further judgement on the descriptive texts around the video, audio or pdf to find out how relevant it is to the keyword, rather than maybe an ad.
   - (4) Diagram, same as (3)

3. Some extra criteria I think is necessary(Planned extra implementation):
   - User comments, rankings, page view, share or reprint times, favorite percentage. 
   - Release time, publisher

# Issues and Future Work

* The website filter function still needs some further improvement to smartly clear out the duplicate websites or similar websites that is truly not useful. 
* Improve the situation that sometimes there will not be enough results returned by the program when applying the filter to it.
* The internet and API issues are still instable. 

# References
## Dataset
Self-collected, attached in 'dataset' folder

## Papers
* Beautiful Soup Official Document: https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
* Current Google Search Packages using Python3.7: A Simple Tutorial: https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4
* An Introduction To Building a Classification Model Using Random Forests In Python: https://blogs.oracle.com/ai-and-datascience/post/an-introduction-to-building-a-classification-model-using-random-forests-in-python
* How To Build a Machine Learning Classifier in Python with Scikit-learn: https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn
* Searching and Ranking Educational Resources based on Terms Clustering: https://pdfs.semanticscholar.org/eee4/070731bcab1e425831aef2bf4fb5006c289f.pdf
* An Implementation and Explanation of the Random Forest in Python: https://towardsdatascience.com/an-implementation-and-explanation-of-the-random-forest-in-python-77bf308a9b76
* Classification: ROC Curve and AUC: https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc


## APIs
* googlesearch API: https://python-googlesearch.readthedocs.io/en/latest/

## Edits by Henrik Tseng
1. Addition of new files and new functions:
   - main_two.py: another additional main py file that focuses on calling functions for web scraping and adding to datasets
   - webpage_crawler.DataCollectionList: New function that expands on Datasearch
   - parsePDF: New function that parses in PDF, uses PyPDF2
   - manual_requirements.txt: full list of new dependencies for manual installation instead of using requirements.txt
   - model_comparisons.txt: New file that stores past comparison with keywords.
2. Modifying and adding datasets:
   - Multiple new datasets added in the dataset folder:
      - Notable datasets are data_labeling_modified_copy.xlsx, which is now the main dataset that should be used for training the model
      - Another notable dataset is data_collection_out.csv, which the main_two.py file will output the results toward, which will store the results of webscrabing
      - The rest of the datasets in the folder are mostly random datasets created while bugtesting, and not really useful
3. Changing functions and functionality:
   - webpage_crawler.DataSearch: Heavily modified to include details about the content within websites and to return the additional content, specifically includes points of 'content_length','content_diagram','content_example', 'content_formula', 'content_graph', 'content_code', 'content_video', 'content_book', 'label'
      - Datasearch now is able to parse txt files, but videos are still ignore and counted as a 0 by the model
      - More parameters now, user can input how long to wait in between search results(in seconds) with parameter sleep_floor and sleep_ceiling
      - Removed youtube links from being accepted as possible results. Can easily add more links to ignore with the new global variable IGNORE_LINKS
   - modify_data.add_sum: modified so that the model will take in additional content parsed by datasearch
4. Possible additions in the future:
   - Incorporate youtube links(currently ignored in the model) by parsing transcript instead
   - Image, audio, links, and files counted can be inaccurate currently due to searching keywords instead
   - Another factor to add could include number of links in the website(would mean that a table of contents could be rated higher)
   - training, evaluate_model, plot_confusion_matrix functions from rf_classifier need to be updated to work with new model
5. New Dependencies:
   - PyPDF2, can be installed with
      - pip install PyPDF2
   - See manual_requirements.txt for full list of dependencies
5. Schedule(Date):
   - 2/7: Changed dependencies. Refer to manual_requirements for more details
   - 2/14: Now skipping certain websites using ignore_website
   - 2/21-3/7: Updating model to use keyword count and additional factors from website details
   - 3/14: Updating training datasets
   - 3/21-4/4: Continue updating model and overall refactoring of the web scraper function
   - 4/11-Current: Created DataCollectionList function and updated to update the new training dataset
6. Current Model performance:
   - Compared to original model at the beginning (Jan 2022) significant improvements on the ratings, outputting higher ratings(2) overall for a more desirable output
   - Still certain problems with current model not predicting accurately, notable with BIG O NOTATION keyword and websites with high keyword count, and educational resources being rated low(ex. big o notation on wikipedia being rated as 0 with good factors to consider)
   - training, evaluate_model, plot_confusion_matrix functions from rf_classifier need to be updated to work with new model

