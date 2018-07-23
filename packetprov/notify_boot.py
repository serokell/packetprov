import click
import packetprov

@click.command()
def main():
    session = packetprov.session()
    metadata = packetprov.metadata(session)

    session.put(metadata['phone_home_url'], json={'instance_id': metadata['id']})


if __name__ == '__main__':
    main()
