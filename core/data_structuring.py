# core/data_structuring.py


def structure_the_response(response):
    """
    Convert raw Tavily search response into a structured format for visualization.

    Parameters:
    - response: raw output from TavilySearchResults tool

    Returns:
    - structured_news: List[Dict] containing title, source, date, summary, and tags
    """

    # Debug output (can be removed in production)
    print("DEBUG: Raw response type:", type(response))
    print("DEBUG: Raw response content:", response)

    # Step 1: Handle different response formats
    if isinstance(response, dict):
        results = response.get("results", [])
    elif isinstance(response, list):
        results = response
    else:
        raise ValueError(f"Unexpected response type: {type(response)}")

    structured_news = []

    # Step 2: Extract and normalize fields
    for item in results:
        structured_news.append(
            {
                "title": item.get("title", "Untitled"),
                "source": item.get("source", "Unknown"),
                "date": item.get("published_date", "Unknown"),
                "summary": item.get("content", "No summary available."),
                "tags": extract_tags(item),  # You can customize tag logic here
            }
        )

    return structured_news


def extract_tags(item):
    """
    Placeholder tag extractor – you can improve this using NLP (e.g., keyword extraction).
    For now, it uses simple keyword heuristics.
    """
    tags = []
    content = (item.get("title", "") + " " + item.get("content", "")).lower()

    keyword_map = {
        "parametric": "parametric insurance",
        "basis risk": "basis risk",
        "climate": "climate change",
        "disaster": "disaster insurance",
        "insurance": "insurance",
        "premium": "insurance pricing",
        "flood": "natural disaster",
        "wildfire": "natural disaster",
    }

    for keyword, tag in keyword_map.items():
        if keyword in content:
            tags.append(tag)

    return list(set(tags))  # remove duplicates
