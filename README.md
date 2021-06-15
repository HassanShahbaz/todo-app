1. Go to root directory
2. Create python3 virtualenv -> `virtualenv -p python3 venv`
3. Activate environment -> `source venv/bin/activate`
4. Install requirements -> `pip install -r requirements.txt`
5. Run project -> `uvicorn todo_app.main:app --reload`

Run via docker:
1. Go to root directory
2. `docker-compose build`
3. `docker-compose up`

Create postgres database:

`sudo -u postgres psql`
`create user todo_app;`
`create database todo_app;`
`alter user todo_app with password 'todo123';`

1. DATABASE_NAME: `todo_app`
2. DATABASE_USER: `todo_app`
3. DATABASE_PASSWORD: `todo123`
4. DATABASE_HOST: if running via docker host should be `db` else host should be `localhost`
5. PORT: `5432`
