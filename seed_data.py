from database import get_db, init_db

SAMPLE_PETS = [
    {
        'name': 'Max',
        'species': 'Dog',
        'breed': 'Golden Retriever',
        'age': 2,
        'size': 'Large',
        'gender': 'Male',
        'description': 'Max is a friendly and energetic Golden Retriever who loves playing fetch and cuddling on the couch. He gets along wonderfully with children and other dogs.',
        'photo_url': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Luna',
        'species': 'Cat',
        'breed': 'Siamese Mix',
        'age': 3,
        'size': 'Small',
        'gender': 'Female',
        'description': 'Luna is a graceful Siamese mix with stunning blue eyes. She loves quiet evenings and will curl up on your lap for hours. Perfect for apartment living.',
        'photo_url': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Buddy',
        'species': 'Dog',
        'breed': 'Labrador Mix',
        'age': 1,
        'size': 'Large',
        'gender': 'Male',
        'description': 'Buddy is a playful young Labrador mix who is still learning the ropes. He\'s quick to learn and loves everyone he meets! Great with kids.',
        'photo_url': 'https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 0
    },
    {
        'name': 'Whiskers',
        'species': 'Cat',
        'breed': 'Tabby',
        'age': 5,
        'size': 'Medium',
        'gender': 'Male',
        'description': 'Whiskers is a laid-back tabby who enjoys sunny spots and long naps. He\'s perfect for a calm household and gets along well with gentle dogs too.',
        'photo_url': 'https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Bella',
        'species': 'Dog',
        'breed': 'Husky',
        'age': 3,
        'size': 'Large',
        'gender': 'Female',
        'description': 'Bella is a stunning Husky with striking blue eyes and a playful spirit. She loves outdoor adventures and would thrive with an active family.',
        'photo_url': 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Coco',
        'species': 'Cat',
        'breed': 'Persian',
        'age': 4,
        'size': 'Medium',
        'gender': 'Female',
        'description': 'Coco is a fluffy Persian princess who loves being pampered. She\'s gentle, calm, and absolutely perfect for quiet, loving homes.',
        'photo_url': 'https://images.unsplash.com/photo-1561948955-570b270e7c36?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Charlie',
        'species': 'Dog',
        'breed': 'Corgi',
        'age': 2,
        'size': 'Small',
        'gender': 'Male',
        'description': 'Charlie is an adorable Corgi with boundless energy and the cutest little legs. He brings joy to everyone around him and loves learning new tricks!',
        'photo_url': 'https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 1
    },
    {
        'name': 'Mochi',
        'species': 'Cat',
        'breed': 'British Shorthair',
        'age': 1,
        'size': 'Small',
        'gender': 'Female',
        'description': 'Mochi is a round-faced British Shorthair kitten with a love for play and exploration. She\'s very sociable and loves meeting new people.',
        'photo_url': 'https://images.unsplash.com/photo-1596854407944-bf87f6fdd49e?w=400&h=300&fit=crop',
        'status': 'Available',
        'vaccinated': 1,
        'neutered': 0
    }
]


def seed():
    init_db()
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM pets')
    count = cursor.fetchone()[0]

    if count == 0:
        for pet in SAMPLE_PETS:
            cursor.execute('''
                INSERT INTO pets (name, species, breed, age, size, gender, description, photo_url, status, vaccinated, neutered)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                pet['name'], pet['species'], pet['breed'], pet['age'],
                pet['size'], pet['gender'], pet['description'],
                pet['photo_url'], pet['status'], pet['vaccinated'], pet['neutered']
            ))
        conn.commit()
        print(f'[OK] Seeded {len(SAMPLE_PETS)} sample pets into database')
    else:
        print(f'[INFO] Database already contains {count} pets - skipping seed')

    conn.close()


if __name__ == '__main__':
    seed()
