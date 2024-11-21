from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/db_helper.py", pty=True)

@task
def unittest(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def robot(ctx):
    ctx.run("robot src/story_tests")