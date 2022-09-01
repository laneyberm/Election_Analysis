# Colorado's Local Congressional Election Audit

## Project Overview
#### A Colorado Board of Elections employees, Tom and Seth, has given us a CSV (comma-seperated-values) data file consisting of a number for the ballot ID and a name for the county and candidate, respectively. At this point, we don't know how many counties and candidates are in the file. Overall, the data appears readable and there are no unusual row values that we can see. We have been given election audit tasks to analyze the data and produce the election results to be presented to the election committee. 

#### In this project, we will work together to create Python code to analyze the CSV data file to find the elections results. Additionally, we present a business proposal to the election commission on how this script can be used, with some modifications, for any election in the future. We used a pseudocode which will make the audit easier to present to colleagues and stakeholders. When looking at the code below, code with the "#" will act as a roadmap of what the steps will take to complete the task of the elections results. This will aid in following the data and recognizing where sections can be altered to analyze future elections given the same data file type. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.6, Visual Studio Code, 1.70.2

## Election-Audit Results
#### The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county turnout results were: 
  - Jefferson County recieved 10.5% of the vote and 38,855 number of the votes
  - Denver County recieved 82.8% of the vote and 306,055 number of the votes
  - Arapahoe County recieved 6.7% of the vote and 24,801 number of the votes
- The county with the largest county turnout was:
  - Denver, which recieved 82.8% of the vote and 306,055 number of the votes
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of the votes
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of the votes
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of the votes
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 number of the votes
#### After running the python code, the following results were displayed in a text file for easy viewing:
<img src="https://github.com/laneyberm/Election_Analysis/blob/main/Resources/election_results.png" width="300">

#### We used the following Python code to calculate the counties' votes:
<img src="https://github.com/laneyberm/Election_Analysis/blob/main/Resources/county_votes.png" width="450">

#### We used the following Python code to calculate the county with the largest turnout:
<img src="https://github.com/laneyberm/Election_Analysis/blob/main/Resources/county_turnout.png" width="600">

#### We used the following Python code to calculate the candidates performance and winning candidate:
<img src="https://github.com/laneyberm/Election_Analysis/blob/main/Resources/winning_candidate.png" width="500">

## Election-Audit Summary
The winner of the election is Diana DeGette with 73.8% of the vote. 

In future elections, the above coding would be able to analyze different candidate names or different counties. Additionally, this type of coding could be used to analyze voters' party affiliation, gender, age, race, and type of voting: mail in, early and day of. This coding could also in as narrow of a scope of a school board election by changing the candidate name coding to new school board names or as large as national elections by changing the county names to state names to find how each state votes for the president. 
