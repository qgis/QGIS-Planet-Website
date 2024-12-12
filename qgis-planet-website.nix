{ lib, stdenv, hugo, gnumake }:

stdenv.mkDerivation {
    name = "qgis-planet-website";
    src = ./.;
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
};