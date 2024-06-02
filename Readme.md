## Python Tank Game. Three tanks meet each other and shoot. User (attacker) wins if tank stayed safe on the battalfied.

### How to run:
##### Copy env.dist and rename it to .env
##### Put value for TRACEBACK_LIMIT in .env (e.g. 0)
##### Run `python3 command.py` with dictionary from below as command line argument

##### Arguments to be passed to command line:
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
##### Random version to be run from command line with `python3 command.py random`

##### Tests to be run with: `python3 -m unittest test`
##### Tests coverage to be generated with: `python3 -m coverage report`

##### Dictionaries to be passed to Battle class if calling from the code:
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