with import <nixpkgs> {};

let
argparse = pythonPackages.buildPythonPackage {
  name = "argparse-1.4.0";
  src = pkgs.fetchurl { url = "https://files.pythonhosted.org/packages/18/dd/e617cfc3f6210ae183374cd9f6a26b20514bbb5a792af97949c5aacddf0f/argparse-1.4.0.tar.gz"; sha256 = "62b089a55be1d8949cd2bc7e0df0bddb9e028faefc8c32038cc84862aefdd6e4"; };
  buildInputs = [];
  propagatedBuildInputs = [ ];
  meta = with pkgs.stdenv.lib; {
    homepage = "https://github.com/ThomasWaldmann/argparse/";
    license = licenses.psfl;
    description = "Python command-line parsing library";
  };
};
pylode = python37.pkgs.buildPythonApplication rec {
  pname = "pylode";
  version = "1.9";

  src = fetchGit ./.;

  doCheck = false;

  # checkPhase = ''
  #   python -m pytest -vs tests
  # '';
  # checkInputs = [ python37.pkgs.py python37.pkgs.pytest python37.pkgs.pytest-datafiles python37.pkgs.mock python37.pkgs.pytest-mock python37.pkgs.pytestrunner pkgs.python37Packages.wheel ];

  propagatedBuildInputs = [ python37.pkgs.rdflib python37.pkgs.py python37.pkgs.requests python37.pkgs.falcon python37.pkgs.jinja2 python37.pkgs.python-dateutil python37.pkgs.gunicorn argparse python37.pkgs.pytest python37.pkgs.wheel ];
};
in
pkgs.mkShell {
  buildInputs = [
    pypi2nix pylode
  ];
}
