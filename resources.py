combinations = ['Комбінація', 'Одиниці', 'Двійки', 'Трійки', 'Четверки', 'П\'ятірки', 'Шістки', 'Сет', 'Каре', 'Фулл Хаус', 'Малий стріт', 'Великий стріт', 'Яхта', 'Будь-яка', 'Підсумок']
combs = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Set', 'Quad', 'FullHouse', 'ShortStraight', 'LongStraight', 'Yahtzee', 'Any']
combpoints = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Set': 0, 'Quad': 0, 'FullHouse': 0, 'ShortStraight': 0, 'LongStraight': 0, 'Yahtzee': 0, 'Any': 0}

data = {
    'canContinue': False,
    'playerCount': 2,
    'playerTurn': 0,
    'turnCount': 0,
    'rolls': 3,
    'diceOne': 0,
    'diceTwo': 0,
    'diceThree': 0,
    'diceFour': 0,
    'diceFive': 0,
    'stats': [{
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Set": -1,
            "Quad": -1,
            "FullHouse": -1,
            "ShortStraight": -1,
            "LongStraight": -1,
            "Yahtzee": -1,
            "Any": -1
        }, {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Set": -1,
            "Quad": -1,
            "FullHouse": -1,
            "ShortStraight": -1,
            "LongStraight": -1,
            "Yahtzee": -1,
            "Any": -1
        }, {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Set": -1,
            "Quad": -1,
            "FullHouse": -1,
            "ShortStraight": -1,
            "LongStraight": -1,
            "Yahtzee": -1,
            "Any": -1
        }, {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Set": -1,
            "Quad": -1,
            "FullHouse": -1,
            "ShortStraight": -1,
            "LongStraight": -1,
            "Yahtzee": -1,
            "Any": -1
    }]

}