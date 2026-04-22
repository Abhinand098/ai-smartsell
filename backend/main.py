from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import io
import psycopg2
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    title: str
    description: str
    category: str
    price: int

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model + processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

conn = psycopg2.connect(
    host="localhost",
    database="marketplace",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    category TEXT,
    price INTEGER
)
""")
conn.commit()

@app.get("/")
def home():
    return {"message": "AI Marketplace running"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    product_data = generate_product_details(caption)

    return product_data

def generate_product_details(caption: str):
    caption_lower = caption.lower()

    # Simple category detection
    if "shoe" in caption_lower:
        category = "Footwear"
        price = 1999
    elif "laptop" in caption_lower:
        category = "Electronics"
        price = 40000
    elif "chair" in caption_lower:
        category = "Furniture"
        price = 1500
    else:
        category = "General"
        price = 999

    # Title (capitalize)
    title = caption.title()

    # Description
    description = f"This is a {caption}. It is in good condition and ready to use."

    return {
        "title": title,
        "description": description,
        "category": category,
        "price": price
    }
def save_to_db(data):
    cursor.execute(
        "INSERT INTO items (title, description, category, price) VALUES (%s, %s, %s, %s)",
        (data['title'], data['description'], data['category'], data['price'])
    )
    conn.commit()

@app.post("/save/")
def save_product(product: Product):
    data = product.dict()

    save_to_db(data)

    return {"message": "Product saved successfully"}
