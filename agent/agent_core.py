import os
import time
from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Database Integration (Supabase/PostgreSQL)
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Sentry Integration
import sentry_sdk

# Hugging Face and External AI APIs Integration
from transformers import pipeline
from openai import OpenAI
import google.generativeai as genai
# from elevenlabs import set_api_key, generate, play
# from perplexity_ai import PerplexityAI

# Google API imports for Gmail and Calendar
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Notion Integration
from notion_client import Client

app = FastAPI()

# --- Database Integration (Supabase/PostgreSQL) ---
DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

class AgentLog(Base):
    __tablename__ = "agent_logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    level = Column(String)
    message = Column(Text)

class AgentMemory(Base):
    __tablename__ = "agent_memory"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    key = Column(String, unique=True, index=True)
    value = Column(Text)

engine = None
SessionLocal = None

if DATABASE_URL:
    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(bind=engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("Supabase/PostgreSQL integration initialized.")

        # Example usage: Log an event
        def log_to_db(level: str, message: str):
            if SessionLocal:
                db = SessionLocal()
                try:
                    log_entry = AgentLog(level=level, message=message)
                    db.add(log_entry)
                    db.commit()
                    db.refresh(log_entry)
                finally:
                    db.close()

        # Example usage: Save/Load memory
        def save_memory_to_db(key: str, value: str):
            if SessionLocal:
                db = SessionLocal()
                try:
                    memory_entry = db.query(AgentMemory).filter(AgentMemory.key == key).first()
                    if memory_entry:
                        memory_entry.value = value
                    else:
                        memory_entry = AgentMemory(key=key, value=value)
                        db.add(memory_entry)
                    db.commit()
                    db.refresh(memory_entry)
                finally:
                    db.close()

        def load_memory_from_db(key: str) -> str | None:
            if SessionLocal:
                db = SessionLocal()
                try:
                    memory_entry = db.query(AgentMemory).filter(AgentMemory.key == key).first()
                    return memory_entry.value if memory_entry else None
                finally:
                    db.close()
            return None

        log_to_db("INFO", "Agent started and connected to Supabase.")
        save_memory_to_db("last_startup", datetime.utcnow().isoformat())

    except Exception as e:
        print(f"Error initializing Supabase/PostgreSQL: {e}")
        engine = None
        SessionLocal = None
else:
    print("DATABASE_URL not set. Supabase/PostgreSQL integration skipped.")

# --- Sentry Integration ---
SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
    print("Sentry integration initialized.")
else:
    print("SENTRY_DSN not set. Sentry integration skipped.")

# --- Hugging Face and External AI APIs Integration ---

# Hugging Face
hf_pipeline = None
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

if HUGGING_FACE_API_KEY:
    try:
        # Example: sentiment-analysis pipeline
        # hf_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        print("Hugging Face integration configured (pipeline not loaded by default).")
    except Exception as e:
        print(f"Error initializing Hugging Face: {e}")
else:
    print("HUGGING_FACE_API_KEY not set. Hugging Face integration skipped.")

# OpenAI (ChatGPT)
openai_client = None
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    try:
        openai_client = OpenAI(api_key=OPENAI_API_KEY)
        print("OpenAI (ChatGPT) integration initialized.")
    except Exception as e:
        print(f"Error initializing OpenAI: {e}")
else:
    print("OPENAI_API_KEY not set. OpenAI integration skipped.")

# Google Gemini
gemini_model = None
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

if GOOGLE_GEMINI_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel("gemini-pro")
        print("Google Gemini integration initialized.")
    except Exception as e:
        print(f"Error initializing Google Gemini: {e}")
else:
    print("GOOGLE_GEMINI_API_KEY not set. Google Gemini integration skipped.")

# ElevenLabs
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if ELEVENLABS_API_KEY:
    try:
        # set_api_key(ELEVENLABS_API_KEY)
        print("ElevenLabs integration configured (API key set).")
    except Exception as e:
        print(f"Error initializing ElevenLabs: {e}")
else:
    print("ELEVENLABS_API_KEY not set. ElevenLabs integration skipped.")

# Perplexity AI
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

if PERPLEXITY_API_KEY:
    try:
        # perplexity_client = PerplexityAI(api_key=PERPLEXITY_API_KEY)
        print("Perplexity AI integration configured (API key set).")
    except Exception as e:
        print(f"Error initializing Perplexity AI: {e}")
else:
    print("PERPLEXITY_API_KEY not set. Perplexity AI integration skipped.")

print("External AI APIs integration setup complete.")

# --- MCP Personalizado (Model Context Protocol) Integration - Conceptual Framework ---

class MCPTool:
    """Representa uma ferramenta ou capacidade exposta por um servidor MCP."""
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func

    def execute(self, *args, **kwargs):
        print(f"Executing MCP Tool: {self.name} with args: {args}, kwargs: {kwargs}")
        return self.func(*args, **kwargs)

# Exemplo de função que poderia ser exposta via MCP
def analyze_code_mcp(code: str) -> str:
    """Simula a análise de código por um subagente MCP."""
    print(f"MCP Subagent: Analyzing code...\n{code}")
    # Aqui você integraria um subagente real para análise de código
    return f"Code analysis for '{code[:50]}...' completed by MCP subagent."

def send_email_mcp(recipient: str, subject: str, body: str) -> str:
    """Simula o envio de e-mail por um subagente MCP."""
    print(f"MCP Subagent: Sending email to {recipient} with subject '{subject}'.")
    # Aqui você integraria um subagente real para envio de e-mails
    return f"Email to {recipient} sent by MCP subagent."

mcp_tools = {
    "analyze_code": MCPTool("analyze_code", "Analisa um trecho de código para bugs e melhorias.", analyze_code_mcp),
    "send_email": MCPTool("send_email", "Envia um e-mail para um destinatário específico.", send_email_mcp),
}

print("MCP Personalizado conceptual framework initialized.")

# --- Gmail Integration ---

SCOPES_GMAIL = ["https://www.googleapis.com/auth/gmail.modify"]
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
GMAIL_REDIRECT_URI = os.getenv("GMAIL_REDIRECT_URI")

gmail_service = None

if GMAIL_CLIENT_ID and GMAIL_CLIENT_SECRET and GMAIL_REDIRECT_URI:
    try:
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = Credentials.from_authorized_user_file('token.pickle', SCOPES_GMAIL)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES_GMAIL, redirect_uri=GMAIL_REDIRECT_URI)
                # This part would typically involve a browser interaction
                # For a headless environment, you might need to use a different flow
                # or have the user manually paste the URL and then the code.
                # print(f"Please go to this URL: {flow.authorization_url}")
                # code = input('Enter the authorization code: ')
                # flow.fetch_token(code=code)
                # creds = flow.credentials
                print("Gmail: Manual OAuth flow required. Please generate token.pickle manually.")
                creds = None # Ensure creds is None if manual step is needed

            # Save the credentials for the next run
            if creds and creds.valid:
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

        if creds and creds.valid:
            gmail_service = build('gmail', 'v1', credentials=creds)
            print("Gmail integration initialized.")
        else:
            print("Gmail integration requires manual token generation. Skipping service initialization.")

    except Exception as e:
        print(f"Error initializing Gmail integration: {e}")
        gmail_service = None
