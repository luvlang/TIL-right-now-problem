import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head())
# sns.histplot(data=titanic, x='age')
# plt.show()