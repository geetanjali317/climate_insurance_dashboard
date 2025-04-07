# core/correlation.py

# Sample mockup research data — in real-world use, you'd fetch this via arXiv or LangChain
research_papers = [
    {
        "title": "Managing Basis Risks in Weather Parametric Insurance",
        "authors": "Hang Gao, Shuohua Yang, Xinli Liu",
        "date": "2024-09-25",
        "abstract": "Monte Carlo simulations show that portfolio diversification reduces basis risk in weather parametric insurance.",
        "tags": ["basis risk", "parametric", "climate"],
    },
    {
        "title": "Data-driven Parametric Insurance Framework Using Bayesian Neural Networks",
        "authors": "Subeen Pang, Chanyeol Choi",
        "date": "2022-09-22",
        "abstract": "This work employs Bayesian neural networks to improve risk prediction for parametric insurance.",
        "tags": ["parametric", "risk", "insurance", "climate"],
    },
    {
        "title": "Climate Risk and Insurance Pricing Models",
        "authors": "Emily Reed, Omar Patel",
        "date": "2023-05-10",
        "abstract": "Analyzes how climate trends influence insurance premium pricing using econometric modeling.",
        "tags": ["insurance", "climate", "pricing", "policy"],
    },
]


def find_research_references_correlating_with_each_news_snnipets(news_snippets):
    """
    Matches each news item with related research papers based on overlapping tags.
    """
    correlated = []
    for article in news_snippets:
        related_papers = []
        for paper in research_papers:
            if set(article["tags"]) & set(paper["tags"]):
                related_papers.append(paper)
        correlated.append({"article": article, "related_papers": related_papers})
    return correlated, research_papers
