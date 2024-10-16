# bapp-template

## Usage

This is a cookiecutter template repo for initializing a default Beepy App.

To run, clone this repo and run:

```
$ pipx install cookiecutter
$ cookiecutter bapp-template
```

Alternatively, you can run `cookiecutter gh:conor-f/bapp-template` to avoid
having to clone the repo.

Note that you will need to manually tag the repo you push this to on Github
with the tag `beepy-app` in order for it to appear in the app store.


## Features

- [x] Basic template with `bapp-details.json` and working `justfile`
- [x] Sample application using `textual` for UI layout
- [x] Pre-commit hooks for linting, type-checking, etc
- [x] Basic tests scaffolding
- [x] CI/CD with Github Actions for testing/deploying to PyPi
