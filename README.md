
# Election_Analysis
## Overview and Purpose of the Election Analysis
I was given the task of auditing an election for a state election commission. They wanted me to calculate the candidate's votes along with the percentage of total votes that they won. I was also tasked with counting the amount of votes that were submitted in each county as well as their percentage in relation to the total. The purpose of this was to find out who won the election and their statistics. Also the commission wanted to see the breakdown of which county the votes were coming from.

## Election-Audit Results

- How many votes were cast

<img width="214" alt="Screen Shot 2021-07-21 at 11 48 59 PM" src="https://user-images.githubusercontent.com/83510059/126587703-046d56f4-c8be-40a4-b1cc-303c7de3cefe.png">


- This was found with a loop that referred to a variable called total_votes that was set to zero and for every row that had voting information it was increased by one. Below is the code that ran in the loop that went through each row counting the total votes
    ***total_votes = total_votes += 1***

- Breakdown of votes per county

<img width="204" alt="Screen Shot 2021-07-21 at 11 45 07 PM" src="https://user-images.githubusercontent.com/83510059/126587996-cd4a4465-bae3-4d4a-8fe2-659ef4b96274.png">

   - This was done by creating a dictionary to keep counties as keys and number of votes in counties as the values. Then a loop was ran indexing the county names in the data file and each time the county name was seen it activated the key in the previously made dictionary and increased the value by one **See Below**

          if countyName not in countyList:


                countyList.append(countyName)


                countyVotes[countyName] = 0


            countyVotes[countyName] += 1

        The Percentages were found by creating a variable and having it equal to a formula that divided each county's votes by the total votes using the dictionary created.
                   
            countyPerc = float(totalCounty) / float(total_votes) * 100


- County with largest vote count
    - Denver was the county with the largest vote count and that was found with an if statement loop that went through the dictionary previously created that now had the total votes per county and compared each county keeping the largest one in a variable called BCounty **See Below**

                 
            if (totalCounty > BCountyCount):
                BCounty = countyName
                BCountyCount = totalCounty
- Breakdown of votes per candidate
 
<img width="303" alt="Screen Shot 2021-07-21 at 11 46 13 PM" src="https://user-images.githubusercontent.com/83510059/126587568-26439110-b136-41c8-b83f-0bd28245f39f.png">

   This was done the same way that votes per county except done for candidates
   
- Winner's votes statistics

<img width="210" alt="Screen Shot 2021-07-21 at 11 46 22 PM" src="https://user-images.githubusercontent.com/83510059/126587612-495ff2f7-7bdb-4ceb-9481-232c63ce854e.png">

   - This was done similarly to finding the county with the most votes except there were two more variables to find being, winning count and winning percentage. The results were displayed and formatted using a fstring. ***See Below***

            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

## Election-Audit Summary

Below is a list of how this script can be used after votes have been tallied according to state laws and regulations
1. calculate total number of votes cast
2. Get a complete list of candidates
3. Calculate total votes for each candidate
4. Calculate percentage of votes for each candidate
5. Get a complete list of candidates
6. Calculate total votes for each candidate
7. Calculate percentage of votes for each candidate
8. Determine winner based on popular vote

This code could be modified to see which candidate a single county voted the most for. Another statistic this code could be modified to see is the percentage of a total candidate's vote that a county participated in.



## Resources
- Data source: election_results.csv
- Software: Python 3.6.1, VS Code 1.38.1

