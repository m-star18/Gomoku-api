# Gomoku-api

"Gomoku-api" is an api that searches for the best move and 
returns it when you send the current board as json.

## Requirement
 
* Flask 2.0.1
* Flask_Cors 3.0.10

## Usage
 
```bash
git clone https://github.com/m-star18/Gomoku-api.git
cd Gomoku-api
docker-compose up -d
```

## Algorithm
- [base](src/base.py)
- [greedy](src/greedy.py)

## Dependent repository

- [Frontend](https://github.com/igsr5/gomoku-app-front)
- [Server api](https://github.com/igsr5/gomoku-app-server)

## License

This program is released under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
