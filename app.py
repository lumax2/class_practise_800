from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 定义卡牌类
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    # 将 Card 对象转换为字典
    def to_dict(self):
        return {"suit": self.suit, "value": self.value}

    # 从字典恢复为 Card 对象
    @staticmethod
    def from_dict(card_dict):
        return Card(card_dict['suit'], card_dict['value'])

# 定义牌堆类
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
                      for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

# 计算手牌点数
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card.value in ["J", "Q", "K"]:
            value += 10
        elif card.value == "A":
            aces += 1
            value += 11
        else:
            value += int(card.value)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    # 初始化牌堆、玩家和庄家的手牌
    deck = Deck()
    player_hand = [deck.draw_card(), deck.draw_card()]
    dealer_hand = [deck.draw_card(), deck.draw_card()]

    # 将手牌对象转换为字典并存储到 session
    session['player_hand'] = [card.to_dict() for card in player_hand]
    session['dealer_hand'] = [card.to_dict() for card in dealer_hand]
    session['deck'] = [card.to_dict() for card in deck.cards]
    session['game_over'] = False

    return redirect(url_for('game'))

@app.route('/game')
def game():
    # 从 session 恢复卡牌对象
    player_hand = [Card.from_dict(card) for card in session['player_hand']]
    dealer_hand = [Card.from_dict(card) for card in session['dealer_hand']]
    player_value = calculate_hand_value(player_hand)

    if player_value > 21:
        session['game_over'] = True

    return render_template('game.html', player_hand=player_hand, dealer_hand=dealer_hand, player_value=player_value,
                           game_over=session['game_over'])

@app.route('/hit')
def hit():
    if not session.get('game_over'):
        # 恢复牌堆并抽牌
        deck = [Card.from_dict(card) for card in session['deck']]
        new_card = deck.pop()
        player_hand = [Card.from_dict(card) for card in session['player_hand']]
        player_hand.append(new_card)

        # 更新 session 中的手牌和牌堆
        session['player_hand'] = [card.to_dict() for card in player_hand]
        session['deck'] = [card.to_dict() for card in deck]

    return redirect(url_for('game'))

@app.route('/stand')
def stand():
    # 恢复玩家和庄家的手牌
    dealer_hand = [Card.from_dict(card) for card in session['dealer_hand']]
    player_value = calculate_hand_value([Card.from_dict(card) for card in session['player_hand']])
    deck = [Card.from_dict(card) for card in session['deck']]

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        result = 'You win!'
    elif dealer_value == player_value:
        result = "It's a tie!"
    else:
        result = 'Dealer wins!'

    session['game_over'] = True
    return render_template('game.html', player_hand=session['player_hand'], dealer_hand=[card.to_dict() for card in dealer_hand],
                           player_value=player_value, dealer_value=dealer_value, result=result, game_over=True)

if __name__ == '__main__':
    app.run(debug=True)
