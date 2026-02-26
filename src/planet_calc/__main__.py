import matplotlib.pyplot as plt
from pandas import DataFrame
from pick import pick
import typer

from planet_calc.hands import HANDS

HAND_LIST = list(HANDS.keys())

app = typer.Typer()

def calculate_levels(hand: str, min: int, max: int) -> dict[int, list[int]]:
    base_chips = HANDS.get(hand)["base_chips"]  #type: ignore
    plus_chips = HANDS.get(hand)["plus_chips"]  #type: ignore
    base_mult = HANDS.get(hand)["base_mult"]    #type: ignore
    plus_mult = HANDS.get(hand)["plus_mult"]    #type: ignore

    level_values: dict[int, list[int]] = {}
    x = min

    while x <= max:
        chips = base_chips + (plus_chips * (x - 1))
        mult = base_mult + (plus_mult * (x - 1))

        this_level = [chips, mult, chips * mult]

        level_values[x] = this_level

        x += 1

    return level_values

def calculate_base_score(hand: str, min: int, max: int) -> dict[int, int]:
    base_chips = HANDS.get(hand)["base_chips"]  #type: ignore
    plus_chips = HANDS.get(hand)["plus_chips"]  #type: ignore
    base_mult = HANDS.get(hand)["base_mult"]    #type: ignore
    plus_mult = HANDS.get(hand)["plus_mult"]    #type: ignore

    level_values: dict[int, int] = {}
    x = min

    while x <= max:
        chips = base_chips + (plus_chips * (x - 1))
        mult = base_mult + (plus_mult * (x - 1))
        base_score = chips * mult

        level_values[x] = base_score

        x += 1
        
    return level_values

@app.command()
def table(min: int = 1, max: int = 10):
    title = "Select hand"
    selected = pick(title=title, options=HAND_LIST, indicator=">")[0]

    level_values = calculate_levels(str(selected), min, max)

    print(f"{selected}\n")
    index = ["Chips", "Mult", "Score"]
    df = DataFrame(level_values, index=index).transpose()
    print(df)

@app.command()
def graph(min: int = 1, max: int = 10):
    title = "Select hand"
    selected = pick(title=title, options=HAND_LIST, indicator=">")[0]

    level_values = calculate_base_score(str(selected), min, max)

    print(f"{selected}")
    index = list(level_values.keys())
    df = DataFrame(level_values, index=index).transpose()

    df.plot(legend=False)
    plt.xticks(range(min, max + 1))
    plt.show()

@app.command()
def level(level: int):
    title = "Select hand"
    selected = pick(title=title, options=HAND_LIST, indicator=">")[0]

    base_chips = HANDS.get(selected)["base_chips"]  #type: ignore
    plus_chips = HANDS.get(selected)["plus_chips"]  #type: ignore
    base_mult = HANDS.get(selected)["base_mult"]    #type: ignore
    plus_mult = HANDS.get(selected)["plus_mult"]    #type: ignore

    chips = base_chips + (plus_chips * (level - 1))
    mult = base_mult + (plus_mult * (level - 1))

    print(f"{selected} Level {level}")
    print(f"Chips: {chips} Mult: {mult} Score: {chips * mult}")


if __name__ == "__main__":
    app()
