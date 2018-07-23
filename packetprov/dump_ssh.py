import click
import packetprov

@click.command()
def main():
    for ssh_key in packetprov.metadata()['ssh_keys']:
        print(ssh_key)
