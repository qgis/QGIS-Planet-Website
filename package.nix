{ lib, stdenv, hugo, gnumake }:

stdenv.mkDerivation {
    name = "qgis-planet-website";
    src = lib.cleanSourceWith {
        src = ./.;
        filter = (
        path: type: (builtins.all (x: x != baseNameOf path) [
            ".git"
            ".github"
            "flake.nix"
            "package.nix"
        ])
        );
    };
    buildInputs = [ hugo gnumake ];

    buildPhase = ''
        make deploy
    '';

    installPhase = ''
        mkdir -p $out
        cp -r public/* $out/
    '';

    meta = with lib; {
        description = "A built QGIS Planet website";
        license = licenses.mit;
    };
}

