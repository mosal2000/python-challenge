# Python-Challenge
## Python Code
  * PyBank/main.py
  * PyPoll/main.py
  * **Extra:** 
    * PyParagraph/main.py
    * PyBoss/main.py
## Output Result
  * PyBank/PyBank.txt
  * PyPoll/PyPoll.txt
  * **Extra:** 
    * PyParagraph/PyParagraph.txt
    * PyBoss/PyBoss.csv

## Background

This project **2** Python Challenges, PyBank and PyPoll. Both of these challenges encompasses a real-world situation using Python scripting.

## PyBank

![Revenue](Images/revenue-per-lead.jpg)

* In this challenge, we are creating a Python script for analyzing the financial records of a company. A set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv) is given. The dataset is composed of two columns: `Date` and `Profit/Losses`.

* The Python script analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The total net amount of "Profit/Losses" over the entire period

  * The average change in "Profit/Losses" between months over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* The script print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote-Counting](Images/Vote_counting.jpg)

* In this challenge, we are building a vote-counting process.

* A set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv) is given. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* The analysis look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, the final script both prints the analysis to the terminal and export a text file with the results.

