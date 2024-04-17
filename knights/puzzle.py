from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge_base = And(
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledge_base,
    Implication(Not(And(AKnight, AKnave)), AKnave),
    Implication(And(AKnight, AKnave), AKnight),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledge_base,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledge_base,
    # A says "We are the same kind."
    Implication(AKnight, Or(And(BKnight, AKnight), And(BKnave, AKnave))),
    Implication(AKnave, Not(Or(And(BKnight, AKnight), And(BKnave, AKnave)))),
    # B says "We are of different kinds."
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(BKnight, AKnave)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    knowledge_base,
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Or(
        Implication(
            BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
        ),
        Implication(
            BKnave,
            Not(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
        ),
    ),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
