from typing import Text
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pickle
import xgboost as xgb 


PATH = "/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Final_NFL.csv"

# Create a side menu 
menu = ["Project Overview", "Project Glossary", "Motivation", "Data Dive", "Rookie Analysis", "Can you make it in the NFL?", "Challenges,Aspects to Improve On, Future Work", "References"]
choice = st.sidebar.selectbox('Rookie Player Performance Prediction', menu)
# Create the Home page
if choice == "Project Overview":    
    st.title('Rookie Player Performance Prediction')
    st.image('/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/7-1-20_nfl_logo_jpg.jpeg', use_column_width="always")
    
    st.write("🏈 The goal of this project is to build a player performance prediction model for the National Football League (NFL American Football) based on the following four factors:")
    st.write("1. Rookie Players Game Statistics")
    st.write("2. Selection of Players in the NFL Draft")
    st.write("3. Rookie Players Combine Performance") 
    st.write("4. Madden Video Game Player Ratings") 
    st.write("🏈 The first THREE factors will be analysed in terms of how they affect player ratings on Madden for the FIRST YEAR of these players professional careers.") 
    st.write("🏈 These ratings will be used as a proxy for levels of player performance and will be divided into one of 3 tiers.")
    
    st.write("1. A (Rating: >75)")
    st.write("2. B (Rating: 65-75)")
    st.write("3. C (Rating: <65)") 
   
    st.write("🏈 Ultimately, a user will be able to input certain key statistics pertaining to player performance and recieve an output in the form of a player rating classification for that players FIRST YEAR of his professional career. ")
    
         
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        name = st.text_input("To whom am I speaking?")
        if name: 
            st.header(name) 
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Smiley.jpeg")
            st.header("It sounds to me like you love the NFL?!")
    with col2:
        fan = st.slider('How long have you been a fan?')
        if fan == 0:
            st.write("Give it a go!")
        if fan >0 and fan < 3:
            st.header("Dont worry rookie, I've got your back!")
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/football.jpeg")
        elif fan >= 4 and fan < 10:
            st.header("You have come to the right place my friend!")
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/football.jpeg")
        elif fan >= 10 and fan < 20:
            st.header("We have a seasoned VET on our hands!")
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/football.jpeg")
        elif fan >= 20: 
            st.header("Is that you John Madden?")
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/football.jpeg")
    with col3:
        team = st.selectbox("What is your favourite?", ["Pick a team","ARIZONA CARDINALS", "ATLANTA FALCONS", "BALTIMORE RAVENS", "BUFFALO BILLS", "CAROLINA PANTHERS", "CHICAGO BEARS", "CINCINNATI BENGALS", "CLEVELAND BROWNS", "DALLAS COWBOYS", "DENVER BRONCOS", "DETROIT LIONS", "GREEN BAY PACKERS", "HOUSTON TEXANS", "INDIANAPOLIS COLTS", "JACKSONVILLE JAGUARS", "KANSAS CITY CHIEFS", "LOS ANGELES CHARGERS", "LOS ANGELES RAMS", "MIAMI DOLPHINS", "MINNESOTA VIKINGS", "NEW ENGLAND PATRIOTS", "NEW ORLEAN SAINTS", "NEW YORK GIANTS", "NEW YORK JETS", "OAKLAND RAIDERS", "PHILADELPHIA EAGLES", "PITTSBURGH STEELERS", "SAN FRANCISCO 49ERS", "SEATTLE SEAHAWKS", "TAMPA BAY BUCCANEERS", "TENNESSEE TITANS", "WASHINGTON Football Team"])  
        if team == "Pick a team":
            st.write("Give it a go!")
        elif team == "GREEN BAY PACKERS":
            st.header("Finally another Cheesehead!")
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Packers.jpg")
        elif team != "Pick a team" or team!= "GREEN BAY PACKERS":
            st.header("Ah well, not everyone is perfect!")  
            st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/crying-smiley.png")

elif choice == "Project Glossary":
    st.title("Project Glossary")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football lineup.jpg")
    st.header("American Football is not everyones cup of tea! Here are a couple of key terms and ideas that will help you understand my project")
    st.write("🏈 **National Football League (NFL)**: A professional American football league consisting of 32 teams, divided equally between the National Football Conference (NFC) and the American Football Conference (AFC). Widely considered the pinacle of American Football competition")
    st.write("🏈 **The NFL Draft**: On Draft day, each of the 32 teams in the NFL receives one pick in each of the seven rounds of the NFL Draft.")
    st.write("The order of these selections are determined by the reverse order of finish in the previous season. Teams are able to trade picks to one another but barring those each round starts with the team that finished with the worst record and ends with the Champions from the previous season.")
    st.write("🏈 **The NFL Combine**: The Combine allows the NFL to host workouts and drills that evaluate a player's speed, strength, agility and IQ all in attempt to learn as much as possible about these athletes before Draft Day.")
    st.write("🏈 **The Madden Video Game Series**: An American football video game series developed by EA Sports.")
    st.write("The game contains up to date player ratings, team infomation, football strategy, practice plays and assignments while allowing players to play against simulated opponents or friends of theirs online.")
    st.write("🏈 **Madden Video Game Ratings**: The creators of the game assign numerical values to practically every aspect of every player’s abilities. These ratings are then summarized into an overall player rating, which is a fairly good indication of how skilled a player is and how dominant they will be on the football field. ")
    st.write("For further reading explaining how this ratings are formulated see the **References** Tab ")
    
    st.write("🏈 **Football Positions**: See the graphic below for a short description about where to find each position on the field")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/football_positions_.jpg")
    
    st.write("🏈 **Feature and Label Descriptions**: The Dataset from which I trained my predictive model has 34 distinctive features each with a varying influence on performance." )
    st.write("Additionally, the label I predicted on, Tier_of_Performance, was constructed from Year 1 Madden Video Game Ratings (rating_1)")
    st.write("Below is a table detailing each feature and label")
    st.markdown(
    """
| Features and Labels | Description                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| Rnd                 | Round Selected in Draft (1-7)                                                                                      |
| Pick                | Overall Selection in Draft                                                                                         |
| Position            | Position on the field                                                                                              |
| Age                 | Age of the player before September 1st in draft year                                                               |
| AP1                 | First-team all-pro selections                                                                                      |
| PB                  | Pro Bowl Selections                                                                                                |
| St                  | Number of years as primary starter for his team at his position                                                    |
| CarAV               | Weighted Career Approximate Value                                                                                  |
| DrAV                | Approximate Value accumulated for team that drafted this player                                                    |
| G                   | Games Played                                                                                                       |
| Cmp                 | Passes Completed                                                                                                   |
| Att (Pass)          | Passes Attempted                                                                                                   |
| Yds (Pass)          | Yards Gained by Passing                                                                                            |
| TD (Pass)           | Passing Touchdowns                                                                                                 |
| Int                 | Interceptions thrown                                                                                               |
| Rec                 | Receptions (Catches)                                                                                               |
| Yds (Rec)           | Receiving Yards                                                                                                    |
| TD (Rec)            | Receiving Touchdowns                                                                                               |
| Solo                | Tackles                                                                                                            |
| Int (Def)           | Defensive Interceptions                                                                                            |
| Sacks               | When a defensive player is able to tackle the Quarterback of the apposing team before he is able to pass the ball. |
| Colege/Univ         | University which the player attended                                                                               |
| Year                | Year in which player was drafted                                                                                   |
| Height              | Height in inches                                                                                                   |
| Weight              | Weight in pounds                                                                                                   |
| Hand Size           | Hand size in inches                                                                                                |
| Arm Length          | Arm length in inches                                                                                               |
| 40 yard             | How many secs it takes a player to run 40 yards from a standing start                                              |
| Bench Press         | How many times a player can consecutively bench press 225 pounds                                                   |
| Vert Leap           | How high a player can jump vertically from a standing start in inches                                              |
| Broad Jump          | How far a player can jump forwards in inches from a standing start                                                 |
| Shuttle             | How many secs it takes a player to complete the Shuttle Drill. See video: https://www.youtube.com/watch?v=1Ik4_GjdrJw                                          |
| 3Cone               | How many secs it takes a player to complete the 3Cone Drill. See video: https://www.youtube.com/watch?v=OmvERmXLlmU                                           |
| rating_1            | Madden Overall Rating for a players first year                                                                     |
| Tier_of_Performance | Grouped Madden Overall ratings for players into three tiers: A, B and C 
"""
)

