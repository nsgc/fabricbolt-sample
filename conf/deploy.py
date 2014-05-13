from fabric.api import run

def put_file():
    run('touch hello')
    run('echo world > hello')
