import os

# Utilisation d'une expression conditionnelle pour définir SQLALCHEMY_DATABASE_URI
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/meet_db")
# Remplacer "postgresql://" par "postgresql://" une seule fois si DATABASE_URL commence par "postgres://"
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS=False