elif choice == 'Motivation':
    # Layout your content
    st.title("Project Motivation")
    
    st.image(["/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football4.gif", "/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football1.gif"])
    st.image(["/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football5.gif", "/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football.gif" ])
    
    st.write("🏈 Besides my obvious interest in sports, the National Football League (NFL) ranks first on the list of the top ten largest sports leagues by revenue, generating a crazy $16 billion last year.")
    st.write("🏈 According to a study undertaken by Statistica, the most viewed sporting event of 2020 was Super Bowl 54 (The NFL’s championship game), which drew in over 100 million viewers in the United States alone.")
    st.write("🏈 Below is snapshot of the money on offer in this league. Bare in mind these 32 players have yet to play a single professional game as they have just left college.")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Rookie Draft Contracts.png")
    st.write("🏈 In short, the NFL is a hugely popular and well funded sports league driven by player performance and statistics.") 
    st.write("🏈 If my model is able to predict what a players performance level may be by the time he begins his rookie contract, it could provide the edge that scouts, teams and fan bases across the league have been looking for.") 

    hype = st.selectbox('Still with me?', ["", "Yes!", "You lost me at NFL"]) 
    
    if hype == "Yes!":
        st.write("Perfect lets carry on!")
        st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Football3.gif")
    elif hype == "You lost me at NFL":
        st.write("Here is a quick crash course : https://www.youtube.com/watch?v=3t6hM5tRlfA ")   
                
    
elif choice == "Data Dive":
    st.title("Data Dive")
    st.header("My data came in THREE forms...")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/DataPic.png")
    
    st.header("1: Player Game Statistics")
    
    st.write("🏈 Format: Player Game Statistics from 2007-2019 in CSV format")
    
    st.write("🏈 Task: Clean, Sort and Concatinate 13 CSVs into one succinct, useable dataframe")
    
    st.write("🏈 Challenges: Creating a unique column key, Misunderstood stat types")
    
    st.header("2: Player Combine Results")
    st.write("🏈 Format: Player Combine Results in two seperate CSV files (1987-2018, 2019) ")
    st.write("🏈 Task: Clean, Sort and Concatinate 2 CSVs into useable dataframe. Deal with Missing Values.")
    st.write("🏈 Challenges: Missing values, Creating a unique column key, Filtering for correct period")
    
    st.header("3: Madden Video Game Ratings")
    st.write("🏈 Format: Madden Video Game Ratings (2013-2019) in yearly CSV format. 2007-2011 scraped from maddenratings.weebly.com by team (32 CSV files for each year)")
    st.write("🏈 Task: Scraping, Cleaning, Sorting and Concatinate 32 CSVs from each team into one dataframe for 2007-2011, Concatinate with data from 2013-2019")
    st.write("🏈 Challenges: MANY!")

    st.title("Player Dataset After Preprocessing")
    # Load data
    @st.cache
    def load_data(path):
        return pd.read_csv(path)
    data = load_data("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_export_dataframe.csv")
    st.dataframe(data)
    st.write("3225 Unique Player Entries. 48 Features. These numbers will change and that change will be explained later.")
    

