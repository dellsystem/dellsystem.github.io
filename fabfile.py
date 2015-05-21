from fabric.api import local, run, env

env.hosts = ['nimbus']
env.use_ssh_config = True

def less():
    local('lessc css/styles.less -x > css/styles.css')

def prepare():
    less()
    local('jekyll build')

def up():
    less()
    local('jekyll serve --watch')

def archive():
	local('rm -rf _site/design _site/fabfile* _site/css/*.less')
	local('tar czf site.tar.gz _site')

def transfer():
	local('scp site.tar.gz %s:' % env.hosts[0])
	local('rm site.tar.gz')

def unpack():
	run('tar xzf site.tar.gz')

def deploy():
	prepare()
	archive()
	transfer()
	unpack()
