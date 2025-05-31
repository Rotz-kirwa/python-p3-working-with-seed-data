#!/usr/bin/env python3

from models import Game
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()

games = session.query(Game).all()
for game in games:
    print(f"{game.id}. {game.title} - {game.platform} - {game.genre} - ${game.price}")