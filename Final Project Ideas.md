# Final Project Ideas
```sequence

Title: Gameplan
1st Step -> 2nd Step: Generate Interesting Ideas
Note right of 1st Step: Brad thinks..
2nd Step -> 3rd Step: Filter Ideas by Finding Suitable Datasets
Note left of 2nd Step: Asks Kaggle for help...
3rd Step -> 4th Step: Seek help from Instructors
4th Step -> 5th Step: Choose 1 Idea and go ALL IN
```
## :memo: Where do I start?

### Step 1: Lets Start by spitballing a few ideas!

- [ ] Anticipate injured numbers in competitive runners / athletes
- [ ] Formula 1 Race Result Predictor / Optimal Race Tactics
- [ ] Soccer Result Predictor
- [ ] Sports Betting --- Top scorer, Match results, MOTM, Cards
- [x] NFL Player Recruitment based off College Attended, Combine Results, Draft Position and Madden Football Statistics.
- [ ] Bitcoin Predictor  --- Positive/Negative sentiments from Twitter?
- [ ] Optimal Golf Swing Video Tracker---- AI GOLF SWING COACH
- [ ] Smart Ticketing --- Ability to move/ swap seats/ earn points midgame.
- [ ] Real Time Player Assesment--- NBA/ NFL/ Soccer (Need to choose one)

:rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket: :rocket:  

# NFL PLAYER PERFORMANCE PREDICTION MODEL

## Overview 

The goal of my project is to build a player performance prediction model for the National Football League (NFL American Football) based on these five factors:

1. College Game Statistics
2. College Attended
3. Combine Performance Results
4. Draft Pick
5. Madden Video Game Player Ratings

The model should consider the first three factors as well as first four years of the players professional playing career based on Madden video game ratings. 

Why 4 years? The length of an NFL rookie (player who is entering the league for the first time) contract is four seasons (along with a fifth year team option for first-round picks which will be explained later). Futhermore, the average career length in the NFL is around four years. As such, this seems like a good length of time to be utilized for prediction. 

**Ultimately, I would like my output to come in TWO FORMS. Firstly, I would like to provide a user interface where a scout, coach or fan could input a number of stats from a players college career. My model should then be able to classify this player into a speficic "tier" of college player. From here I will provide a second user interface where I will use my college prediction in conjunction with my college attended and combine performance data. This model will generate an output in the form of a players predicted performance "tier", using the Madden video game ratings, for years one to four of his professional playing career.** 

**Furthermore, I would like to conclude what kind of performance is needed at the college level in order to get invited to the NFL combine, and how your combine performance could effect where you get drafted but this will be seperate from my model.**

## **College Attended**

