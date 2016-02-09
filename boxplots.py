def get_teams(dataframe):
	"""Extracts the team names (column names) from a dataframe"""
	team_numbers = list(dataframe[:0]) # take the column names and convert them to a list 
	del team_numbers[0] # remove the text header

def make_data_groups(dataframe, team_names):
	"""Split a dataframe in to groups based on a list of column names"""
	master_group = [] # set an empty list to hold multiple lists
	for name in team_names: # itterate through each teach name
		group = [] # set an empty list for each team
		group.append(dataframe[column]) # fill a list with each team's ranks
		master_group.append(group) # add each of the team lists to the master list
	return master_group

def make_plots(data_groups):
	"""Takes data groups created with make_data_groups and creates boxplots from them"""
	figure = plot.boxplot(data_groups)
	figure.show()

def sort_plots(data_groups):
	
19dc20996adc95cdad4966a66414ae16fc6e886f