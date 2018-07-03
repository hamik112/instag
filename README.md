# Installation

```
pip install -r requirements.txt
```

# Usage
Adjust lines 20-21 with your desired search configuration.

`search_list` is a list of the initial set of hashtags to search. Do not place `#` in the list (e.g. put `nycspc` instead of `#nycspc`).

`search_len` is how many hashtags to search. 

If `len(search_list) < search_len`, it will use the most popular hashtags found while searching. For example, if while searching through `search_list = ['nycspc']`, `wearethestreet` is the second most popular tag, the algorithm will search for `wearethestreet` next.

Then run with:
```
python main.py
```

# TODO
* Ignore posts already used - keep track of image IDs