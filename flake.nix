{
  description = "Development environment and build process for a Hugo app with Python requirements";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;

      nixpkgsFor = forAllSystems (system: import nixpkgs { 
        inherit system; 
        config.allowUnfree = true;
      });

      mkDevShell = system: 
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              hugo                          # Hugo for building the website
              vscode                        # VSCode for development
              python312Packages.feedparser  # Python package: feedparser
              python312Packages.requests    # Python package: requests
              python312Packages.pillow      # Python package: Pillow
              python312Packages.python-dateutil # Python package: dateutil
              gnumake                       # GNU Make for build automation
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
              echo ""
              echo "🪛 Hugo:"
              echo "--------------------------------"
              echo "Start Hugo like this:"
              echo ""
              echo "hugo server"
              echo "-----------------------"
            '';
          };
        };

    in
    {
      devShells = builtins.listToAttrs (map (system: {
        name = system;
        value = mkDevShell system;
      }) supportedSystems);

      packages = builtins.listToAttrs (map (system: {
        name = system;
        value = {
          qgis-planet-website = nixpkgsFor.${system}.callPackage ./package.nix {};
        };
      }) supportedSystems);
    };
}
