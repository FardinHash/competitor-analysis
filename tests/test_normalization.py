from src.utils.normalization import normalize_data

def test_normalization_with_gemma2():
    raw_data = {
        "google": {"google_summary": "Leading AI research organization."},
        "wikipedia": {"wikipedia_summary": "OpenAI specializes in AI and machine learning."},
        "linkedin": {"linkedin_summary": "Pioneering advancements in AI for ethical applications."}
    }
    normalized = normalize_data(raw_data)

    assert "google_summary" in normalized
    assert "wikipedia_summary" in normalized
    assert "linkedin_summary" in normalized
    assert normalized["google_summary"] == "Leading AI research organization."
    assert normalized["wikipedia_summary"] == "OpenAI specializes in AI and machine learning."
    assert normalized["linkedin_summary"] == "Pioneering advancements in AI for ethical applications."
