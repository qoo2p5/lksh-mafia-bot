from bot.state import *
from telegram import Update


def create_game(update: Update, text: str, user: User) -> None:
    assert user.status == UserStatus.CREATING

    if text.lower() == 'старт':
        game = user.creating_game
        user.creating_game = None
        state.game_by_id[game.game_id] = game

        update.message.reply_text(messages.GAME_CREATED.format(
            user_count=len(game.roles),
            roles=', '.join(game.roles),
            game_id=game.game_id
        ))

        user.join_game(game, update)
        return

    role = text
    roles = user.creating_game.roles
    roles.append(role)
    update.message.reply_text(messages.ROLE_ADDED.format(
        user_count=len(roles),
        roles=', '.join(roles)
    ))
