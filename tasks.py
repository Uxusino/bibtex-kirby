import os
from invoke import task
from dotenv import load_dotenv, set_key, dotenv_values

ENV_FILE = ".env"

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
    if not os.path.exists(ENV_FILE):
        print(".env file not found. Let's create a new one.")
        open(ENV_FILE, 'w').close()
        db_host = input("Enter your database address in 'postgresql:...' format [localhost]:") or "localhost"
        db_test = input("Enable test environment? ('true' or 'false') [true]") or "true"
        db_secret = input("Enter secret key:")

        env_vars = {
            "DATABASE_URL": db_host,
            "TEST_ENV": db_test,
            "SECRET_KEY": db_secret
        }

        for key, value in env_vars.items():
            set_key(ENV_FILE, key, value)

        print(".env file was created successfully.")
    ctx.run("python3 src/db_helper.py", pty=True)

@task
def unittest(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def robot(ctx):
    ctx.run("robot src/story_tests")