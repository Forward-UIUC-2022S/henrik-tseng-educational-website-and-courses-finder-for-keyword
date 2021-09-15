# Educational-website-and-courses-finder-for-keyword
Return the filtered useful educational resources based on input keyword and filtering conditions from users
## Functional Design(primary version, subject to change)
### Module: DataCollection
1. Function: SemanticParsing
   - Description: Simulate the real environment of a google search, respond to any strings a user may type in
   - Input:
     - user_demand: arbitrary input strings that a user may input for educational resources google search
   - Output:
     - keywords: list of keywords for related educational resources finding according to user input string
     - conditions: filtering conditions for returned value according to user input string
   - Functionality: Paraphrase the key info of what user what from input string, parse them out for ranking and filtering separately
     
2. Function: DataCollection
   - Description: The search process for resources gathering
   - Input:
     - keywords: list of keywords for related educational resources finding
     - conditions: filtering conditions for returned values
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
1. Function: ConditionFiltering
   - Description: First step of filtering the resources
   - Input:
     - ripe_data: processed related resources found through the search, format friendly for later modules
     - conditions: filtering conditions for returned value according to user input string
   - Output:
     - filtered_data: list of resources that satisfy all conditions from the user
   - Functionality: Filter the resources according to input conditions from user that parsed above

2. Function: RankingFiltering
   - Description: Second step of filtering the resources
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
