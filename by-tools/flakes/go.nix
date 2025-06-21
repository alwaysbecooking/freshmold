{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };
    gomod2nix = {
      url = "github:nix-community/gomod2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ flake-parts, self, nixpkgs, gomod2nix, nixpkgs-unstable, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      perSystem = { config, pkgs, system, ... }:
        let
          pkgs = import nixpkgs {
            inherit system;
            overlays = [ gomod2nix.overlays.default ];
          };
          src = ./.;
          lib = pkgs.lib;
          version = builtins.substring 0 8 self.lastModifiedDate;
        in {
          packages = {
            ## build with: nix build --no-eval-cache .#server
            # server = pkgs.buildGoApplication {
            #   pname = "server";
            #   inherit version;
            #   src = ./.;
            #   # NOTE: we need to manually run "gomod2nix" if the file doesn't
            #   #       exist in the directory
            #   modules = ./gomod2nix.toml;
            #   subPackages = [ "cmd/some_dile" ];
            # };

            # # build with: nix build --no-eval-cache .#server_docker
            # server_docker = pkgs.dockerTools.buildLayeredImage {
            #   name = "${builtins.getEnv "ECR_REGISTRY"}/${builtins.getEnv "ECR_REPOSITORY"}";
            #   tag = builtins.getEnv "IMAGE_TAG";
            #   contents = with pkgs; [ server cacert ];
            #   config = {
            #   # TODO
            #   };
            # };
          };

          devShells = {
            default = pkgs.mkShell {
              name = "env";
              env = { GOROOT = pkgs.go + "/share/go"; };
              # https://github.com/go-delve/delve/issues/3085
              hardeningDisable = [ "fortify" ];
              nativeBuildInputs = [ ];
              buildInputs = [
                pkgs.go
                pkgs.gotestsum
                pkgs.gofumpt
                pkgs.golangci-lint
                pkgs.gomod2nix

                # pkgs.just
                # unstable.sqlc
                pkgs.delve
                # unstable.duckdb
              ];
              packages = [ ];
              shellHook = ''
                export LD_LIBRARY_PATH="${
                  pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc ]
                }"
              '';

            };
          };
        };
    };
}
