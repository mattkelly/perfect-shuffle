perfect-shuffle
===============

A simple, colorful utility for playing with perfect in/out Faro shuffles. Shuffling is performed iteratively until the deck returns to its initial arrangement. 

Some of the shuffling code is borrowed from https://en.wikipedia.org/wiki/Faro_shuffle.

### Usage

```
usage: perfect-shuffle.py [-h] shuffle_type num_cards

A simple utility for playing with perfect in/out Faro shuffles

positional arguments:
  shuffle_type  Type of shuffle [in|out]
  num_cards     Number of cards to shuffle

optional arguments:
  -h, --help    show this help message and exit

```

### Example

```
% python perfect-shuffle.py out 24

New deck:

      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 


Shuffling:

      0  12   1  13   2  14   3  15   4  16   5  17   6  18   7  19   8  20   9  21  10  22  11  23 

      0   6  12  18   1   7  13  19   2   8  14  20   3   9  15  21   4  10  16  22   5  11  17  23 

      0   3   6   9  12  15  18  21   1   4   7  10  13  16  19  22   2   5   8  11  14  17  20  23 

      0  13   3  16   6  19   9  22  12   2  15   5  18   8  21  11   1  14   4  17   7  20  10  23 

      0  18  13   8   3  21  16  11   6   1  19  14   9   4  22  17  12   7   2  20  15  10   5  23 

      0   9  18   4  13  22   8  17   3  12  21   7  16   2  11  20   6  15   1  10  19   5  14  23 

      0  16   9   2  18  11   4  20  13   6  22  15   8   1  17  10   3  19  12   5  21  14   7  23 

      0   8  16   1   9  17   2  10  18   3  11  19   4  12  20   5  13  21   6  14  22   7  15  23 

      0   4   8  12  16  20   1   5   9  13  17  21   2   6  10  14  18  22   3   7  11  15  19  23 

      0   2   4   6   8  10  12  14  16  18  20  22   1   3   5   7   9  11  13  15  17  19  21  23 

      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 
      
      
      Deck is back in new-deck order after 11 shuffles.

```

### Dependencies

colorama: http://pypi.python.org/pypi/colorama
