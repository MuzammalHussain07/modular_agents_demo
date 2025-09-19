import openai

openai.api_key = "YOUR_API_KEY"  # replace with your key

def optimize_marketing_mix(data: dict):
    """
    Example input:
    {
      "spend": {"google_ads": 5000, "facebook": 3000, "email": 2000},
      "roi": {"google_ads": 1.5, "facebook": 1.2, "email": 2.0}
    }
    """
    spend = data.get("spend", {})
    roi = data.get("roi", {})

    # Simple rule-based optimization
    recommendations = {
        ch: round(spend[ch] * roi.get(ch, 1.0), 2)
        for ch in spend
    }

    return {
        "input": data,
        "recommended_allocation": recommendations,
        "note": "This is a simple demo. A real version can use ML/LLM optimization."
    }
