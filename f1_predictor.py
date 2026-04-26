#ideas:
#take the average of all the poeple in a particular team.
#then give the one with the highest probability

import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt


'''This is the main file I will be using to compare the user's data with'''
the_comparison_file = pd.read_csv("winners_f1_2000_2025_v2.csv")

df_main = pd.DataFrame(the_comparison_file)
del df_main['Date'] #Deleting date which has YYYY-MM-DD format to polish the dataset

'''Creating a class F1DataPredictor'''
class F1Predictor:
    # the constructor contains and creates the main dataframe.
    def __init__(self, main_df):
        self.df = main_df.copy() # Making a copy to operate later in the program.
        self.the_dict = {} # This dictionary stores the final team averages.
        self.filtered_df = pd.DataFrame() # This dataframe stores the filtered results.
    # the filter_by_file function assigns the filepath, and checks if the file exists in the operating system.
    def filter_by_file(self, filename: str):
        self.filepath = f"{filename}.txt"
        if not os.path.exists(self.filepath):
            print(f"Error: File '{self.filepath}' does not exist in the os!")
        else:
            return None
    # this filters data and stores the result in self.filtered_df dataframe
    def filter_by_circuit_and_team(self):
        """Reads the teams, circuit, and the particular year from the file and filters the data accordingly."""
        '''do smth'''
        if not self.filepath:
            raise AttributeError(f"Run the function of (filter_by_file) and please set the filepath.")
        else:
            #opening the file and reading it.
            try:
                with open(self.filepath, 'r') as f:
                    the_list_req = f.readlines() #readlines converts into a list with newline character \n.
                
                # Remove the newline character that appears after each object after using the readlines() function.
                team_list_raw = [line.strip() for line in the_list_req]
                
                if len(team_list_raw) <= 3:
                    print("Unable to do the analysis, because we need atleast 2 teams for comparison!")
                #test case:
                # put a test file of one team, a circuit and the year. It should print out this statement!
                else:
                    # Assigning values-
                    # The text file contains the following:
                    # -> the names of the teams participating in the Prix.
                    # -> followed by the circuit name, and the year as the last line.
                    circuit_name = team_list_raw[-2]
                    the_year = team_list_raw[-1]
                    team_list = team_list_raw[:-2] # All elements except circuit and year.
                    if isinstance(int(the_year), (str or float)): #checking if the year is only an int.
                        print("Year should be an integer!")
                    else:
                        # filtering the dataframe using .str.contains() to filter out the particular year the user has asked for.
                        filtered_df = self.df[
                            self.df['Circuit'].str.contains(
                                circuit_name
                            )
                        ]       
                        # Checking if the user's teams exists in the list of teams in the kaggle dataset.
                        self.filtered_df = filtered_df[filtered_df['Team'].isin(team_list)]

                        if self.filtered_df.empty: #checks if df is empty, i.e if any of column/row length is 0.
                            print("No exact matching data was available!")
            except FileNotFoundError:
                    print("File is not available!")

    # as the time in the dataset is in hours:minutes:seconds format, I will have to format the 'Time' column enitrely into seconds.
    """Converts the 'Time' column from HH:MM:SS format to total seconds."""
    def converting_to_seconds(self):
        """ Converting HH:MM:SS using .str.slice().astype(datatype)
        By doing this:
        -> .str.slice(0, 2) is similar to [0:2], but it does not convert dataype of object to int via normal slicing.
        -> then using conversion method of '.astype(datatype)' to convert each of these types into seconds.
        """
        if self.filtered_df.empty:
            return None
        else:
            # Hours:
            #Example: 01:12:23
            # slices out '01'
            # treats all the time objects as strings and slices out each one of them
            hours = self.filtered_df['Time'].str.slice(0, 2).astype(int)
            # Minutes:
            #Example: 01:12:23
            # slices out '12'
            minutes = self.filtered_df['Time'].str.slice(3, 5).astype(int) #.astype() casting into int()
            # Seconds:
            #Example: 01:12:23
            # slices out '23'
            seconds = self.filtered_df['Time'].str.slice(6, 8).astype(int)
            
            #Adding them all up and converting them into seconds.
            self.filtered_df['Time_in_seconds'] = (hours * 3600) + (minutes * 60) + (seconds)
            
            self.filtered_df.drop('Time', axis=1) #axis means column.
    # This function calculates time per lap for each data entry
    def time_per_lap(self):
        """Calculates the time taken per lap for each row."""
        try:
            if self.filtered_df.empty:
                return None
            else:
                # Division of per column for determining time per lap.
                self.filtered_df['Time_per_lap'] = self.filtered_df['Time_in_seconds'] / self.filtered_df['Laps']
            # #test case: look out for zero division error
            # # if laps == 0, zerodivisionerrror occurs.
            # if self.filtered_df[self.filtered_df['Laps'] <= 0]: #checking if value of laps is 0.
                #print("Invalid laps!")
            if self.filtered_df.empty:
                print("No exact matching data is available")  
        except ZeroDivisionError:
            print("ZeroDivisonError occured! Laps are invalid!, cannot divide by 0.")     

    # Finding out the average time per lap for the teams in the dictionary.
    def average_time_per_lap(self):
        """Calculates average time per lap by looping through unique teams."""
        if self.filtered_df.empty:
            print("No data in the df!")
            return None
        else:
            self.the_dict = {}

            # Unique list is a list of teams where each of the team is unique and it does not show the duplicate items and their values in the list.
            unique_teams = self.filtered_df['Team'].unique()

            # testing .unique()
            # if not using unique, this was the issue
            # teams = self.filtered_df['Team']
            # print(teams) 

            # For loop to iterate through each team
            for team in unique_teams:
                # Checking if team in the unique team equals the team in the list.
                team_rows = self.filtered_df[self.filtered_df['Team'] == team]
                
                # Calculating the mean (average) of time_per_lap entries for respective teams.
                average_value = team_rows['Time_per_lap'].mean()
                
                # Mapping the average value to the team.
                self.the_dict[team] = average_value
                
                # Showing the average of each team.
                print(f"Team: {team}, Average time: {self.the_dict[team]}")

                # The main issue I encountered was that for each of the dictionary values was it had a np.float64 datatype.
                # so I used dict comprehension to check if the value of a key was np.float() using isinstance(), where all of the values were actually np.float64 datatype
                # I then converted all the values into float type.

            self.the_dict = {
                key: float(value) if isinstance(value, np.float64) else value #if np.float64 -> converts to float, else stays the same.
                for key, value in self.the_dict.items() #mapping for each of the new values to the keys.
            }
    # Comparing all the teams and determining which team has the least average, thus determining the winnner.
    def comparison(self):
        """
        Determines the team with the lowest average time per lap (highest probability).
        """
        try:
            if not self.the_dict:
                return "No data available", 0.0
            else:
                #finding the minimum.
                winning_team = min(self.the_dict, key=self.the_dict.get)
                global min_time
                min_time = self.the_dict[winning_team]
                return winning_team, min_time #returns a tuple of winning team and the minimum time
        except:
            print("File is not available!")
    # Plotting the graph
    def drawing_graph(self):
        """
        Creates a sorted bar chart of average time per lap for all teams.
        """
        try:
            # The data
            x_axis_data = [team for team in self.the_dict] # the teams.
            y_axis_data = [value for key, value in self.the_dict.items()] # the value for each team, i.e their average time.

            # Plotting the graph.
            plt.plot(x_axis_data, y_axis_data) # Plots y versus x

            # Giving the title and labelling the axis.
            plt.title("Teams vs Average Race Time")
            plt.xlabel("Teams (X-axis)")
            plt.ylabel("Average Time (Y-axis)")

            # Showing the final plot.
            plt.show()
        except:
            print("File not found!") 
    def display_winner(self):
        try:
            print("Final Prediction:")
            print(f"Winner: {winner}")
            print(f"Average Time: {min_time} seconds")
        except:
            print("File not found!")
 
obj = F1Predictor(df_main)
#test case where the file name is "wrong", but does not exist in the operating system:
# obj.filter_by_file("wrong")
obj.filter_by_file("test")
obj.filter_by_circuit_and_team()
obj.converting_to_seconds()      
obj.time_per_lap()               
obj.average_time_per_lap()      
obj.drawing_graph()
comparison_tuple = obj.comparison() # As the comparison() function returns a tuple of winner and time, I unpacked them.
winner = comparison_tuple[0]
time = comparison_tuple[1]
obj.display_winner()
