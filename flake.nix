{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ flake-parts, self, nixpkgs, nixpkgs-unstable, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      perSystem = { config, pkgs, system, ... }:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
        in {
          devShells = {
            default = pkgs.mkShell {
              name = "env";
              nativeBuildInputs = [ ];
              buildInputs = [
                pkgs.cruft
                pkgs.cookiecutter
                pkgs.ripgrep
                pkgs.sd
                pkgs.just
              ];
              packages = [ ];
            };
          };
        };
    };
}
