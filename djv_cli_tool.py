import click


@click.group()
def cli():
    pass


@click.command()
def greet():
    click.echo("Ich grüße dich")


cli.add_command(greet)


if __name__ == "__main__":
    cli()
