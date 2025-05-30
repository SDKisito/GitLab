from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle de données pour la route POST
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# Route GET simple
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI CI/CD avec GitLab"}

# Route GET avec paramètre
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Bonjour, {name} !"}

# Route POST
@app.post("/items/")
def create_item(item: Item):
    return {"item_received": item}
