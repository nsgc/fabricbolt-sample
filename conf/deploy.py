from fabric.api import run, env

def put_file():
  env.gateway     = ''
  env.host_string = '192.168.111.223'
  env.user        = 'vagrant'
  env.password    = 'vagrant'

  run('touch hello')
  run('echo world > hello')
