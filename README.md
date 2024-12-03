# bibtex-kirby
[![GHA workflow badge](https://github.com/Uxusino/bibtex-kirby/workflows/CI/badge.svg)](https://github.com/Uxusino/bibtex-kirby/actions)

* [Product Backlog](https://docs.google.com/spreadsheets/d/1cU50iwuRWAjs2o86rISFNLVATdS2hZPp1eciziTLBD8/edit?gid=0#gid=0)
* [Sprint Backlog](https://github.com/users/Uxusino/projects/3/views/1)
* [Burndown Chart](https://docs.google.com/spreadsheets/d/1cU50iwuRWAjs2o86rISFNLVATdS2hZPp1eciziTLBD8/edit?gid=334129755#gid=334129755)

## Setup

1. Dependencies:

```
poetry install
```

2. Build:

```
poetry run invoke build
```

If there is no .env file in the folder, this command will create a new one with custom settings.

3. Start:

```
poetry run invoke start
```

## Other commands

### Testing

1. Unit testing:

```
poetry run invoke unittest
```

2. Robot tests:

```
poetry run invoke robot
```

## Definition of Done
- The user story and its acceptance criteria have been implemented.
- Unit tests are complete and pass successfully.
- End-to-End robot tests are complete and pass successfully.
- The code passes the CI process.
- The code review is complete.

## License

This project is released under the [Unlicense](LICENSE).

