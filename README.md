1.Go to root directory
2.Activate environment -> source venv/bin/activate
3.Run project -> uvicorn todo_app.main:app --reload

Run via docker:
1.Go to root directory
2.docker-compose build
3.docker-compose up

Create postgres database:
DATABASE_NAME: todo_app
DATABASE_USER: todo_app
DATABASE_PASSWORD: todo123
DATABASE_HOST: if running via docker host should be db else host should be localhost
PORT: 5432
