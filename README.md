# OGI (objective general index) implementation in Python


### Setup
```bash
pip install git@github.com:stardust-coder/objective-general-index.git
```


### How to use
```python
from OGI import *
data = 'data/sample.csv'
weights, vectors, OGI = ogi_weight(data, is_csv=True)
```

### Citations
```
Tomonari Sei,
An objective general index for multivariate ordered data,
Journal of Multivariate Analysis,
Volume 147,
2016,
Pages 247-264,
```