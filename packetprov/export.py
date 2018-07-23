import click
import json
import packetprov

def pretty_json(data):
    return json.dumps(data, indent=2)

@click.command()
def main():
    print(pretty_json(packetprov.metadata()))
