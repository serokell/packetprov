import click
import packetprov

events = {
    '101': 'Provisioning started',
    '105': 'Server partitions created',
    '109': 'Installation finished, rebooting server'
}


def event_id_to_payload(event_id):
    return {'type': 'provisioning.' + event_id, 'body': events[event_id]}


@click.command()
@click.argument('event_id', required=True, type=click.Choice(events.keys()))
def main(event_id):
    session = packetprov.session()
    session.put(packetprov.metadata(session)['phone_home_url'],
                json=event_id_to_payload(event_id))


if __name__ == '__main__':
    main()
