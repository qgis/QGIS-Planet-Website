{
  description = "Development environment for Hugo app with Python requirements";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }:
    let
      # Import nixpkgs for all systems
      systems = [ "x86_64-linux" "x86_64-darwin" ];
      mkDevShell = system: let
        pkgs = import nixpkgs { 
          inherit system; 
          config = { allowUnfree = true; };
        };
      in pkgs.mkShell {
        packages = with pkgs; [
          hugo
          vscode
          python312Packages.feedparser
          python312Packages.requests
          python312Packages.pillow
          python312Packages.python-dateutil
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
          echo "On running, it will install hugo related extensions."
          echo ""
          echo "🪛 Hugo:"
          echo "--------------------------------"
          echo "Start hugo like this:"
          echo ""
          echo "hugo server"
        '';
      };
    in {
      devShells = builtins.listToAttrs (map (system: {
        name = system;
        value = { default = mkDevShell system; };
      }) systems);
    };
}