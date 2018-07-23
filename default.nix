with import <nixpkgs> {};
with python3Packages;

buildPythonApplication {
  name = "packetprov";
  src = lib.cleanSource ./.;

  propagatedBuildInputs = [ click requests ];
}

