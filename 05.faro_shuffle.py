import copy
card_data = input().split()
shuffles = int(input())

left_card = card_data[0]
right_card = card_data[-1]

shuffle_cards = []
card_data = copy.deepcopy(card_data)
half_cards = len(card_data) // 2

for shuffle in range (shuffles):

    left_deck = []
    right_deck = []

    for index in range(1, half_cards):
        left_deck.append(card_data[index])

    for index in range(half_cards, len(card_data) - 1):
        right_deck.append(card_data[index])

    for index in range(len(left_deck)):
        shuffle_cards.append(right_deck[index])
        shuffle_cards.append(left_deck[index])

    card_data = shuffle_cards.copy()
    card_data.append(right_card)
    card_data.insert(0, left_card)
    shuffle_cards = []

print(card_data)