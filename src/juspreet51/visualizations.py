import matplotlib as plt
import pandas as pd
import seaborn as sns

# manipulation data
import pandas as pd
import numpy as np

#visualiation data
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot

#default theme
plt.style.use('ggplot')
sns.set(context='notebook', style='darkgrid', palette='colorblind', font='sans-serif', font_scale=1, rc=None)
matplotlib.rcParams['figure.figsize'] =[8,8]
matplotlib.rcParams.update({'font.size': 15})
matplotlib.rcParams['font.family'] = 'sans-serif'



def draw_piechart(data=None):
    if data is None:
        train = pd.read_csv('https://raw.githubusercontent.com/juspreet51/ml_templates/main/datasets/regression/black_friday/black_friday_train.csv')
        train.dtypes.value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%1.2f%%',shadow=True)
        plt.title('type of our data')
    else:
        data.value_counts().plot.pie()
        plt.title('Pie Chart')