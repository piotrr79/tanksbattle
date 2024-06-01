### Run `python3 command.p` with dictionary from below as command line argument

### Arguments to be passed to command line:
```  
'{
  "attacker" : {
    "armor" : 600,
    "penetration" : 670,
    "armor_type" : "chobham"
  },
  "defender" : {
    "armor" : 620,
    "penetration" : 670,
    "armor_type" : "chobham"
  },
  "sample_tank" : {
    "armor" : 400,
    "penetration" : 400,
    "armor_type" : "ceramic"
  }
}'
```
### Random version to be run from command line with `python3 command.py random`

### Tests to be run with: python3 -m unittest test

### Dictionaries to be passed to Battle class if calling from the code:
```  
  "attacker" : {
    "armor" : 600,
    "penetration" : 670,
    "armor_type" : "chobham"
  }
```
``` 
  "defender" : {
    "armor" : 620,
    "penetration" : 670,
    "armor_type" : "chobham"
  }
```
``` 
  "sample_tank" : {
    "armor" : 400,
    "penetration" : 400,
    "armor_type" : "ceramic"
  }
```