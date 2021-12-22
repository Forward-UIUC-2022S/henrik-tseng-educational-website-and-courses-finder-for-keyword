# zicheng-ma-educational-website-and-courses-finder-for-keyword
Return the filtered useful educational resources based on input keyword and filtering conditions from users
# Setup

## Dependencies
```
pip install -r requirements.txt
```

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

* ```dataset/data_labeling.xlsx```: 
* ```dataset/evaluation_keyword_list.txt```: 
* ```dataset/features_data.csv```: 
* ```dataset/keywords_training.txt```: 
* ```src/ __init__.py```: 
* ```src/webpage_crawler.py```: 
* ```src/main.py```: 
* ```src/Train_Classifier.py```: 
* ```src/rf_classifier.py```: 

# Demo Video
Incoming

# Functional Design
## Module: DataCollection
1. Function: DataCollection
   - Description: The search process for resources gathering
   - Input:
     - keywords: list of keywords for related educational resources finding
   - Output:
     - raw_data: unprocessed related resources found through the search, stored in lists for future processing
   - Functionality: Obtain searching resources from Google Search with keywords

2. Function: Preprocessing(For classifier)
   - Description: Process the resources for later processing
   - Input:
     - raw_data: unprocessed related resources found through the search, stored in lists for future processing
   - Output:
     - processed_data: processed related resources found through the search, format friendly for later modules
   - Functionality: Turn the rough format of resources into the format and syntax that later modules want

## Module: UsefulnessRanking
1. Function: ResourceRanking(Firstly implement by 'many-if')
   - Description: Rank the usefulness of collected resources
   - Input:
     - processed_data: processed related resources found through the search, format friendly for later modules
   - Output:
     - rank: a list that contains the ranking for resources of the same index in ripe_data accordingly
   - Functionality: Provide the ranking of usefulness for all resources, used as judgment criteria in later module

2. Function: FurtherResearch(extra)
   - Description: For each of the classified result, track some furthur features, include but not limited to user comments, user rankings, page view, share or reprint times, favorite perventage, release time, publisher etc..
   - Input:
     - processed_data: processed related resources found through the search, format friendly for later modules
     - (extra)conditions: filtering conditions for returned value according to user input string
   - Output:
     - filtered_data:  a list that contains the further ranking for resources of the same index in ripe_data accordingly
   - Functionality: Track all top results upon certain features for further usefulness evaluation

# Algorithm Design(secondary version, subject to change)
## (New version)only naive primary thought, no reference
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
   - User comments, rankings, page view, share or reprint times, favorite perventage. 
   - Release time, publisher

# Issues and Future Work

* The website filter function still needs some further improvement to smartly clear out the duplicate websites or similar websites that is truly not useful. 
* Improve the situation that sometimes there will not be enough results returned by the program when applying the filter to it.
* The internet and API issues are still instable. 

# References
## Dataset
Self-collected, attached in 'dataset' folder

## Papers
incoming:https://ieeexplore.ieee.org/abstract/document/9529407

## APIs
googlesearch API: https://python-googlesearch.readthedocs.io/en/latest/
