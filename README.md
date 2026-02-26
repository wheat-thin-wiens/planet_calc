# planet_calc

A small CLI tool for visually representing planet scaling in Balatro.

### Installation

```bash
git clone https://github.com/wheat-thin-wiens/planet_calc
cd planet_calc
pip install -e .
```

### Usage

The `table` command shows a table of planet levels for a given range (default 1 - 10).
```bash
planet-calc table --min 1 --max 10
```

The `graph` command displays a graph of the base scores of a hand for a given range (default 1 - 10).
```bash
planet-calc graph --min 1 --max 10
```

The `level` command returns the chips, mult and base score for a selected hand at a given level.
An `int` must be provided.
```bash
planet-calc level 5
```
