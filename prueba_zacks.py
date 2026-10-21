from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page()
    r = page.goto("https://www.zacks.com/stock/quote/ADBE", wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    html = page.content()
    print("Codigo:", r.status)
    print("Largo:", len(html))
    print("Tiene rank_view:", "rank_view" in html)
    i = html.find('rank_view">')
    print(html[i:i + 150] if i != -1 else html[:300])
    b.close()
