{
  description = "Development environment and build process for a Hugo app with Python requirements";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }: 
    let
      systems = [ "x86_64-linux" "x86_64-darwin" ];
      
      mkDevShell = system: let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
      in pkgs.mkShell {
        packages = with pkgs; [
          hugo
          vscode
          python312Packages.feedparser
          python312Packages.requests
          python312Packages.pillow
          python312Packages.python-dateutil
          gnumake
        ];
        shellHook = ''
          export DIRENV_LOG_FORMAT=
          echo "-----------------------"
          echo "🌈 Your Hugo Dev Environment is ready."
          echo "It provides hugo and vscode for use with the QGIS Planet Website Project"
          echo ""
          echo "🪛 VSCode:"
          echo "--------------------------------"
          echo "Start vscode like this:"
          echo ""
          echo "./vscode.sh"
          echo "-----------------------"
          echo "On running, it will install Hugo-related extensions."
          echo ""
          echo "🪛 Hugo:"
          echo "--------------------------------"
          echo "Start Hugo like this:"
          echo ""
          echo "hugo server"
        '';
      };

      mkQGISPlanetWebsite = system: let
        pkgs = import nixpkgs {
          inherit system;
        };
      in pkgs.stdenv.mkDerivation {
        name = "qgis-planet-website";
        src = ./.;
        buildInputs = [ pkgs.hugo pkgs.gnumake ];

        buildPhase = ''
          make deploy
        '';

        installPhase = ''
          mkdir -p $out
          cp -r public/* $out/
        '';

        meta = with pkgs.lib; {
          description = "A built QGIS Planet website";
          license = licenses.mit;
        };
      };
    in {
      # Development environment for all supported systems
      devShells = builtins.listToAttrs (map (system: {
        name = system;
        value = mkDevShell system;
      }) systems);

      # Hugo website build derivations
      packages = builtins.listToAttrs (map (system: {
        name = system;
        value = mkQGISPlanetWebsite system;
      }) systems);
    };
}