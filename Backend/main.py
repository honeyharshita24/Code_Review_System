from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai 
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CodeSnippet(Base):
    __tablename__ = "code_snippets"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    snippet_id = Column(Integer, ForeignKey("code_snippets.id"))
    feedback = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

#  Gemini Configuration 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Add to .env
model = genai.GenerativeModel('gemini-1.5-flash')  # Or 'gemini-pro'

class CodeRequest(BaseModel):
    code: str

@app.get("/")
async def home():
    return "Hello Mani"

@app.post("/review")
async def review_code(request : CodeRequest):
    db = SessionLocal()
    db_snippet = CodeSnippet(code=request.code)
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)

    # Gemini API Call
    try:
        response = model.generate_content(
            f"Act as a senior software engineer. Review this code and suggest improvements:\n\n{request.code}\n\nFormat feedback as bullet points."
        )
        feedback = response.text
    except Exception as e:
        feedback = f"Error getting feedback: {str(e)}"

    
    db_review = Review(snippet_id=db_snippet.id, feedback=feedback)
    db.add(db_review)
    db.commit()

    return {"feedback": feedback}