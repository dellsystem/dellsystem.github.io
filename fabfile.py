from fabric.api import local, run, env, cd

env.hosts = ['aws']
env.use_ssh_config = True

def less():
    local('lessc css/styles.less -x > css/styles.css')

def prepare():
    less()
    local('jekyll build')

def up():
    less()
    local('jekyll serve --watch --future')

def archive():
	local('rm -rf _site/design _site/fabfile* _site/css/*.less')
	local('tar czf site.tar.gz _site')

def transfer():
	local('scp site.tar.gz %s:dellsystem.me/' % env.hosts[0])
	local('rm site.tar.gz')

def unpack():
    with cd('dellsystem.me'):
        run('tar xzf site.tar.gz')

def deploy():
	prepare()
	archive()
	transfer()
	unpack()
