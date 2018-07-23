with import <nixpkgs> {};
with python3Packages;

stdenv.mkDerivation {
  name = "packetprov";

  buildInputs = [ pip python virtualenv ];

  shellHook = ''
    export SOURCE_DATE_EPOCH=$(date +%s)
    virtualenv --no-setuptools virtualenv

    export PATH=$PWD/virtualenv/bin:$PATH
    pip install -r requirements.txt
    pip install --editable .
  '';
}