![](https://big12fanatics.com/wp-content/uploads/2016/07/cclp5.jpg)

In the NCAA (National Collegiate Athletic Association), there are five major conferences (known as the POWER FIVE). The Power Five encompasses 65 schools, those that make up the five largest and richest conferences in college athletics (ACC, Big Ten, Big 12, Pac-12, SEC) plus Notre Dame. These schools are widely regarded as the upper echelon of NFL pro ready talent. 

However, these 65 schools are just one part of the NCAA football program, meaning there is a plethora of talent elsewhere that may not be getting the appropriate attention from NFL scouts.

> What effect if any does attending one of these schools have on your likelyhood of success at the top level? 

## **Combine Performance Results**

https://www.youtube.com/watch?v=GBgIDBtA9_4)

{%youtube GBgIDBtA9_4 %}

For years, NFL scouts have been searching for the most optimal way to evaluate the potential talent and skill level of collegiate athletes and how well these skills will translate to the professional level. 

In 1982 the NFL Combine was born. The Combine allows the NFL to host workouts and drills that evaluate a player’s speed, strength, agility and IQ all in attempt to learn as much  as possible about these athletes before Draft Day.

>Do stellar combine results guarantee you an ealry draf position? Are they essential to a players success as a pro? 

## **Draft Pick**

![](https://nflops.blob.core.windows.net/cachenflops-lb/4/5/c/0/d/0/45c0d06e12df729c654abe639c54a49acfb3e3d7.jpeg)

Collegiate athletes who have finished their studies or feel that the have the ability to turn pro are able to declare,make themselves available, for the NFL draft.

On Draft day, each of the 32 teams in the NFL receives one pick in each of the seven rounds of the NFL Draft.

The order of these selections are  determined by the reverse order of finish in the previous season. Teams are able to trade picks to one another but barring those each round starts with the team that finished with the worst record and ends with the Champions from the previous season. 

Player performance may be impacted by round and team selection in the draft  as first-round selections should receive more opportunities than seventh-round selections. 

> Are you destined to succeed if you get picked in the first round? Arguably the greatest quarterback of all time is Tom Brady who was picked 199th overall. How could my model explain this? 

## **Madden Video Game Ratings**

![](https://www.madden-school.com/wp-content/uploads/2020/02/OL-21.jpg)

Madden is the only officially licensed National Football League (NFL) video game series in circulation. Think of it as the Fifa of the NFL. Every year a team of rating analysts will rate nearly 3,000 players for the games latest iteration before the NFL makes its final cuts.

Players are created with a mix of physical and mental attributes, measuring things like strength, speed, passing accuracy, and defensive awareness. There are more than 50 different attributes per player and each one is assigned a value between 1 and 100.

A benefit of these ratings is that they provide a continuous output on a consistent scale across both years and positions. A player rated 99 overall is considered to be elite at their position. As such, these ratings could eliminate some of the challenges attatched to quantifying performance specific to that position.

> Could these ratings be used as a proxy for player progression and performance? These rating could certainly be used to segment players into clusters of performing athletes as well as provide a clear trajectory for these players careers to date. Could my model predict what caliber of player you will be in the final year of your rookie contract?  


## Why the NFL? 

Besides my obvious interest in sports, the National Football League (NFL) ranks first on the list of the top ten largest sports leagues by revenue, generating a crazy $16 billion last year. 

According to a study undertaken by Statistica, the most viewed sporting event of 2020 was Super Bowl 54 (The NFL's championship game), which drew in over 100 million viewers in the United States alone. 

Below is snapshot of the money on offer in this league. Bare in mind these 32 players have yet to play a single professional game as they have just left college. 


## 2020 NFL Draft First-Round Rookie Salary Projections
```csvpreview {header="true"}
Pick, Team, Name, Total Contract, Signing Bonus
1st,Bengals,Joe Burrow,$36.0 million,$23.9 million
2nd,Redskins	,Chase Young	,$34.6 million	,$22.7 million
3rd,Lions	,Jeff Okudah	,$33.5 million	,$21.9 million
4th,Giants	,Andrew Thomas	,$32.3 million	,$21.1 million
5th,Dolphins	,Tua Tagovailoa	,$30.3 million	,$19.6 million
6th,Chargers	,Justin Herbert	,$26.6 million	,$16.9 million
7th,Panthers	,Derrick Brown	,$23.6 million	,$14.7 million
8th,Cardinals	,Isaiah Simmons	,$20.7 million	,$12.6 million
9th,Jaguars	,CJ Henderson	,$20.5 million	,$12.5 million
10th,Browns	,Jedrick Wills Jr.	,$19.7 million	,$11.9 million
11th,Jets	,Mekhi Becton	,$18.4 million	,$11.0 million
12th,Raiders	,Henry Ruggs III	,$16.7 million	,$9.7 million
13th,Buccaneers	,Tristan Wirfs	,$16.2 million	,$9.4 million
14th,49ers	,Javon Kinlaw	,$15.5 million	,$8.8 million
15th,Broncos	,Jerry Jeudy	,$15.2 million	,$8.6 million
16th,Falcons	,A.J. Terrell	,$14.3 million	,$8.0 million
17th,Cowboys	,CeeDee Lamb	,$14.0 million	,$7.7 million
18th,Dolphins	,Austin Jackson	,$13.6 million	,$7.5 million
19th,Raiders	,Damon Arnette	,$13.4 million	,$7.3 million
20th,Jaguars	,K'Lavon Chaisson	,$13.3 million	,$7.3 million
21st,Eagles	,Jalen Reagor	,$13.3 million	,$7.2 million
22nd,Vikings	,Justin Jefferson	,$13.1 million	,$7.1 million
23rd,Chargers	,Kenneth Murray	,$13.0 million	,$7.0 million
24th,Saints	,Cesar Ruiz	,$12.7 million	,$6.8 million
25th,49ers	,Brandon Aiyuk	,$12.5 million	,$6.7 million
26th,Packers	,Jordan Love	,$12.4 million	,$6.6 million
27th,Seahawks	,Jordyn Brooks	,$12.3 million	,$6.5 million
28th,Ravens	,Patrick Queen	,$12.2 million	,$6.4 million
29th,Titans	,Isaiah Wilson	,$11.6 million	,$6.0 million
30th,Dolphins	,Noah Igbinoghene	,$11.3 million	,$5.7 million
31st,Vikings	,Jeff Gladney	,$11.0 million	,$5.6 million
32nd,Chiefs,Clyde Edwards-Helaire,$10.8 million,$5.4 million
```

In short, the NFL is a hugely popular and well funded sports league driven by player performance and statistics. If my model is able to predict what a players performance level may be by the time he has finished his rookie contract, it could provide the edge that scouts, teams and fan bases across the league have been looking for. 

# **Data Description**

## 1) College Player Statistics

First off a big thanks to the team at CollegeFootballData.com who allowed me to download each players game statistics for each game of each of the NCAA Football seasons from 2005-2019. I am going to have to group specific stats to each player but I should be able get all fifteen tables into one succint dataframe with all of the stats for each players college career that I need to run meaningful EDA. 

![](https://i.imgur.com/1koKRju.png)
###### Player Game statistics for 2019


## 2) Combine Results

Data.world proved an invaluable resource when it came to this part of my data hunt. They allowed me to access and use the csv file that can be seen below with players combine results from 1987 - 2018. Kaggle provided me with the combine results from 2019 which I will merge with together with the Data.word dataframe. Once again I will only be using the data from 2005-2019. 

As you can probably see below a challenge that I will face with this dataset is missing values. Not all players who get drafted compete in the NFL combine and not all athletes who do show up do all of the events. 
![](https://i.imgur.com/WaFEItN.png)
###### Combine Results 1987-2018


## 3) College Attended + NFL Draft Results

Once again the team at CollegeFootballData.com delivered with a beautifully put together csv file with all of the draft picks from each of the seven draft rounds from 2005-2019.

![](https://i.imgur.com/fHRxnCI.png)

## 4) Madden Player Ratings

I found the final piece of the puzzle thanks to maddenratings.weebly.com. This site is an absolute goldmine for video game ratings and statistics and provided me with a roster spreadsheet file containing full player ratings for all 32 NFL teams from the years 2013-2021. For the period from 2005-2012 I have to download each teams spreadsheet (all 32 of them) and compile them into one csv file for each of the years in that period. The data is complete with no NAN values. 

![](https://i.imgur.com/Q6NpmD9.png)
###### Madden Ratings 2019

## Links to Datasets

The data that I need fall into these 3 categories:

* College Player Statistics
* Colleges Attended (Power 5 or Other)
* Combine Performance Results
* Draft Results (Where was each athlete drafted)
* Madden Ratings 


| Name of Dataset         | Links|
| ----------------- |:----------------------- |
|Github | [:link:][GitHub-Sync] |
|Link Should More Data Need to be Scraped (Combine)| [:link:][Link Should More Data Need to be Scraped (Combine)] | 
|Link Should More Data Need to be Scraped (Madden Ratings)| [:link:][Link Should More Data Need to be Scraped (Madden Ratings)] |
|Reference Paper - Player's Success, Combine Stats and the Universities They Attend| [:link:][Reference Paper - Player's Success, Combine Stats and the Universities They Attend] | 
|Reference Paper - NFL Draft Model using Machine Learning | [:link:][Reference Paper - NFL Draft Model using Machine Learning] |
|Reference Paper - NFL Combine Data Visulization | [:link:][Reference Paper - NFL Combine Data Visulization] |


[GitHub-Sync]:https://github.com/bradbolus/Final-Project-Player-Performance-Prediction-Model.git 
[Link Should More Data Need to be Scraped (Combine) ]:https://www.pro-football-reference.com/draft/2016-combine.html 
[Link Should More Data Need to be Scraped (Madden Ratings)]: https://maddenratings.weebly.com/madden-nfl-20.html   
[Reference Paper - Player's Success, Combine Stats and the Universities They Attend]: https://www.linkedin.com/pulse/players-success-combine-stats-universities-attend-ryan-mclaughlin 
[Reference Paper - NFL Draft Model using Machine Learning]: https://www.reddit.com/r/nfl/comments/b27abi/oc_building_an_nfl_draft_model_using_machine/
[Reference Paper - NFL Combine Data Visulization]: https://nycdatascience.com/blog/student-works/nfl-scouting-combine-data-visualization/

# Project Timeline
### Saturday, Sunday [12/6, 13/6]
- [ ] Clean and sort data. One succinct table with all of my data and one smaller table for college player stats. Goal by the end of the weekend is to have my data in the correct format, merged and ready to start EDA in Google Colab.  
### Mon 14/6 
- [ ] Complete EDA on College Game Stats. Come up with a conclusion as to what kind of stats each position needs in order to be invited to the NFL combine, 
### Tue 15/6
- [ ] Complete EDA on the Combine Results and Draft Picks. Come up with a conclusion as to what kind of performance you would need in the combine to get drafted and how does performing well in the combine affect your draft pick.
### Wed 16/6
- [ ] Define "Tiers of Players". Decide on my model. KNN, Random Forest, SVM, K means Clustering? My model needs to classify players into one of 5 tiers.
### Thurs, Fri [17/6, 18/6]
- [ ] Train-test split the data. Implement model. Run model. Test model. Refine model.
### Sat, Sun [19/6, 20/6]
- [ ] Debug. Overview of project. Have I answered all of the questions I sought to? Is it easy to understand and follow etc. Try to finish most of the programming of the project 

### Mon [21/6]
- [ ] Create Streamlit for project. Develope "input bar" which scout can enter player info to recieve prediction on player performance for years 1-4 of professional career. 
### Tue [22/6]
- [ ] Finalize Github, HackMD and Streamilt.
### Wed [23/6]
- [ ] Create Powerpoint or something similar with which to present.
### Thur [24/6]
- [ ] Refine project and practice presentation/ Pull all nighter to finish! 
### Fri [25/6]
- [ ] Present final project and celebrate!


 






