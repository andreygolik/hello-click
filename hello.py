import click

class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

@cli.command()
# options are optional
@click.option('--string', default='World', # type is derived from default value
                help='This is the thing that is greeted.')
@click.option('--repeat', default=1, type=int, # or you can specify it explicitly
                help='How many times you should be greeted.')
# arguments are mandatory (by default) and come after options
@click.argument('out', type=click.File('w'), default='-', # stdout
                required=False)
@pass_config
def say(config, string, repeat, out):
    """This script greets you."""

    if config.verbose:
        click.echo('We are in verbose mode')
        click.echo('Home directory is {0}'.format(config.home_directory))

    for i in range(repeat):
        click.echo('Hello, {0}!'.format(string), file=out)
