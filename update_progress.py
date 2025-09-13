import requests
from bs4 import BeautifulSoup

# === HackerRank ===
HACKERRANK_USERNAME = "Vishal_Wahatule"
hr_url = f"https://www.hackerrank.com/rest/hackers/{HACKERRANK_USERNAME}/recent_challenges"

try:
    hr_data = requests.get(hr_url).json()
    hr_solved = len(hr_data.get("models", []))
    hr_total = 100  # You can set your target total questions here
except Exception as e:
    print("HackerRank fetch error:", e)
    hr_solved = 0
    hr_total = 0

# === GeeksforGeeks ===
GFG_USERNAME = "vishalwahatulegfg"
gfg_url = f"https://practice.geeksforgeeks.org/user/{GFG_USERNAME}/"
try:
    page = requests.get(gfg_url)
    soup = BeautifulSoup(page.content, "html.parser")
    # Extract solved count (example assumes GFG shows total solved in a span with class 'score-card')
    gfg_solved_tag = soup.find("div", class_="score-card")
    gfg_solved = int(gfg_solved_tag.text.strip()) if gfg_solved_tag else 0
    gfg_total = 500  # Set your total target questions
except Exception as e:
    print("GFG fetch error:", e)
    gfg_solved = 0
    gfg_total = 0

# === Update README.md ===
with open("README.md", "r") as file:
    content = file.read()

content = content.replace("{{HACKERRANK_SOLVED}}", str(hr_solved))
content = content.replace("{{HACKERRANK_TOTAL}}", str(hr_total))
content = content.replace("{{GFG_SOLVED}}", str(gfg_solved))
content = content.replace("{{GFG_TOTAL}}", str(gfg_total))

with open("README.md", "w") as file:
    file.write(content)

print("README.md updated successfully!")
