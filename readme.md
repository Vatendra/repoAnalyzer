# Project Name: RepoAnalyser
# Flipkart Grid 4.0

## Team name: The A Team
* Anubhav Mishra (Leader)
* Karan Kartikeya
 

### Problem Statement: Open Source Software (OSS) Security Inspector 

### Problem Description:
 * Examine the public open source repository by just providing the link
 * Share the rating of the repository
 * Describe a criteria to say a repo is vulnerable or not

### Our Solution:
 * CodeBase Layout: 
    * Backend: Flask
    *  Frontend: HTML and  CSS
 * Logic:
    * Designed python files which contains API calls to get information about the repository from Github, GitLab, npm, pypi and Bitbucket as of now.
    * After fetching of the required details, we pass it to the below algorithm for generating a critical score. The formula and the table can seen [here](#algorithm)
    * The critical score algorithm has been enhanced according to the common datapoints fetched from each platform
  

### Future of the Project:
  * We desire to host the project online for the vast use and feedback purposes.
  * We are also working on enhancing the  algorithm by fetching maximum datapoints in the formula.
  * We welcome contributors to enhance the project and help us gaining the correct insights on a repository to protect the users from using any vulnerable repository.




### Algorithm: 
This algorithm is responsible for generating the critical score which judges whether the repo is vulnerable or not.

The base algorithm is a derived version of the research paper by [Mr. Rob Pike]() :
<img src="https://raw.githubusercontent.com/ossf/criticality_score/main/images/formula.png" width="359" height="96"> 

The above algorithm has been enhanced accordingly to improve the citing of vulnerability in a repo due to the change of datapoints which can't be retrieved for each repository on every platform.


## Contributors

[![Contributors](https://contrib.rocks/image?repo=Vatendra/repoAnalyzer)](https://github.com/Vatendra/repoAnalyzer/graphs/contributors)
