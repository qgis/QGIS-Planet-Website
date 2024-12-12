{
  description = "Development environment and build process for a Hugo app with Python requirements";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }: 
    let
      system = "x86_64-linux";

      # Importing packages from nixpkgs
      pkgs = import nixpkgs {
        inherit system;
      };
      
      mkDevShell = let
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
    in
    {
      devShells = {
        value = mkDevShell;
      };

      packages = {
        x86_64-linux = {
          qgis-planet-website = pkgs.callPackage ./packages/qgis-planet-website.nix {};
        };
      };
    };
}
