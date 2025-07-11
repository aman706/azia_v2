from duckduckgo_search import DDGS
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=3)
            if not results:
                return "I couldn’t find anything useful, but I’ll keep learning from you."

            summary = ""
            for i, result in enumerate(results):
                title = result.get("title", "No title")
                snippet = result.get("body", "No description")
                summary += f"{title} — {snippet}\n"

            return f"Here’s what I found:\n{summary.strip()}"

    except Exception as e:
        print(f"[Search Error] {e}")
        return "I tried searching, but something went wrong. Maybe I need a break?"
