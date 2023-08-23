import numpy as np
import pandas as pd

mydictionary = {'names': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'physics': [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra': [78, 88, 82, 87]}

#create dataframe using dictionary
df_marks = pd.DataFrame(mydictionary)

print(df_marks)
