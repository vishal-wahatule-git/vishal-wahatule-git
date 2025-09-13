import requests
from bs4 import BeautifulSoup
import re

HACKERRANK_USER = "Vishal_Wahatule"
GFG_USER = "vishalwahatulegfg"

def fetch_hackerrank_problems():
    url = f"https://www.hackerrank.com/rest/hackers/{HACKERRANK_USER}/profile"
    try:
        res = requests.get(url, timeout=10).json()
        return res.get("model", {}).get("solved_challenges", 0)
    except:
        return 0

def fetch_gfg_problems():
    url = f"https://auth.geeksforgeeks.org/user/{GFG_USER}/practice/"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        solved_text = soup.find("div", {"class": "scoreCard_head__title"})
        if solved_text:
            numbers = re.findall(r"\d+", solved_text.text)
            return int(numbers[0]) if numbers else 0
        return 0
    except:
        return 0

def update_readme(hackerrank_count, gfg_count):
    with open("README.md", "r") as f:
        content = f.read()

    new_table = f"""| Topic                     | Solved Today | Total Solved |
|----------------------------|--------------|--------------|
| Core Java                 | 0            | 0            |
| Spring Boot + Hibernate   | 0            | 0            |
| Microservices             | 0            | 0            |
| **HackerRank**            | {hackerrank_count}            | {hackerrank_count}            |
| **GeeksforGeeks (GFG)**   | {gfg_count}            | {gfg_count}            |"""

    import re
    updated = re.sub(r"\| Topic.*?\| GeeksforGeeks.*?\|", new_table, content, flags=re.S)

    with open("README.md", "w") as f:
        f.write(updated)

if __name__ == "__main__":
    hackerrank_count = fetch_hackerrank_problems()
    gfg_count = fetch_gfg_problems()
    update_readme(hackerrank_count, gfg_count)