else:
    print("GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, or GMAIL_REDIRECT_URI not set. Gmail integration skipped.")

# --- Google Calendar Integration ---

SCOPES_CALENDAR = ["https://www.googleapis.com/auth/calendar.events"]
GOOGLE_CALENDAR_CLIENT_ID = os.getenv("GOOGLE_CALENDAR_CLIENT_ID")
GOOGLE_CALENDAR_CLIENT_SECRET = os.getenv("GOOGLE_CALENDAR_CLIENT_SECRET")
GOOGLE_CALENDAR_REDIRECT_URI = os.getenv("GOOGLE_CALENDAR_REDIRECT_URI")

google_calendar_service = None

if GOOGLE_CALENDAR_CLIENT_ID and GOOGLE_CALENDAR_CLIENT_SECRET and GOOGLE_CALENDAR_REDIRECT_URI:
    try:
        creds_calendar = None
        if os.path.exists('calendar_token.pickle'):
            with open('calendar_token.pickle', 'rb') as token:
                creds_calendar = Credentials.from_authorized_user_file('calendar_token.pickle', SCOPES_CALENDAR)

        if not creds_calendar or not creds_calendar.valid:
            if creds_calendar and creds_calendar.expired and creds_calendar.refresh_token:
                creds_calendar.refresh(Request())
            else:
                flow_calendar = InstalledAppFlow.from_client_secrets_file(
                    'calendar_credentials.json', SCOPES_CALENDAR, redirect_uri=GOOGLE_CALENDAR_REDIRECT_URI)
                print("Google Calendar: Manual OAuth flow required. Please generate calendar_token.pickle manually.")
                creds_calendar = None

            if creds_calendar and creds_calendar.valid:
                with open('calendar_token.pickle', 'wb') as token:
                    pickle.dump(creds_calendar, token)

        if creds_calendar and creds_calendar.valid:
            google_calendar_service = build('calendar', 'v3', credentials=creds_calendar)
            print("Google Calendar integration initialized.")
        else:
            print("Google Calendar integration requires manual token generation. Skipping service initialization.")

    except Exception as e:
        print(f"Error initializing Google Calendar integration: {e}")
        google_calendar_service = None
