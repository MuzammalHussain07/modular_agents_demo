from fastapi import FastAPI
from agents.dedup_agent import deduplicate_customers
from agents.marketing_mix_agent import optimize_marketing_mix

app = FastAPI(title="Modular AI Agents Demo")

@app.get("/")
def home():
    return {"message": "Welcome to Modular Agents Demo"}

@app.post("/dedup")
def run_dedup(customers: list[dict]):
    """
    Deduplicate customer records
    """
    return deduplicate_customers(customers)

@app.post("/marketing_mix")
def run_marketing(data: dict):
    """
    Optimize marketing budget allocation
    """
    return optimize_marketing_mix(data)
