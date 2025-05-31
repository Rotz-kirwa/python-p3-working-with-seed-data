#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear existing data
    print("Clearing existing games...")
    session.query(Game).delete()
    session.commit()
    
    # Seed with new data
    print("Seeding games...")
    
    # Create predefined games
    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    ccs = Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0)
    
    session.bulk_save_objects([botw, ffvii, mk8, ccs])
    
    # Generate 50 random games
    platforms = ["PC", "Switch", "Playstation", "Xbox", "Mobile", "Arcade"]
    genres = ["Action", "Adventure", "RPG", "Strategy", "Puzzle", "Sports", "Simulation", "Racing"]
    
    games = [
        Game(
            title=fake.sentence(nb_words=3)[:-1],  # Remove period at end
            genre=random.choice(genres),
            platform=random.choice(platforms),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]
    
    session.bulk_save_objects(games)
    session.commit()
    
    print(f"Done! Added {session.query(Game).count()} games to the database.")