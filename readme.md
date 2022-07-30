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
    * After fetching of the required details, we pass it to the below algorithm for generating a critical score. The formula and the table can seen [here](#algorithm).
    * The critical score algorithm has been enhanced according to the common datapoints fetched from each platform.
  

### Future of the Project:
  * We desire to host the project online for the vast use and feedback purposes.
  * We are also working on enhancing the  algorithm by fetching maximum datapoints in the formula.
  * We welcome contributors to enhance the project and help us gaining the correct insights on a repository to protect the users from using any vulnerable repository.

### Screenshots:
<img src="static\images\homepage.jpeg">
<img src="static\images\safe_result.jpeg">
<img src="static\images\unsafe_result.jpeg">


### Algorithm: 
This algorithm is responsible for generating the critical score which judges whether the repo is vulnerable or not.

The base algorithm is a derived version of the research paper by [Mr. Rob Pike]() :
<img src="https://raw.githubusercontent.com/ossf/criticality_score/main/images/formula.png" width="359" height="96"> 

We use the following default parameters to derive the criticality score for an
open source project:

| Parameter (S<sub>i</sub>)  | Weight (&alpha;<sub>i</sub>) | Max threshold (T<sub>i</sub>) | Description | Reasoning |
|---|---:|---:|---|---|
| created_since | 1 | 120 | Time since the project was created (in months) | Older project has higher chance of being widely used or being dependent upon. |
| updated_since  | -1 | 120 | Time since the project was last updated (in months) | Unmaintained projects with no recent commits have higher chance of being less relied upon. |
| **contributor_count** | **2** | 5000 | Count of project contributors (with commits) | Different contributors involvement indicates project's importance. |
| commit_frequency | 1 | 1000 | Average number of commits per week in the last year | Higher code churn has slight indication of project's importance. Also, higher susceptibility to vulnerabilities.


The above algorithm has been enhanced accordingly to improve the citing of vulnerability in a repo due to the change of datapoints which can't be retrieved for each repository on every platform.


## Contributors

[![Contributors](https://contrib.rocks/image?repo=Vatendra/repoAnalyzer)](https://github.com/Vatendra/repoAnalyzer/graphs/contributors)