# Create the Second page
elif choice == "Rookie Analysis":
    st.title('Rookie Analysis')
    st.image('/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/NFL Rookies.jpg')
    st.write("🏈 My first step was to take this dataset and filter it for players with less than 50 career games.")
    st.write("🏈 My motivation for this is driven by the goal of this project. To predict the next big NFL prospect coming out of college. Unfortunately, due to a mishap with my data (to be detailed later), this was the proxy used for Rookie Career Stats")
    
    st.header("Rookie Dataset")
    # Load data
    @st.cache
    def load_data(path):
        return pd.read_csv(path)
    
    data = load_data("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_ROOKIES_FINAL.csv")
    st.dataframe(data)
    
    st.header("Rookie Data Description")
    st.write("Game statistics from 1495 Players who have played less than 50 career games.") 
    st.write("Data on where these players were drafted in their respective draft classes, combine performance data and Madden NFL player ratings for these players first year in the league.")
    
    st.header("EDA of Rookie Dataset")
    st.write("My project centers around player performance. As such the questions I sought to answer revolved around how the different features in my dataset influenced and interacted with Year 1 Madden Ratings")

    st.header("Question 1: Does Early Draft Selection Influence First Year Madden Ratings? ")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Early Draft Pick MAdden Rating.png")
    st.write("🏈 Above is a scatterplot showing the relationship between when a player gets drafted (X-axis) and what that players first year madden rating is (Y-axis)")
    st.write("🏈  We can see a positive correlation as the higher you get drafted the more likely you are to have a stellar first year rating")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Late Draft Pick  Madden Rating.png")
    st.write("🏈  Next I wanted to investigate high performing players picked in later rounds as seen above")
    st.write("🏈  There doesnt seem to be too many instances of Tier A  performers picked in later rounds but....")
    st.write(" Lets take a deeper look at the late round high performers")
    st.dataframe(pd.read_csv("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_Kickers.csv"))
    st.write("🏈  Interestingly, of the players who were picked after the 5th Round and who recieved an A Tier Player Rating, 7 out of 10 of them play on Special Teams as either Kickers or Punters.") 
    st.write("🏈  This makes sense as these positions are seldom drafted in the 1st round as they are not deemed to be 'game changing' positions but could still be given a good rating on Madden as they may excel at their specific position.")
    
    st.header("Question 2: Is Early Draft Selection a Precursor for a Player Appearing in at Least 1 Pro Bowl or 1 All Pro Team? ")
    st.write("🏈 Pro Bowls are the All-star games for the NFL. It matches the top players of each season in leagues two conferences (American Football Conference (AFC) and National Football Conference (NFC)) in a once off game. Players are selected based on fan votes as well as their performance in the season")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Pro Bowl Boxplot.png")
    st.write("🏈 As you can see from the boxplot there does seem to be a positive relationship between getting picked early and appearing in a Pro Bowl later in your career")
    st.write("🏈 Pro Bowls have massive implications for endorsements and contract extensions as it essentially means you are a high performing fan favorite ")
    
    st.write("🏈 The All Pro First Team is an honor given to the best player at each position during a given season")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/AP1 Boxplot.png")
    st.write("🏈 The analysis does not seem too conclusive when it comes down to AP1 selection vs early draft selection.")
    st.write("🏈 Early draft selection is not a conclusive indicator of recieving this honor")
    
    st.header("Question 3: Which Rookie Career Playing Stats are the Most Highly Correlated with High Performance in Year 1? ")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Career Stats Heatmap.png")
    st.write("🏈 Shown above is a correlation heatmap of Rookie Career stats to Madden Year 1 Ratings.")
    st.write("🏈 The larger the numbers next to each player stat the more positively correlated that stat is to player performance in Year 1")
    st.write("🏈 As you can see the three standout features are: Games Played, Defensive Interceptions and Sacks")
    st.write("🏈 What this means is that the bigger the body of work a player has (the more games he has played) the better his Madden Year 1 rating seems to be.")
    st.write("🏈 The same can be said for Interceptions and Sacks which occur on a rare basis and are big contributing factors to game outcomes from a defensive teams standpoint.")
    
    st.header("Question 4: How do Combine Events correlate to Performance?")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Combine Events vs Player Performance.png")
    st.write("🏈 These numbers dont seem to indicate much! It would appear that performance in the Bench Press and Broad Jump events are positively correlated with First Year Madden Ratings.") 
    st.write("🏈 The problem with the combine dataset is that very few atheletes compete in every event.")
    st.write("🏈  Rookie stars in the making may look at the combine as a lose-lose with a poor event performance hurting their draft stock more than simply not attending.")
    st.write("🏈 As such, lets try impute the missing values using a Baysian Imputer to see if we can get as accurate as possible measurements.")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Fit Imputer.png")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Transform Imputer.png")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Correlation after Imputation.png")
    st.write("🏈 Iterative imputation refers to a process where each feature is modeled as a function of the other features, e.g. a regression problem where missing values are predicted. Each feature is imputed sequentially, one after the other, allowing prior imputed values to be used as part of a model in predicting subsequent features.")
    st.write("🏈 After imputation correlation decreased. The results are still quite inconclusive but an atheletes performance in the Broad Jump (in) and Vertical Leap(in) have the largest effect of the the combine events on athelete first year performance and rating.")
    st.write("🏈 Somthing to work on for next time!")
    
    
    st.header("Question 5: Which Positions are the Most Sought After?  Do the Physical Measurements,such as Height and Weight, of these positions have any baring on their success in the league? ")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Position Count.png")
    st.write("🏈 Above is a breakdown of the total amount of each position drafted between 2007-2019")
    st.write("🏈 Examining the data one can see that the most coverted or most populated position is Wide Reciever followed by Runningbacks (HB), Defensivebacks (DB), Linebackers(LB) and Defensive Ends (DE).")
    st.write("🏈 Lets take a closer look at these 5 positions as well as quarterbacks by grouping them into three groups.")
    st.write("**1. Quarterbacks**")
    st.write("**2. Wide Recievers and Runningbacks**")
    st.write("**3. Defensive Players**")

    st.write("**Quarterbacks**")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/QB.png")
    st.write("🏈  At the quarterback position the data tells us that both Hand Size (in) and Weight (lbs) are resonably highly correlated with high performance in year 1.")
    st.write("🏈  This is interesting and makes sense for two reasons.")
    st.write("🏈  First the quarterbacks main job is to throw the football. Bigger hands may mean a better grip of the football in cold weather games and fewer bad throws for interceptions from the other team.")
    st.write("🏈  Second, a quarterback is the most important position on the field with teams placing a huge amount of value at the position. As such, it is incredibly important these players stay injury free. A thicker-set quarterback may be able to absorb more punishment on the field and stay injury free for longer.")

    st.write("**Wide Recievers and Runningbacks**")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/RB:WR.png")
    st.write("🏈  Weight seems to play a big factor in success for running backs and wide recievers while Age is negatively correlated which is unsurprising and will be shown highlighted further down.")
    
    st.write("**Defensive Players**")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/DEF.png")
    st.write("🏈  On the defensive side of the ball the most important physical feature seems to be Arm Length (in).") 
    st.write("🏈  Again this is interesting and makes sense as defensive players need to make use of there arms to get past offensive players whose job is to block some of them from tackling the quarterback.")
    
    st.header("Question 6: Does a players College Team Play a Role in where they get Drafted and in turn what their Player Performance is After Year 1?? ")
    st.write("🏈 Sporting News ranked all the FBS College Football programs over their past 10 seasons.")
    st.write("🏈 They used a formula in order to bridge the Bowl Championship Series and College Football Playoff eras")  
    st.write("🏈 Here are the categories they used: ")
    st.write("**National championships: 10 points each**")
    st.write("**National title game appearances: 5 points each**")
    st.write("**College Football Playoff appearances: 5 points each**")
    st.write("**New Years Day Six/BCS bowl appearances: 3 points each**")
    st.write("**Heisman Trophy winners: 2 points each **")
    st.write("🏈 For the sake of my analysis I will be looking at the top 15 Schools from this list over the last decade vs the rest.")

    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/School Pie Charts.png")
    st.write("🏈 Above is a breakdown of Tier A, B and C performing players and the college which they attended.")
    st.write("🏈 Interestingly, the Tier A performers have a larger percentage of players from these top 15 'Power' schools")
    st.write("🏈 This can be explained by the recruitment process of young players in the American Football.")
    st.write("🏈 Recruitment starts young and is very though with highschool and middleschool minicamps for evaluating young talent commonplace throughout the year in varying parts of the country")
    st.write("🏈 As such players we are equipped with the skills to succeed are scouted early and recruited to colleges with the biggest budgets and best records")
    
    st.header("EDA Conclusions")
    st.write("🏈  **High draft selection** is mostly positively correlated with a players first year performance (with the exception of some examples in certain positions like kickers and punters)")
    st.write("🏈  While draft selection appears to be a precurser for future Pro Bowl selection it **does not** appear to indicate future All-Pro Team selection")
    st.write("🏈  **Games Played, Defensive Interceptions and Sacks** seem to be the most important features from Rookie Career playing statistics in positively influencing first year performance")
    st.write("🏈  While the correlations are less impressive, it appears that the **three most important combine events** to perform well in are the **Bench Press, Broad Jump and Vertical Leap**")
    st.write("🏈  **Wide Reciever (WR), Runningbacks (HB), Defensivebacks (DB), Linebackers(LB) and Defensive Ends (DE)** are the five most sought after or populated positions in the NFL draft ")
    st.write("🏈  The most correlated **physical features** with improved first year performance for a **Quarterback** are: **Hand Size and Weight**")
    st.write("🏈  The most correlated **physical feature** with improved first year performance for **Wide Recievers and Runningbacks** is: **Weight**")
    st.write("🏈  The most correlated **physical feature** with improved first year performance for **Defensive players** is: **Arm Length**")
    st.write("🏈  Relatively speaking, there is a high percentage chance of you recieveing a Tier A player rating if you go to a **Top 15 school**")
