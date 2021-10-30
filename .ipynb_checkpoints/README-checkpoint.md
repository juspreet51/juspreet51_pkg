# Juspreet51
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/juspreet51/juspreet51_pkg)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/juspreet51/juspreet51_pkg)
![GitHub followers](https://img.shields.io/github/followers/juspreet51?label=%40Juspreet51&style=social)
![Twitter URL](https://img.shields.io/twitter/url?label=%40Juspreet51&style=social&url=https%3A%2F%2Fwww.twitter.com%2Fjuspreet51)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/BMSMBmuweD)


Juspreet51 is a library for making EDA and Modelling in Python quick and convinient. It is utilizes:
- pandas
- numpy
- matplotlib 
- seaborn
- plotly
- scikit-learn
- xgboost
- and others

___
To install `juspreet51`
- open your jupyter notebook
- and run

```python
% pip install juspreet51
```

Here are some of the features that `juspreet51` offers:
```python
from juspreet51 import visualizations as js51viz
js51viz.draw_piechart()
```
___

To visualize with your own data, run
```python
js51viz.draw_piechart(dataframe['column_name'])

# Taking housing dataset example, and plotting pie chart for ocean_proximity value
# Replace "https://...link/..." with data of your choice
house_val = pd.read_csv('https://raw.githubusercontent.com/juspreet51/ml_templates/main/datasets/regression/housing/housing.csv')

js51viz.draw_piechart(house_val["ocean_proximity"])
```
___