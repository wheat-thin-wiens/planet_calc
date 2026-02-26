HANDS: dict[str, dict[str, int]] = {
    "High Card": {
        "base_chips": 5,
        "base_mult": 1,
        "plus_chips": 10,
        "plus_mult": 1
    },
    "Pair": {
        "base_chips": 10,
        "base_mult": 2,
        "plus_chips": 15,
        "plus_mult": 1
    },
    "Two Pair": {
        "base_chips": 20,
        "base_mult": 2,
        "plus_chips": 20,
        "plus_mult": 1
    },
    "Three of a Kind": {
        "base_chips": 30,
        "base_mult": 3,
        "plus_chips": 20,
        "plus_mult": 2
    },
    "Four of a Kind": {
        "base_chips": 60,
        "base_mult": 7,
        "plus_chips": 30,
        "plus_mult": 3
    },
    "Full House": {
        "base_chips": 40,
        "base_mult": 4,
        "plus_chips": 25,
        "plus_mult": 2
    },
    "Flush": {
        "base_chips": 35,
        "base_mult": 4,
        "plus_chips": 15,
        "plus_mult": 2
    },
    "Straight": {
        "base_chips": 30,
        "base_mult": 4,
        "plus_chips": 30,
        "plus_mult": 3
    },
    "Straight Flush": {
        "base_chips": 100,
        "base_mult": 8,
        "plus_chips": 40,
        "plus_mult": 4
    },
    "Five of a Kind": {
        "base_chips": 120,
        "base_mult": 12,
        "plus_chips": 35,
        "plus_mult": 3
    },
    "Flush Five": {
        "base_chips": 160,
        "base_mult": 16,
        "plus_chips": 50,
        "plus_mult": 3
    },
    "Flush House": {
        "base_chips": 140,
        "base_mult": 14,
        "plus_chips": 40,
        "plus_mult": 4
    },
    "Royal Flush": {
        "base_chips": 100,
        "base_mult": 8,
        "plus_chips": 40,
        "plus_mult": 4
    }
}
