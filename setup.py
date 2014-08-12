from distutils.core import setup

setup(name = "syslog-stdout",
    version = "0.1",
    description = "Minimalistic syslog which just prints to stdout",
    author = "O. Schacher",
    url='https://github.com/gryphius/syslog-stdout',
    download_url='https://github.com/gryphius/syslog-stdout/tarball/master',
    author_email = "oli@wgwh.ch",
    long_description = """This minimalistic syslog process creates the /dev/log socket and prints all received messages to stdout
    This is useful in docker containers if don't want to run a full blown syslog
    """ ,
    scripts  = ['syslog-stdout.py'],
)
