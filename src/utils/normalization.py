def normalize_data(raw_data):
    """
    Normalize and consolidate data from multiple sources.
    """
    normalized_data = {}

    google_data = raw_data.get("google", {})
    if "error" not in google_data:
        normalized_data["google_summary"] = google_data.get("google_results", [])
    else:
        normalized_data["google_summary"] = google_data.get("error")

    wikipedia_data = raw_data.get("wikipedia", {})
    if "error" not in wikipedia_data:
        normalized_data["wikipedia_summary"] = wikipedia_data.get("extract", "No summary available")
    else:
        normalized_data["wikipedia_summary"] = wikipedia_data.get("error")

    return normalized_data
