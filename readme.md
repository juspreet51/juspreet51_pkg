# Juspreet51
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/juspreet51/juspreet51_pkg)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/juspreet51/juspreet51_pkg)
![GitHub followers](https://img.shields.io/github/followers/juspreet51?label=%40Juspreet51&style=social)
![Twitter URL](https://img.shields.io/twitter/url?label=%40Juspreet51&style=social&url=https%3A%2F%2Fwww.twitter.com%2Fjuspreet51)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/BMSMBmuweD)


Juspreet51 is a library for making EDA and Modelling in Python quick and convinient. It's built on top of:
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
<br>
- Open your `Anaconda Prompt`
- type in
```python
pip install juspreet51
```
- and hit Enter

<br>

- Or simply, open your `Jupyter Notebook`
- and type in 
```python
% pip install juspreet51
```
- and press `Shift+Enter`

___

# Demo Notebooks:
<br>
<ol>
    <li>
    
 js51_metrics.[plot_confusion_matrix()](https://github.com/juspreet51/juspreet51_pkg/tree/main/src/juspreet51/demo_nbs/plot_confusion_matrix.ipynb)
```python
from juspreet51 import metrics as js51_metrics
js51_metrics.plot_confusion_matrix(y_test, predictions)
```
<img 
src="https://raw.githubusercontent.com/juspreet51/juspreet51_pkg/main/src/juspreet51/media/plot_cfm_output.PNG" 
style="width:45%;  display: block; margin-left: auto;  margin-right: auto;">
</li>

<li> 

js51_viz.[draw_piechart()](https://github.com/juspreet51/juspreet51_pkg/tree/main/src/juspreet51/demo_nbs/draw_piechart.ipynb)

```python
from juspreet51 import visualizations as js51_viz
js51_viz.draw_piechart(dataframe['column_name'])
```
<img 
src="https://raw.githubusercontent.com/juspreet51/juspreet51_pkg/main/src/juspreet51/media/draw_piechart.PNG" 
style="width:35%;  display: block; margin-left: auto;  margin-right: auto;">
</li>

## Future Release:

<li> 

 js51_lin_model.[LinearRegression()](#)
<br>
```python
from juspreet51 import linear_model as js51_lin_model
```
</li>
</ol>

___