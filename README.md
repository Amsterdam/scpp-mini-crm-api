# mini-crm-api
An API to get remote data, cached in a database, for mini-crm

## Database migration
`mini-crm.sh` executes the SQL files in the `sql/` directory, add new migrations in this directory and file

## How to start

### Development:

- Create a Python 3 virtual env named `venv` and activate it.
- Install requirements inside your virtual env with `python -m pip install -r requirements.txt`
- Create a PostgreSQL database and user, setup PostGIS extension
- Set up and customize the environment variabels, see below
- Start application with `./mini-crm.sh`

### Production:

- Build Docker image (see Dockerfile)
- Create container with the required environments variabels (see below, customize them)
- Start container, the application will be exported under port 8000


## Handy endpoints
[API homepage](http://localhost:8000/)
[OpenApi docs](http://localhost:8000/docs)
[Import data](http://localhost:8000/api/jobs)
[General](http://192.168.4.20:8000/status/health)

## Environment variables
Set the following environment variabels before starting the application.

    DATABASE_URL=postgresql://user:pass@127.0.0.1/minicrm
    USERS={"demo": "test12345"}
    BACKEND_CORS_ORIGINS_CSV=http://localhost,http://localhost:4200,http://localhost:3000
    AMSTERDAM_PRIMARY_SCHOOLS=https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/po
    AMSTERDAM_HIGH_SCHOOLS=https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/vo
    AMSTERDAM_KINDERGARTEN=https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/opvang
    AMSTERDAM_DAYCARE=https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/bso

### About USERS variabel

The `USERS` variabel defines the list of users with password. This should be a secret value. The list is a JSON object, property is the username, value is a plain password string (we need to change this to hashed values in the near feature).

Example:

    {
      "tim": "insecure-password",
      "tom": "another-insecure-password"
    }
