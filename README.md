
## Installation

1. Fork this repository to your github account
2. Clone the forked repository and move to the cloned repository on your local machine.

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```

### Starting the server and running tests (with Dockerfile)

```
sudo docker build -t my-flask-app .
sudo docker run -p 7755:7755 my-flask-app

# This will start the server at `http://localhost:7755`

# Note :- The dockerfile will automatically run the tests itself. 
# Please check the terminal log for the test coverage report.
```

### Starting the server (using docker-compose)

```
sudo docker-compose up

# This will start the server at `http://localhost:7755`
```

### Aborting the server (using docker-compose)

```
sudo docker-compose down
```

### Start Server (Without using Dockerfile)

```
bash run.sh
```
### Run Tests (Without using Dockerfile)

```
Note: - Please reset the DB everytime before running the tests.
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

