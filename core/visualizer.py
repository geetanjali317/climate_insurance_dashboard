# core/visualizer.py


def define_ui_and_visual_elements(enriched_responses, references_dict):
    """
    Prepares a clean structure for the Streamlit UI to render.
    """
    visual_data = []
    for item in enriched_responses:
        visual_data.append(
            {
                "title": item["article"]["title"],
                "summary": item["article"]["summary"],
                "tags": item["article"]["tags"],
                "related_papers": item["related_papers"],
            }
        )
    return visual_data
