# Educational-website-and-courses-finder-for-keyword
Return the filtered useful educational resources based on input keyword and filtering conditions from users
## Functional Design(primary version, subject to change)
### Module: DataCollection
1. Function: SemanticParsing(extra)
   - Description: Simulate the real environment of a google search, respond to any strings a user may type in
   - Input:
     - user_demand: arbitrary input strings that a user may input for educational resources google search
   - Output:
     - keywords: list of keywords for related educational resources finding according to user input string
     - (extra)conditions: filtering conditions for returned value according to user input string
   - Functionality: Paraphrase the key info of what user what from input string, parse them out for ranking and filtering separately
     
2. Function: DataCollection
   - Description: The search process for resources gathering
   - Input:
     - keywords: list of keywords for related educational resources finding
     - (extra)conditions: filtering conditions for returned values
   - Output:
     - raw_data: unprocessed related resources found through the search, stored in lists for future processing
   - Functionality: Obtain searching resources from Google Search with keywords


3. Function: Preprocessing
   - Description: Process the resources for later ranking and filtering module
   - Input:
     - raw_data: unprocessed related resources found through the search, stored in lists for future processing
   - Output:
     - ripe_data: processed related resources found through the search, format friendly for later modules
   - Functionality: Turn the rough format of resources into the format and syntax that later modules want

### Module: UsefulnessRanking
1. Function: ResourceRanking
   - Description: Rank the usefulness of collected resources
   - Input:
     - ripe_data: processed related resources found through the search, format friendly for later modules
   - Output:
     - rank: a list that contains the ranking for resources of the same index in ripe_data accordingly
   - Functionality: Provide the ranking of usefulness for all resources, used as judgment criteria in later module

### Module: ResultFiltering
1. Function: ConditionFiltering(extra)
   - Description: First step of filtering the resources
   - Input:
     - ripe_data: processed related resources found through the search, format friendly for later modules
     - (extra)conditions: filtering conditions for returned value according to user input string
   - Output:
     - filtered_data: list of resources that satisfy all conditions from the user
   - Functionality: Filter the resources according to input conditions from user that parsed above

2. Function: RankingFiltering
   - Description: Second step of filtering the resources, sort the resources according to usefulness rank
   - Input:
     - filtered_data: list of resources that satisfy all conditions from the user
     - rank: a list that contains the ranking for resources of the same index in ripe_data accordingly
   - Output:
     - filtered_useful_data: list of sorted resources that satisfy all conditions from the user and in the descending order of usefulness ranking
   - Functionality: Sort the primarily filtered resources based on usefulness ranking produced in UsefulnessRanking module

3. Function: DisplayResult
   - Description: Final step, show user the filtered results
   - Input: 
     - filtered_useful_data: list of sorted resources that satisfy all conditions from the user and in the descending order of usefulness ranking
     - Top_X : integer, meaning to get the topX of resources
   - Output:
     - Result: Final resources that best fit user command
   - Functionality: Return and display the needed topX results


## Algorithm Design(primary version, subject to change)
### (New version)only naive primary thought, no reference
Using a crawler to copy down the source code of html page for every individual google search result according to input keyword.</br>
Then judge usefulness based on the following, every single point satisfied will add up score for that result, and different point may provide different score:</br>
1. The url of that result, is it ended with edu, org? (Obviously not all resources are provided on .edu or .org, but this should give higher preference）
2. The title label in html，such as'course', 'class' ,'lecture', 'tutorial', 'exercise', 'textbook', 'handout', 'guideline' etc.(But should all contain keyword)
3. The 'audio','video','pdf' labels in html，a resource with picture or video or pdf can be much more useful than plain texts. 
   - Further judgement on the 'source' tag under 'video' tag or others, and check the 'src' string to fing out the name of audio, video or pdf to judge whether it is useful(based on the comparison to keyword)
   - Further judgement on the descriptive texts around the video, audio or pdf to find out how relevant it is to the keyword, rather than maybe an ad.
4. Diagram, same as 3

Some extra criteria I think is necessary:
   1. User comments, rankings, page view, share or reprint times, favorite perventage. 
   2. Release time, publisher
</br>

Blocked down paper, which might be useful for me but have no chance to read:https://ieeexplore.ieee.org/abstract/document/9529407</br>

Funny thing is, I notice that all judgement made above can be implemented simply by several 'if's, rather than designing a brilliant algorithm or supervised classifier.






## References
### Dataset
To be updated

### Papers
To be updated
