from setuptools import setup, find_packages

setup(
    name='packetprov',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'packetprov-dump-ssh=packetprov.dump_ssh:main',
            'packetprov-export=packetprov.export:main',
            'packetprov-notify=packetprov.notify:main',
        ],
    }
)
