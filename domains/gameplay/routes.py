from flask import Blueprint, session, jsonify, request
from logic.blackjack_game import BlackjackGame
from models.user import User

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST'])
def start_game():
    game = BlackjackGame()
    session['game'] = game.__dict__  # Save game state to session
    return jsonify(game.get_game_state())

@game_bp.route('/hit', methods=['POST'])
def hit():
    game = BlackjackGame()
    game.__dict__ = session.get('game', {})
    game.player_hit()
    session['game'] = game.__dict__
    return jsonify(game.get_game_state())
