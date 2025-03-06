{ lib
, stdenv
, hugo
}:

stdenv.mkDerivation {
  name = "qgis-planet-website";

  src = lib.cleanSourceWith {
    src = ./.;
    filter = (
      path: type: (builtins.all (x: x != baseNameOf path) [
        ".git"
        ".github"
        "flake.nix"
        "flake.lock"
        "package.nix"
        "result"
      ])
    );
  };

  buildInputs = [ hugo ];

  buildPhase = ''
    hugo --config config.toml,config/config.prod.toml
  '';

  installPhase = ''
    mkdir -p $out
    cp -r public_prod/* $out/
  '';

  meta = with lib; {
    description = "A built QGIS Planet website";
    license = licenses.mit;
  };
}

