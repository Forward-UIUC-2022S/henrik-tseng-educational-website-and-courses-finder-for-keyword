# Educational-website-and-courses-finder-for-keyword
Return the filtered useful educational resources based on input keyword and filtering conditions from users
## Functional Design(primary version)
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


## Algorithm Design(primary version)
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

### (Old version)Part 1: Gathering related educational resources(diagram incoming)
#### Introduction: 
This part is for related resources gathering. Start with a rough collection on Google, followed by concept identification (and also a naive concept summarization) to filter out resources with low correlation, shrink the dataset scale to make convenience for later processing.

#### Implementation:
Suppose we have an input keyword W, we gather the related educational resources through following process.
1. Complete Google search and obtain all results that contain W in their text content.
2. For every single result, do following steps in order:
   - Do TextRank(my previous implementation) upon the text content to find weighted keywords(or key phrases, the same below) through built weighted graph.
   - Do frequency count within the text content for all keywords in weight.
   - Weighting the two results from above 2 steps to get the Final Keyword List(FKL) with weight updated weight attached.
   - Keep the result if obtained FKL contains W, otherwise disgard it.

### Part 2: Usefulness ranking(diagram incoming)
#### Introduction: 
This part is to rank the usefulness of the resources selected in previous part, and return the resources to users sorted according to usefulness ranks.

#### Implementation:
This part only works on results survive from previous part.
1. Add all words in FKLs of remaining results into a corpus C without duplicates.
2. For all keywords in C, set up a matrix A, where Aij is the weight of ith keyword in jth result's FKL, here the order of i,j does not matter.
3. Do singular value decomposition(SVD) for A :</br>
![image](https://user-images.githubusercontent.com/66361320/134427181-4a6829cb-8bb9-46a7-a4d4-def8722ffbde.png)
4. Dimension reduction for A: only keep the k highest eigenvalues in Σ and set all other values to 0, then multiply back to get:(Notice that Ak here is for future extra use)
![image](https://user-images.githubusercontent.com/66361320/134428069-bab4a12f-56cf-4ed2-87b4-6d3500484257.png)
5. Sort Σk according to eigenvalues and fetch the highest n values, find corresponding keywords(with eigenvalue as weight) and form a set K
6. Each result calculate total score, which is the sum of weight of word i, where i ∈ its FKL and i ∈ K. 
7. Sort the results according to their total scores, which is actually the usefulness ranking, and return to the users.


## References
### Dataset
To be updated

### Papers
Jorge Villalon & Rafael A. Calvo. (2009).Concept Extraction from Student Essays, Towards Concept Map Mining: 
- Main page: https://ieeexplore.ieee.org/abstract/document/5194208
- pdf version from Google scholar: https://d1wqtxts1xzle7.cloudfront.net/50645682/Concept_Extraction_from_Student_Essays_T20161130-19200-de091o-with-cover-page-v2.pdf?Expires=1632349340&Signature=JAqnsyiLEiEE17k4TalYoQqx8YHdOrXi4qgXJcYwZgcrCOG0sgSzdYq1l-220nl4MdlkCuYShihyN2qGuZDctLnSCpasTCKgveSy1XJoewo1Ar0gbe3CmYhkXhdXxAnp2HIbiYtL9dClxTzm0xWZTQPEmn8FviRRCKlOrIZcfoVU2ipsWoDRA6cik6wTzLVw4dZQcJgMprVlsk4HqgJy1Dmj0pOIKrtKtMUyvFXjYEH0EYRtmiBheAhrIyNJ0eBE~FmapNFj88vMarR9xcZZQcVsCsp6w0Bz0A-d~wuINTEWQ3CV95dW1IFs91dZ4xPkBXtrrCpmkYoFgbHkQn2fXg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
