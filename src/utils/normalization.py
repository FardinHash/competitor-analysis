def normalize_data(raw_data):
    """
    Normalize and consolidate data from multiple sources.
    """
    normalized_data = {}

    google_data = raw_data.get("google", {})
    if "error" not in google_data:
        normalized_data["google_summary"] = google_data.get("google_summary", [])
    else:
        normalized_data["google_summary"] = google_data.get("error")

    wikipedia_data = raw_data.get("wikipedia", {})
    if "error" not in wikipedia_data:
        normalized_data["wikipedia_summary"] = wikipedia_data.get("wikipedia_summary", "No summary available")
    else:
        normalized_data["wikipedia_summary"] = wikipedia_data.get("error")

    linkedin_data = raw_data.get("linkedin", {})
    if "error" not in linkedin_data:
        normalized_data["linkedin_summary"] = linkedin_data.get("linkedin_summary", "No data available")
    else:
        normalized_data["linkedin_summary"] = linkedin_data.get("error")

    return normalized_data
