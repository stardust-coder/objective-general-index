# OGI (objective general index) implementation in Python


### Setup
```bash
pip install git@github.com:stardust-coder/objective-general-index.git
```


### How to use
```python
from OGI import *
data = 'data/sample.csv'
weights, vectors, ogi = ogi_weight(data, is_csv=True)
```


If you are looking for R package, see [Tomonari Sei and Masaki Hamada](https://cran.r-project.org/package=OGI).

### Reference

If you use this algorithm, please cite the article:

```
Tomonari Sei,
An objective general index for multivariate ordered data,
Journal of Multivariate Analysis,
Volume 147,
2016,
Pages 247-264,
```

### How to cite

In BibTeX format
```
@software{ogi-in-python,
  author = {Sukeda, Issey},
  title = {{Objective General Index implementation in Python}},
  url = {https://github.com/stardust-coder/objective-general-index},
  version = {1.0.0},
  date = {2024-01-06},
}
```