else:
    print("GOOGLE_CALENDAR_CLIENT_ID, GOOGLE_CALENDAR_CLIENT_SECRET, or GOOGLE_CALENDAR_REDIRECT_URI not set. Google Calendar integration skipped.")

# --- Notion Integration ---
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
notion_client = None

if NOTION_API_KEY:
    try:
        notion_client = Client(auth=NOTION_API_KEY)
        print("Notion integration initialized.")
    except Exception as e:
        print(f"Error initializing Notion integration: {e}")
        notion_client = None
else:
    print("NOTION_API_KEY not set. Notion integration skipped.")

# --- Zapier Integration ---
ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

# This integration is primarily via webhooks, so no client initialization here.
# Functions to send data to Zapier would be implemented as needed.
if ZAPIER_WEBHOOK_URL:
    print("Zapier integration configured (webhook URL set).")
else:
    print("ZAPIER_WEBHOOK_URL not set. Zapier integration skipped.")


@app.get("/")
async def read_root():
    return {"message": "ManusAI-Clone Agent is running!"}

@app.get("/status")
async def get_status():
    status = {
        "database_connected": engine is not None,
        "sentry_initialized": SENTRY_DSN is not None,
        "openai_connected": openai_client is not None,
        "gemini_connected": gemini_model is not None,
        "gmail_connected": gmail_service is not None,
        "google_calendar_connected": google_calendar_service is not None,
        "notion_connected": notion_client is not None,
        "zapier_webhook_configured": ZAPIER_WEBHOOK_URL is not None,
        "mcp_tools_available": len(mcp_tools) > 0
    }
    return status

# Example endpoint for MCP tool execution
@app.post("/mcp/execute/{tool_name}")
async def execute_mcp_tool(tool_name: str, payload: dict):
    if tool_name in mcp_tools:
        tool = mcp_tools[tool_name]
        result = tool.execute(**payload)
        return {"tool": tool_name, "result": result}
    raise HTTPException(status_code=404, detail="MCP Tool not found")

# Example endpoint for Gmail operations (conceptual)
@app.post("/gmail/send")
async def send_gmail_message(recipient: str, subject: str, body: str):
    if gmail_service:
        # Implement actual Gmail sending logic here
        return {"status": "success", "message": f"Attempted to send email to {recipient}"}
    raise HTTPException(status_code=500, detail="Gmail service not initialized")

# Example endpoint for Google Calendar operations (conceptual)
@app.post("/calendar/create_event")
async def create_calendar_event(summary: str, description: str, start_time: str, end_time: str):
    if google_calendar_service:
        # Implement actual Google Calendar event creation logic here
        return {"status": "success", "message": f"Attempted to create event: {summary}"}
    raise HTTPException(status_code=500, detail="Google Calendar service not initialized")

# Example endpoint for Notion operations (conceptual)
@app.post("/notion/create_page")
async def create_notion_page(parent_page_id: str, title: str, content: str):
    if notion_client:
        # Implement actual Notion page creation logic here
        return {"status": "success", "message": f"Attempted to create Notion page: {title}"}
    raise HTTPException(status_code=500, detail="Notion service not initialized")

# Example endpoint for Zapier trigger (conceptual)
@app.post("/zapier/trigger")
async def trigger_zapier_webhook(event_name: str, payload: dict):
    if ZAPIER_WEBHOOK_URL:
        # Implement actual Zapier webhook trigger logic here
        # requests.post(ZAPIER_WEBHOOK_URL, json={"event": event_name, "payload": payload})
        return {"status": "success", "message": f"Attempted to trigger Zapier webhook for event: {event_name}"}
    raise HTTPException(status_code=500, detail="Zapier webhook URL not configured")

