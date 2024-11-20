# bibtex-kirby
[![GHA workflow badge](https://github.com/Uxusino/bibtex-kirby/workflows/CI/badge.svg)](https://github.com/Uxusino/bibtex-kirby/actions)

* [Product Backlog](https://docs.google.com/spreadsheets/d/1cU50iwuRWAjs2o86rISFNLVATdS2hZPp1eciziTLBD8/edit?gid=0#gid=0)
* [Sprint Backlog](https://github.com/users/Uxusino/projects/3/views/1)

## Asennus

1. Riippuvuudet:

```
poetry install
```

2. Build:

```
poetry run invoke build
```

3. Käynnistys:

```
poetry run invoke start
```

## Muut komennot

### Testaus

1. Yksikkötestaus:

```
poetry run invoke unittest
```