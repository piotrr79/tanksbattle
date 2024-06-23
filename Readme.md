## Python Tank Game. Three tanks meet each other and shoot. User (attacker) wins if tank stayed safe on the battalfied.

## Setup:
##### Copy env.dist and rename it to .env
##### Put value for TRACEBACK_LIMIT in .env (e.g. 0)
##### Create SqLite database, for example in /api folder, called py_tank_game.db and execute following statement via any database UI like Valentina or Workbench:

```
CREATE TABLE IF NOT EXISTS `Users`(
        `uuid` VARCHAR(36) NOT NULL,
        `player_name` VARCHAR(255) NOT NULL,
        `player_ip` VARCHAR(255) NOT NULL,
        `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `last_updated` TIMESTAMP NOT NULL,
        PRIMARY KEY (`uuid`)
);

CREATE TABLE IF NOT EXISTS `Stats`(
        `uuid` VARCHAR(36) NOT NULL,
        `user_id` VARCHAR(36) NOT NULL,
        `player_score` INT NOT NULL,
        `number_of_games` INT NOT NULL,
        `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `last_updated` TIMESTAMP NOT NULL,
        PRIMARY KEY (uuid),
        CONSTRAINT FK_Users FOREIGN KEY (`user_id`)
        REFERENCES Users(`uuid`)
);
```


### Run from api:

##### Run `fastapi dev main.py` from /api directory to start api server

##### Follow instructions from /dev_oauth_server/README.md to create user and generate authorization token

##### Run selected urls with culr or with Postman (collections attached to repository), for random game use authorization token in header: 

```Authorization: Bearer your_token_obtained_in_ouath_dev_server```

##### Urls: 
```
Game intro: http://127.0.0.1:8000/game/intro
Game rules: http://127.0.0.1:8000/game/rules
Random game: http://127.0.0.1:8000/game/random
Defined game: http://127.0.0.1:8000/game/defined
```

### Run from command:

##### Random version to be run from command line with:
 `python3 command.py random`

##### Run defined version with dictionary passed as argument with:
`python3 command.py`

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


##### Tests to be run with: 
`cd test`
`python3 -m unittest testarmour`

##### Tests coverage to be generated with: 
`cd test`
`python3 -m coverage report`

##### Dictionaries to be passed to Battle class if calling from the code for non random game:
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