# Create the Sixth page
elif choice == "Can you make it in the NFL?":
    st.title("Can you make it in the NFL?")
    st.image('/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Madden Ratings.png')
    st.title("Model Explanation")
    st.header("Model Choice")
    st.write("🏈 In total I tried out 5 models for my problem...")
    st.write("**1. Random Forest Classifier**")
    st.write("**2. KNN Classifier**")
    st.write("**3. Linear SVM**")
    st.write("**4. LightGBM Classification Model**")
    st.write("**5. XGBoost Classifier**")
    st.write("🏈 In the end I settled on the XGBoost Classifier Machine Learning Model as it yielded the best results for my dataset")

    st.header("XGBoost")
    st.write("🏈  XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable.")
    st.write("🏈  XGBoost utilizes parallel tree boosting to solve, in this case a classification problem, in a fast and accurate way.")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/XGB Explanation.png")
    st.write("🏈  XGBoost is used Supervised Machine Learning problems (i.e problems with labelled data) ")
    st.write("🏈  XGBoost is comprised of a tree ensemble model which consists of a set of classification and regression trees (CART).")
    st.write("🏈  Hyperparameters and other configurations are used in conjunction with CART when building the model.")
    st.write("🏈  Optimal Hyperparameters can be found using a Gridsearch which considers all given parameter combinations in order to find an optimal combination of hyperparameters for your specific data")

    st.header("Model Methodology")
    st.write("1.Drop Missing values for Labels") 
    st.write("2.Add Tier Performance Column Based on Madden Ratings (converted to float)")
    st.write("3.Seperate labels and features")
    st.write("4.Drop unnessasary Feature columns") 
    st.write("**5.Label Encoded Categorical Features**")
    st.write("**6.Imputed missing values of features- Bayesian Iterative Imputer**")
    st.write("7.Normalized the data by Standard Scalar") 
    st.write("**8.Imported Smote to deal with unbalanced data**")
    st.write("9.Performed a train test split on the data (0.2 test size)")
    st.write("10.Gridsearch for optimal XGBoost parameters.") 
    st.write("11.Fit and predict XGBoost Machine Learning Model on balanced data.")
    st.write("12.Evaluate model using classification report.") 
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Classification Report.png")
    st.write(" 🏈 Accuracy on the Test set of 81 percent and 91 percent on the Training Set")

    st.header("What does this mean?")
    st.write("🏈 Essentially what it means is that my model is able to predict player performance in the correct tier (A, B or C), 81 percent of the time on unseen/new data.")
    st.write("🏈 Precision is the ability of a classifier not to label an instance positive that is actually negative.")
    st.write("🏈 F1 scores embed precision and recall into their computation.")
    st.write("🏈 An F1 score closer to 1 means that the model has low false positives and low false negatives, so its correctly identifying positive and negative predictions. An F1 score closer to 0 means pro accuracy of prediction in the model")
    
    st.header("Player Predictor")
    st.write("**Why not give it a try yourself? Adjust the inputs below to find out your first year player rating!**")
    
    Position_list = ['QB', 'DE', 'DT', 'LB', 'TE', 'G', 'C', 'T', 'HB', 'WR', 'S', 'CB',
    'P', 'K', 'ILB', 'OLB', 'DL', 'LS', 'OL', 'DB', 'FB', 'NT']
    Position_list_nums = [17,  3, 5, 11, 20,  7,  0, 19,  8, 21, 18,  1, 16,
    10,  9, 15,  4, 12, 14,  2,  6, 13]
    College_list = ['Oklahoma', 'Ohio St.', 'Alabama', 'Clemson', 'LSU', 'Duke',
       'Iowa', 'Michigan', 'Boston Col.', 'Florida St.',
       'North Carolina St.', 'Washington St.', 'Alabama St.',
       'Mississippi St.', 'Notre Dame', 'TCU', 'Washington',
       'Arizona St.', 'Temple', 'Florida', 'South Carolina',
       'Central Michigan', 'Kansas St.', 'Missouri', 'Hawaii',
       'Vanderbilt', 'Utah', 'Texas A&M', 'Mississippi', 'Penn St.',
       'Northern Illinois', 'Georgia', 'Central Florida', 'Delaware',
       'Massachusetts', 'Virginia', 'Toledo', 'San Jose St.', 'Iowa St.',
       'Florida Atlantic', 'Wisconsin', 'BYU', 'Michigan St.',
       'Western Illinois', 'Louisiana Tech', 'San Diego St.', 'Stanford',
       'USC', 'Auburn', 'Old Dominion', 'Murray St.', 'Kentucky',
       'West Virginia', 'Boise St.', 'East. Michigan', 'Oklahoma St.',
       'Arkansas', 'Miami (FL)', 'Wake Forest', 'Memphis', 'Houston',
       'Indiana', 'Charleston (WV)', 'Pittsburgh', 'Oregon', 'Minnesota',
       'Maryland', 'Texas', 'Tarleton St.', 'North Dakota St.',
       'North Carolina', 'Fresno St.', 'Rutgers', 'Washburn', 'Colorado',
       'SE Missouri St.', 'Wyoming', 'Bowling Green', 'Utah St.',
       'Illinois', 'James Madison', 'Prairie View A&M', 'Cincinnati',
       'Idaho', 'Colorado St.', 'Morgan St.', 'Texas Tech', 'UCLA',
       'Texas-San Antonio', 'Virginia Tech', 'Louisville', 'Nevada',
       'Texas-El Paso', 'South Carolina St.', 'SMU', 'South Dakota St.',
       'Sam Houston St.', 'North Carolina A&T', 'Fort Hays St.',
       'Louisiana', 'Tennessee', 'South Florida', 'Western Michigan',
       'Humboldt St.', 'Southern Miss', 'Richmond', 'Western Kentucky',
       'Weber St.', 'New Mexico St.', 'Fordham', 'S.F. Austin', 'Purdue',
       'Pennsylvania', 'Illinois St.', 'Arizona', 'Jacksonville St.',
       'Tulane', 'Connecticut', 'Maine', 'Central Arkansas', 'Yale',
       'Virginia St.', 'Wagner', 'Appalachian St.', 'California', 'Ohio',
       'New Mexico', "Unknown", 'Syracuse', 'Ferris St.', 'Middle Tenn. St.',
       'Western Carolina', 'Northwestern', 'Ashland', 'Youngstown St.',
       'Grambling St.', 'Lamar', 'Oregon St.', 'San Diego', 'Drake',
       'West Georgia', 'Georgia Southern', 'Nebraska', 'Coastal Carolina',
       'Georgia St.', 'Chattanooga', 'East Central (OK)', 'Buffalo',
       'Baylor', 'East. Kentucky', 'Northern Iowa', 'Harvard',
       'La-Monroe', 'Georgia Tech', 'Montana', 'Navy',
       'Southeastern Louisiana', 'Miami (OH)', 'Texas St.',
       'Texas Southern', 'Kansas', 'Towson', 'Ala-Birmingham', 'Monmouth',
       'Northwestern St. (LA)', 'East. Washington', 'Newberry',
       'William & Mary', 'Eastern Illinois', 'Kent St.', 'Bloomsburg',
       'Tennessee St.', 'Arkansas St.', 'Ball St.', 'NW Missouri St.',
       'Concordia-St.Paul (MN)', 'South Dakota', 'Marshall',
       'Valdosta St.', 'UT Martin', 'California (PA)',
       'Florida International', 'Southern Utah', 'Harding', 'Albion',
       'Troy', 'Rice', 'West. Michigan', 'Abilene Christian', 'Lehigh',
       'Missouri State', 'Alabama A&M', 'Long Beach CC', 'Indiana (PA)',
       'Southern Illinois', 'East Carolina', 'Cal Poly-San Luis Obispo',
       'UNLV', 'McNeese St.', 'Jackson St.', 'Army', 'Akron',
       'Nicholls St.']
    college_number_list = [126, 125,   3,  32,  79,  40,  70,  95,  20,  51, 117, 189,   5,
       100, 123, 157, 188,   9, 159,  48, 146,  28,  76, 101,  62, 181,
       178, 163,  99, 131, 119,  55,  27,  38,  90, 182, 169, 145,  71,
        49, 199,  15,  96, 195,  85, 144, 155, 175,  14, 128, 106,  78,
       192,  19,  44, 127,  10,  93, 186,  92,  63,  68,  29, 133, 129,
        98,  89, 162, 158, 118, 115,  54, 138, 187,  34, 140, 200,  21,
       179,  66,  74, 134,  31,  65,  35, 105, 166, 173, 168, 184,  86,
       110, 167, 147, 141, 149, 142, 116,  53,  84, 160, 150, 197,  64,
       153, 137, 196, 190, 112,  52, 139, 135, 132,  67,   8,  73, 172,
        37,  87,  26, 201, 183, 185,   7,  24, 124, 111, 177, 156,  47,
        97, 194, 121,  13, 202,  59,  81, 130, 143,  39, 191,  56, 109,
        33,  57,  30,  42,  22,  17,  43, 120,  61,  80,  58, 104, 108,
       151,  94, 165, 164,  75, 170,   2, 103, 122,  45, 113, 198,  46,
        77,  18, 161,  11,  16, 107,  36, 148,  88, 180, 176,  25,  50,
       154,  60,   6, 171, 136, 193,   0,  82, 102,   4,  83,  69, 152,
        41,  23, 174,  91,  72,  12,   1, 114]
    
    model_features = ['Rnd', 'Pick', 'Pos', 'Age', 'AP1', 'PB', 'St', 'CarAV', 'DrAV', 'G',
    'Cmp', 'Att (Pass)', 'Yds (Pass)', 'TD (Pass)', 'Int', 'Att (Rush)',
    'Yds (Rush)', 'TD (Rush)', 'Rec', 'Yds (Rec)', 'TD (Rec)', 'Solo',
    'Int (Def)', 'Sacks', 'College/Univ', 'Height (in)', 'Weight (lbs)',
    'Hand Size (in)', 'Arm Length (in)', '40 Yard', 'Bench Press',
    'Vert Leap (in)', 'Broad Jump (in)', 'Shuttle', '3Cone']
    
    model_path = "/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/xgboostsmote.pkl"
    
    model = pickle.load(open(model_path, "rb"))

    # Load data
    @st.cache
    def load_data(path):
        return pd.read_csv(path)
    
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Nick Bosa.jpg")
    st.write("**This is Nick Bosa.**") 
    st.write("**He plays Defensive End (DE) and was selected 2nd in the 2019 NFL Draft by the San Francisco 49ers.**")
    st.write("**He recieved a Madden First Year Rating of 78 and as such he falls into my Tier A performance bracket**")
    st.write("**To save time I have input his stats already**")
    data_bosa = load_data("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_bosa.csv")
    st.dataframe(data_bosa)
    
    # form_round = st.form("round")
    
    # def pick(round):
    #     if Round == 1:
    #         Pick == form.slider("Which number were you picked?", min_value = 1, max_value = 32)
    #     elif Round == 2:
    #         Pick == form.slider("Which number were you picked?", min_value = 33, max_value = 64)
    #     elif Round == 3:
    #         Pick == form.slider("Which number were you picked?", min_value = 65, max_value = 96)
    #     elif Round == 4:
    #         Pick == form.slider("Which number were you picked?", min_value = 97, max_value = 128)
    #     elif Round == 5:
    #         Pick == form.slider("Which number were you picked?", min_value = 129, max_value = 160)
    #     elif Round == 6:
    #         Pick == form.slider("Which number were you picked?", min_value = 161, max_value = 192)
    #     elif Round == 7:
    #         Pick == form.slider("Which number were you picked?", min_value = 193, max_value = 255)
    #     return Pick    
    # Button = form_round.form_submit_button("Submit the Round you were drafted!")
    st.write("**Tips before you start**")
    st.write("🏈 CarAv from 0-50. 75 percent of the players in this dataset had a rating of 10 or below.") 
    st.write("🏈 High-end draft picks CarAV ranged from 15 - 35")
    st.write("🏈 DrAV from 0-50. Should input the same value as CarAV")
    
    form = st.form("my_form")
    
    Round = form.slider("Which round were you picked?", min_value = 1, max_value = 7, value = 1)
    Pick = form.slider("Which number were you picked?", min_value = 1, max_value = 255, value = 2) 
    Pos= form.selectbox("Which position do you play?", Position_list)
    Age= form.slider("How old are you", min_value = 18, max_value = 50, value = 21)
    AP1= form.slider("How many All Pro 1st Team selections do you have?", min_value = 0, max_value = 15)
    PB = form.slider("How many Pro Bowl Selections do you have?", min_value = 0, max_value = 15, value = 1)
    St = form.slider("How many years have you been a starter on your team?", min_value = 0, max_value = 15, value = 1)
    CarAV = form.slider("What is your Career Weighted Average?", min_value = 0, max_value = 50, value = 13)
    DrAV = form.slider("What is your Draft Weighted Average of the team that selected you?", min_value = 0, max_value = 50, value = 13)
    G = form.slider("How many games have you played in your career?", min_value = 0, max_value = 50, value = 18)
    Cmp = form.slider("How many passes have you completed as a Quarterback?", min_value = 0, max_value = 1500, step = 10)
    Att_Pass = form.slider("How many career pass attempts do you have?", min_value = 0, max_value = 2000, step = 10)
    Yds_Pass = form.slider("How many career passing yards do you have?", min_value = 0, max_value = 15000, step = 50)
    TD_Pass = form.slider("How many caeer TD passes do you have?", min_value = 0, max_value = 200)
    Int = form.slider("How many career interceptions have you thrown?", min_value = 0, max_value = 200)
    Att_Rush= form.slider("How many career rushing attempts do you have?", min_value = 0, max_value = 1000, step = 25)
    Yds_Rush = form.slider("How many career rushing yards do you have?", min_value = 0, max_value = 4000, step = 20)
    TD_Rush = form.slider("How many rushing TDs do you have?", min_value = 0, max_value = 150, step = 5)
    Rec = form.slider("How many career receptions do you have?", min_value = 0, max_value = 500, step = 5)
    Yds_Rec = form.slider("How many career recieving yards do you have?", min_value = 0, max_value = 5000, step = 50)
    TD_Rec = form.slider("How many career recieving touchdowns do you have?", min_value = 0, max_value = 500, step = 5)
    Solo = form.slider("How many tackles have you made in your career?", min_value = 0, max_value = 500, value = 35)
    Int_Def = form.slider("How many defensive interceptions have you made in your career?", min_value = 0, max_value = 250, value = 1)
    Sacks = form.slider("How many sacks have you made in your career?", min_value = 0, max_value = 400, step = 2, value = 9)
    College = form.selectbox("Which College did you attend?", College_list)
    
    
    Height_inches = form.slider("How tall are you in inches?", min_value = 0.0, max_value = 100.0, step= 0.5, value = 76.0)
    Weight_lbs = form.slider("How heavy are you in pounds?", min_value = 0.0, max_value = 500.0, step = 0.5, value = 266.0)
    Hand_Size_inches = form.slider("How big is your hand in inches?", min_value = 0.0, max_value = 15.0, step = 0.5, value = 10.5)
    Arm_Length_inches = form.slider("How long is your Arm in inches?", min_value = 0.0, max_value = 45.0, step = 0.5, value = 33.0)
    Forty_yard_dash = form.slider("How fast do you run the 40 yard dash?", min_value = 0.0, max_value = 15.0, step= 0.05, value = 4.8)
    Bench_Press = form.slider("How many times can you bench press 225 pounds?", min_value = 0.0, max_value = 60.0, step = 1.0, value = 29.0)
    Vert_Leap_inches = form.slider("How high can you jump in inches?", min_value = 0.0, max_value = 60.0, step=0.5, value = 33.5)
    Broad_Jump_inches = form.slider("How long is your broad jump in inches?", min_value = 0.0, max_value = 160.0, step = 0.5, value = 116.0)
    Shuttle = form.slider("How fast can you complete the shuttle drill?", min_value = 0.0, max_value = 15.0, step= 0.5, value = 7.0)
    Three_Cone = form.slider("How fast can you complete the 3Cone drill?", min_value = 0.0, max_value = 15.0, step = 0.25, value = 4.25)
    
    Button = form.form_submit_button("Press for a bit of magic!")

    # x = np.array([[Round, Pick, Pos, Age, AP1, PB, St, CarAV, DrAV, G, Cmp, Att_Pass, Yds_Pass, TD_Pass, Int, Att_Rush, Yds_Rush, TD_Rush,
    #     Rec, Yds_Rec, TD_Rec, Solo, Int_Def, Sacks, College_list.index(College), Height_inches, Weight_lbs, Hand_Size_inches, Arm_Length_inches, Forty_yard_dash, Bench_Press,
    #     Vert_Leap_inches, Broad_Jump_inches, Shuttle, Three_Cone, 1]])

    # st.write(model.predict(x))  
    
    if Button:
        st.header("Player Prediction:")
        st.write(model.predict(np.array([[Round, Pick, Position_list.index(Pos), Age, AP1, PB, St, CarAV, DrAV, G, Cmp, Att_Pass, Yds_Pass, TD_Pass, Int, Att_Rush, Yds_Rush, TD_Rush,
        Rec, Yds_Rec, TD_Rec, Solo, Int_Def, Sacks, College_list.index(College), Height_inches, Weight_lbs, Hand_Size_inches, Arm_Length_inches, Forty_yard_dash, Bench_Press,
        Vert_Leap_inches, Broad_Jump_inches, Shuttle, Three_Cone]])))
        
        # if prediction[0] == "A":
        #     st.write("Hi")
        
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Payne.jpg")
    st.write("This is Justin Layne. He was selected 83rd overall in the 3rd Round by the Pitsburgh Steelers and plays Corner Back.")
    st.write("His first year Madden Rating was 69 and as such falls into my B Tier for player performance")
    data_layne = load_data("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_layne.csv")
    st.dataframe(data_layne)

    form3 = st.form("patrick_form")
    
    Round = form3.slider("Which round were you picked?", min_value = 1, max_value = 7, value = 3)
    Pick = form3.slider("Which number were you picked?", min_value = 1, max_value = 255, value = 83) 
    Pos= form3.selectbox("Which position do you play?", Position_list)
    Age= form3.slider("How old are you", min_value = 18, max_value = 50, value = 21)
    AP1= form3.slider("How many All Pro 1st Team selections do you have?", min_value = 0, max_value = 15)
    PB = form3.slider("How many Pro Bowl Selections do you have?", min_value = 0, max_value = 15)
    St = form3.slider("How many years have you been a starter on your team?", min_value = 0, max_value = 15)
    CarAV = form3.slider("What is your Career Weighted Average?", min_value = 0, max_value = 50, value = 2)
    DrAV = form3.slider("What is your Draft Weighted Average of the team that selected you?", min_value = 0, max_value = 50, value = 2)
    G = form3.slider("How many games have you played in your career?", min_value = 0, max_value = 50, value = 26)
    Cmp = form3.slider("How many passes have you completed as a Quarterback?", min_value = 0, max_value = 1500, step = 10)
    Att_Pass = form3.slider("How many career pass attempts do you have?", min_value = 0, max_value = 2000, step = 10)
    Yds_Pass = form3.slider("How many career passing yards do you have?", min_value = 0, max_value = 15000, step = 50)
    TD_Pass = form3.slider("How many caeer TD passes do you have?", min_value = 0, max_value = 200)
    Int = form3.slider("How many career interceptions have you thrown?", min_value = 0, max_value = 200)
    Att_Rush= form3.slider("How many career rushing attempts do you have?", min_value = 0, max_value = 1000, step = 25)
    Yds_Rush = form3.slider("How many career rushing yards do you have?", min_value = 0, max_value = 4000, step = 20)
    TD_Rush = form3.slider("How many rushing TDs do you have?", min_value = 0, max_value = 150, step = 5)
    Rec = form3.slider("How many career receptions do you have?", min_value = 0, max_value = 500, step = 5)
    Yds_Rec = form3.slider("How many career recieving yards do you have?", min_value = 0, max_value = 5000, step = 50)
    TD_Rec = form3.slider("How many career recieving touchdowns do you have?", min_value = 0, max_value = 500, step = 5)
    Solo = form3.slider("How many tackles have you made in your career?", min_value = 0, max_value = 500, value = 16)
    Int_Def = form3.slider("How many defensive interceptions have you made in your career?", min_value = 0, max_value = 250)
    Sacks = form3.slider("How many sacks have you made in your career?", min_value = 0, max_value = 400, step = 2)
    College = form3.selectbox("Which College did you attend?", College_list)
    
    
    Height_inches = form3.slider("How tall are you in inches?", min_value = 0.0, max_value = 100.0, step= 0.5, value = 74.0)
    Weight_lbs = form3.slider("How heavy are you in pounds?", min_value = 0.0, max_value = 500.0, step = 0.5, value = 192.0)
    Hand_Size_inches = form3.slider("How big is your hand in inches?", min_value = 0.0, max_value = 15.0, step = 0.25, value = 9.25)
    Arm_Length_inches = form3.slider("How long is your Arm in inches?", min_value = 0.0, max_value = 45.0, step = 0.5, value = 33.0)
    Forty_yard_dash = form3.slider("How fast do you run the 40 yard dash?", min_value = 0.0, max_value = 15.0, step= 0.05, value = 4.5)
    Bench_Press = form3.slider("How many times can you bench press 225 pounds?", min_value = 0.0, max_value = 60.0, step = 1.0)
    Vert_Leap_inches = form3.slider("How high can you jump in inches?", min_value = 0.0, max_value = 60.0, step=0.5, value = 37.5)
    Broad_Jump_inches = form3.slider("How long is your broad jump in inches?", min_value = 0.0, max_value = 160.0, step = 0.5, value = 134.0)
    Shuttle = form3.slider("How fast can you complete the shuttle drill?", min_value = 0.0, max_value = 15.0, step= 0.05, value = 7.0)
    Three_Cone = form3.slider("How fast can you complete the 3Cone drill?", min_value = 0.0, max_value = 15.0, step = 0.05, value = 4.0)
    
    Button_ben = form3.form_submit_button("Press for a bit of magic!")

    # x = np.array([[Round, Pick, Pos, Age, AP1, PB, St, CarAV, DrAV, G, Cmp, Att_Pass, Yds_Pass, TD_Pass, Int, Att_Rush, Yds_Rush, TD_Rush,
    #     Rec, Yds_Rec, TD_Rec, Solo, Int_Def, Sacks, College_list.index(College), Height_inches, Weight_lbs, Hand_Size_inches, Arm_Length_inches, Forty_yard_dash, Bench_Press,
    #     Vert_Leap_inches, Broad_Jump_inches, Shuttle, Three_Cone, 1]])

    # st.write(model.predict(x))  
    
    if Button_ben:
        st.header("Player Prediction:")
        st.write(model.predict(np.array([[Round, Pick, Position_list.index(Pos), Age, AP1, PB, St, CarAV, DrAV, G, Cmp, Att_Pass, Yds_Pass, TD_Pass, Int, Att_Rush, Yds_Rush, TD_Rush,
        Rec, Yds_Rec, TD_Rec, Solo, Int_Def, Sacks, College_list.index(College), Height_inches, Weight_lbs, Hand_Size_inches, Arm_Length_inches, Forty_yard_dash, Bench_Press,
        Vert_Leap_inches, Broad_Jump_inches, Shuttle, Three_Cone]])))
    
    
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Daniel Jones.jpeg")
    st.write("This is Daniel Jones. He was selected 6th by the New York Giants and plays Quarterback.")
    st.write("His first year Madden Rating was 63 and as such falls into my C Tier for player performance")
    data_jones = load_data("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/C__Users_Admin_Desktop_jones.csv")
    st.dataframe(data_jones)

    form2 = st.form("jones_form")
    
    Round = form2.slider("Which round were you picked?", min_value = 1, max_value = 7, value = 1)
    Pick = form2.slider("Which number were you picked?", min_value = 1, max_value = 255, value = 6) 
    Pos= form2.selectbox("Which position do you play?", Position_list)
    Age= form2.slider("How old are you", min_value = 18, max_value = 50, value = 22)
    AP1= form2.slider("How many All Pro 1st Team selections do you have?", min_value = 0, max_value = 15)
    PB = form2.slider("How many Pro Bowl Selections do you have?", min_value = 0, max_value = 15)
    St = form2.slider("How many years have you been a starter on your team?", min_value = 0, max_value = 15, value = 2)
    CarAV = form2.slider("What is your Career Weighted Average?", min_value = 0, max_value = 50, value = 18)
    DrAV = form2.slider("What is your Draft Weighted Average of the team that selected you?", min_value = 0, max_value = 50, value = 18)
    G = form2.slider("How many games have you played in your career?", min_value = 0, max_value = 50, value = 27)
    Cmp = form2.slider("How many passes have you completed as a Quarterback?", min_value = 0, max_value = 1500, step = 10, value = 564)
    Att_Pass = form2.slider("How many career pass attempts do you have?", min_value = 0, max_value = 2000, step = 10, value = 907)
    Yds_Pass = form2.slider("How many career passing yards do you have?", min_value = 0, max_value = 15000, step = 50, value = 5970)
    TD_Pass = form2.slider("How many caeer TD passes do you have?", min_value = 0, max_value = 200, value = 35)
    Int = form2.slider("How many career interceptions have you thrown?", min_value = 0, max_value = 200, value = 22)
    Att_Rush= form2.slider("How many career rushing attempts do you have?", min_value = 0, max_value = 1000, step = 25, value = 110)
    Yds_Rush = form2.slider("How many career rushing yards do you have?", min_value = 0, max_value = 4000, step = 20, value = 702)
    TD_Rush = form2.slider("How many rushing TDs do you have?", min_value = 0, max_value = 150, step = 5, value = 3)
    Rec = form2.slider("How many career receptions do you have?", min_value = 0, max_value = 500, step = 5)
    Yds_Rec = form2.slider("How many career recieving yards do you have?", min_value = 0, max_value = 5000, step = 50)
    TD_Rec = form2.slider("How many career recieving touchdowns do you have?", min_value = 0, max_value = 500, step = 5)
    Solo = form2.slider("How many tackles have you made in your career?", min_value = 0, max_value = 500)
    Int_Def = form2.slider("How many defensive interceptions have you made in your career?", min_value = 0, max_value = 250)
    Sacks = form2.slider("How many sacks have you made in your career?", min_value = 0, max_value = 400, step = 2)
    College = form2.selectbox("Which College did you attend?", College_list)
    
    
    Height_inches = form2.slider("How tall are you in inches?", min_value = 0.0, max_value = 100.0, step= 0.5, value = 77.0)
    Weight_lbs = form2.slider("How heavy are you in pounds?", min_value = 0.0, max_value = 500.0, step = 0.5, value = 221.0)
    Hand_Size_inches = form2.slider("How big is your hand in inches?", min_value = 0.0, max_value = 15.0, step = 0.25, value = 9.75)
    Arm_Length_inches = form2.slider("How long is your Arm in inches?", min_value = 0.0, max_value = 45.0, step = 0.5, value = 32.5)
    Forty_yard_dash = form2.slider("How fast do you run the 40 yard dash?", min_value = 0.0, max_value = 15.0, step= 0.1, value = 4.8)
    Bench_Press = form2.slider("How many times can you bench press 225 pounds?", min_value = 0.0, max_value = 60.0, step = 1.0)
    Vert_Leap_inches = form2.slider("How high can you jump in inches?", min_value = 0.0, max_value = 60.0, step=0.5, value = 33.5)
    Broad_Jump_inches = form2.slider("How long is your broad jump in inches?", min_value = 0.0, max_value = 160.0, step = 0.5, value = 120.0)
    Shuttle = form2.slider("How fast can you complete the shuttle drill?", min_value = 0.0, max_value = 15.0, step= 0.5, value = 7.0)
    Three_Cone = form2.slider("How fast can you complete the 3Cone drill?", min_value = 0.0, max_value = 15.0, step = 0.5, value = 4.40)
    
    Button_2 = form2.form_submit_button("Press for a bit of magic!")

    if Button_2:
        st.header("Player Prediction:")
        st.write(model.predict(np.array([[Round, Pick, Position_list.index(Pos), Age, AP1, PB, St, CarAV, DrAV, G, Cmp, Att_Pass, Yds_Pass, TD_Pass, Int, Att_Rush, Yds_Rush, TD_Rush,
        Rec, Yds_Rec, TD_Rec, Solo, Int_Def, Sacks, College_list.index(College), Height_inches, Weight_lbs, Hand_Size_inches, Arm_Length_inches, Forty_yard_dash, Bench_Press,
        Vert_Leap_inches, Broad_Jump_inches, Shuttle, Three_Cone]])))

