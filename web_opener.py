import webbrowser

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "chatgpt": "https://chat.openai.com",
    "twitter": "https://twitter.com",
    "snapchat": "https://www.snapchat.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "quora": "https://www.quora.com",
    "reddit": "https://www.reddit.com",
    "pinterest": "https://www.pinterest.com",
    "wikipedia": "https://www.wikipedia.org",
}

def open_website(site_name):
    """
    Open a website in the default browser.
    """
    site_name = site_name.lower()
    if site_name in WEBSITES:
        webbrowser.open(WEBSITES[site_name])
        print(f"Opening {site_name}...")
    else:
        print("Website not found in the supported list.")
