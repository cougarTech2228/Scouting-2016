# import libraries 
import pandas as pd 
import matplotlib.pyplot as plt 
import random as rd 
import numpy as np 
import statistics as stat

# take a url of the csv or can read the csv locally into a pandas data frame
data = pd.read_csv("/robot_data.csv")

# eventually get the data from the csv into robot objects
# maybe get rid of this and just use library analysis tools 
class Robot(object):

	def __init__(self, name, alliance, auto_points, points):

		self.name = name
		self.alliance = alliance
		self.auto_points = auto_points
		self.points = points

	def points_per_sec(self):
		return self.points / 150

	def auto_points_per_sec(self):
		return self.auto_points / 15

	def get_name(self):
		return self.name

	def get_alliance(self):
		return self.alliance









