#!/usr/bin/env python3
"""Switch the Sway site between "coming soon" and "live on the App Store".

    python3 scripts/store.py soon                       # the state before release (the default)
    python3 scripts/store.py live --app-id 1234567890   # once Sway is actually on the App Store
    python3 scripts/store.py live --app-id 1234567890 --price 3.99
    python3 scripts/store.py status                     # say which state the pages are in

It rewrites only the text between marker comments (<!-- name:start --> ... <!-- name:end -->)
in the HTML pages next to this folder. Everything else is edited by hand. It never commits
or pushes. Standard library only.
"""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted(ROOT.glob("*.html"))


def blocks(app_id, price):
    live = app_id is not None
    url = f"https://apps.apple.com/app/id{app_id}" if live else None
    return {
        "appmeta": f'<meta name="apple-itunes-app" content="app-id={app_id}">' if live else "",
        "store-cta": (f'<a class="btn" href="{url}">Download on the App Store</a>' if live
                      else '<span class="soon">Coming soon to the App Store</span>'),
        "store-note": "" if live else "In development, with no release date yet. ",
        "store-closing": ('<h2 id="closing-title">Hang the first piece.</h2>\n'
                          '    <p>Sway is on the App Store for iPhone.</p>' if live else
                          '<h2 id="closing-title">Coming to the App Store.</h2>\n'
                          '    <p>Sway is in development. There is no release date yet.</p>'),
        "store-release": (f'Out now on the <a href="{url}">App Store</a>' if live
                          else "In development. Coming to the App Store, with no release date yet."),
        "store-faq": ("\n<details><summary>Where do I get Sway?</summary><p>On the "
                      f'<a href="{url}">App Store</a>, for iPhone. One price, paid once, with no ads, '
                      "no in-app purchases and no account.</p></details>\n"
                      "<details><summary>How do I get a refund?</summary><p>Apple handles all payments and "
                      'refunds. Request one at <a href="https://reportaproblem.apple.com">'
                      "reportaproblem.apple.com</a>.</p></details>\n" if live else
                      "\n<details><summary>When does Sway come out?</summary><p>Sway is in development and "
                      "is coming to the App Store. There is no release date yet.</p></details>\n"
                      "<details><summary>What will it cost?</summary><p>One price, paid once. The planned "
                      "price is USD 3.99. There are no ads, no in-app purchases and no account.</p></details>\n"),
    }


def structured_data(text, app_id, price):
    """Add or remove downloadUrl and the offer in the JSON-LD block; the rest is kept as written."""
    m = re.search(r"(<!-- ld:start -->\n<script type=\"application/ld\+json\">\n)(.*?)(\n</script>\n<!-- ld:end -->)", text, re.S)
    if not m:
        return text
    data = json.loads(m.group(2))
    data.pop("downloadUrl", None)
    data.pop("offers", None)
    if app_id is not None:
        data["downloadUrl"] = f"https://apps.apple.com/app/id{app_id}"
        if price is not None:
            data["offers"] = {"@type": "Offer", "price": price, "priceCurrency": "USD"}
    return text[:m.start(2)] + json.dumps(data, indent=2) + text[m.end(2):]


def apply(app_id, price):
    new = blocks(app_id, price)
    for page in PAGES:
        text = before = page.read_text()
        for name, body in new.items():
            text = re.sub(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)",
                          lambda m: m.group(1) + body + m.group(2), text, flags=re.S)
        text = structured_data(text, app_id, price)
        if text != before:
            page.write_text(text)
            print("updated", page.name)


def status():
    text = (ROOT / "index.html").read_text()
    m = re.search(r"apps\.apple\.com/app/id(\d+)", text)
    print(f"live (App Store id {m.group(1)})" if m else "coming soon (no App Store link)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state", choices=["soon", "live", "status"])
    ap.add_argument("--app-id", help="the numeric App Store id, required for live")
    ap.add_argument("--price", help="the US price for the structured data, for example 3.99")
    a = ap.parse_args()
    if a.state == "status":
        return status()
    if a.state == "live":
        if not (a.app_id and a.app_id.isdigit()):
            sys.exit("live needs --app-id with the numeric App Store id")
        if a.price is not None and not re.fullmatch(r"\d+(\.\d\d)?", a.price):
            sys.exit("--price looks like 3.99")
        apply(a.app_id, a.price)
        print("Now edit by hand: the 'planned price' lines and the development-build notes (see README).")
    else:
        apply(None, None)
    status()


if __name__ == "__main__":
    main()