elif choice == "Challenges,Aspects to Improve On, Future Work":
    st.title("Challenges and Aspects to Improve On")
    st.image("/Users/fwworner/Desktop/NFL_Rookie_ Predictor_Streamlit/Challenges.jpeg")
    st.title("Challenges")
    st.header("🏈  Data Collection Accuracy")
    st.header("🏈  Data Cleaning and Concatination")
    st.header("🏈  MORE DATA,MORE DATA,MORE DATA!")
    st.header("🏈  Picking Appropriate Model")
    
    
    st.title("Things to improve on for next time")
    st.header("🏈  The User Experience")
    st.header("🏈  More Complete Player Data from College Teams")
    st.header("🏈  More Tiers of Classification or Possible Conversion to a Regression Rating Predictor")
    st.header("🏈  Feature Selection in Model")
    st.header("🏈  App Implementaton")
# Create Last page
elif choice == "References":
    st.title("References")
    st.write("Excellent Project with Similar ideas (MODEL BUILDNG PAPER): https://www.reddit.com/r/nfl/comments/b27abi/oc_building_an_nfl_draft_model_using_machine/")
    st.write("Madden Ratings: https://maddenratings.weebly.com/madden-nfl-20.html ")
    st.write("Machine Learning Project with NFL Combine Stats: https://www.linkedin.com/pulse/players-success-combine-stats-universities-attend-ryan-mclaughlin")
    st.write("Combine 2020 Data: https://www.pro-football-reference.com/draft/2016-combine.html")
    st.write("Great Resource for Sports Datasets: https://sports-statistics.com/sports-data/sports-data-sets-for-data-modeling-visualization-predictions-machine-learning/")
    st.write("NFL Combine Data Visulizulization: https://nycdatascience.com/blog/student-works/nfl-scouting-combine-data-visualization/ ")
    st.write("NFL Data Resource: https://data.world/sportsvizsunday/nfl-combine-data ")
    st.write("Project Combining Draft and Combine Results: https://nfldraftcombineanalysis.wordpress.com/ ")
    st.write("2019 Combine Data: https://www.kaggle.com/dtrade84/2019-nfl-scouting-combine?select=2019_nfl_combine_results.csv")
    st.write("How are Madden Ratings Calculated: https://www.businessinsider.com/madden-20-player-rating-process-adjusters-2019-7 ")
    st.write("2019 Version of Madden Ratings Calculations: https://www.espn.com/nfl/story/_/id/27092399/who-rates-players-madden-nfl-20-go-ratings-process ")
    st.write("Can the Combine Predict Future Success?: https://nfldraftcombineanalysis.wordpress.com ")



















      
                