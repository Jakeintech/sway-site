#!/usr/bin/env python3
"""Write the Sway site pages. Edit the copy here, run `python3 scripts/build.py`, read the pages, commit.
Every claim must be true of the build on the App Store (repo ~/Developer/GitHub/Sway, appstore/listing.json).
Never state a price: the App Store shows it in the reader's own currency."""
import pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://jakeintech.github.io/sway-site/"
STORE = "https://apps.apple.com/app/id6837027785"
UPDATED = "November 25, 2026"


def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F3EDE1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1A1816" media="(prefers-color-scheme: dark)">
<meta name="apple-itunes-app" content="app-id=6837027785">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sway">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sway. Get the birds to bed before the branch tips. A balance game for iPhone.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}assets/img/og.png">
<link rel="preload" href="assets/fonts/DMSerifDisplay-Regular.ttf" as="font" type="font/ttf" crossorigin>
<link rel="preload" href="assets/fonts/DMSans-Regular.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="./" aria-label="Sway home">
      <picture><source srcset="assets/img/icon-192-dark.png" media="(prefers-color-scheme: dark)"><img src="assets/img/icon-192.png" alt="" width="32" height="32"></picture>
      Sway
    </a>
    <nav class="site-nav" aria-label="Site">
      <a href="./#how">How it plays</a>
      <a href="press.html">Press</a>
      <a href="support.html">Support</a>
    </nav>
  </div>
</header>
"""


FOOT = """<footer class="site-foot">
  <div class="wrap">
    <nav aria-label="Footer">
      <a href="./">Home</a>
      <a href="press.html">Press kit</a>
      <a href="support.html">Support</a>
      <a href="privacy-policy.html">Privacy Policy</a>
      <a href="terms-of-service.html">Terms of Use</a>
      <a href="mailto:info@jakeawilliams.com">Contact</a>
    </nav>
    <p>Type set in DM Serif Display and DM Sans, under the SIL Open Font License (<a href="assets/fonts/OFL-DMSerifDisplay.txt">DM Serif Display licence</a>, <a href="assets/fonts/OFL-DMSans.txt">DM Sans licence</a>).</p>
    <p>&copy; 2026 Jake Williams. Apple, iPhone and App Store are trademarks of Apple Inc., registered in the U.S. and other countries.</p>
  </div>
</footer>
</body>
</html>
"""

SHOTS = [
    ("01-hero", "Night 4 of 7", "Eight birds on a hanging branch at dusk",
     "Sway in play on night 4 of 7: eight round birds sit on a tilted hanging branch at dusk, an owl at the high end, three more birds wait below, and a pill reads One more is worth +15. Risk it? above a Goodnight button."),
    ("02-risk", "Bank it, or risk one more", "Goodnight banks the night. One more bird is worth more.",
     "Sway in play on night 3: seven birds on a branch, two owls waiting below, and the hint One more is worth +8. Risk it?"),
    ("04-birdbook", "The Birdbook", "Twelve birds, each with its own habit",
     "The Birdbook screen listing the birds met so far, each with a short note about how it behaves."),
    ("06-daily", "Today's Daily", "Same birds, same branch, for everyone",
     "The Daily: the same birds and the same branch for every player, once a day."),
]


def shot_li(n, eyebrow, title, alt):
    return f"""      <li><figure>
        <img src="assets/img/shots/{n}.jpg" width="600" height="1304" loading="lazy" alt="{html.escape(alt)}">
        <figcaption class="placard"><p class="eyebrow">{eyebrow}</p><b>{title}</b></figcaption>
      </figure></li>"""


def faq(q, a):
    return f"<details><summary>{q}</summary><p>{a}</p></details>"


INDEX = head("Sway: Bird Puzzle. A balance game for iPhone.",
             "Sway is a balance game for iPhone: perch the birds on a hanging branch and get them to bed before it tips. All of Spring is free. No ads, no subscription.", "") + f"""<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <p class="eyebrow">A balance game for iPhone</p>
      <h1 id="hero-title">Sway</h1>
      <p class="tagline">Get the birds to bed before the branch tips.</p>
      <p class="lede">Birds arrive one at a time. Drag each one onto a hanging branch and let go. Past 24 degrees they start to slip.</p>
      <div class="cta">
        <a class="btn" href="{STORE}">Download on the App Store</a>
        <a class="btn ghost" href="#how">See how it plays</a>
      </div>
      <p class="fine">Free to download. iPhone, iOS 18 or later.</p>
    </div>
    <figure class="hero-art">
      <img src="assets/img/shots/01-hero.jpg" width="300" height="652" alt="{html.escape(SHOTS[0][3])}">
    </figure>
  </div>
</section>
<section class="section" id="how" aria-labelledby="how-title">
  <div class="wrap">
    <p class="eyebrow">How it plays</p>
    <h2 id="how-title">Take the safe night, or push it.</h2>
    <dl class="catalogue">
      <div><dt>Perch</dt><dd>Drag a bird onto a branch. A ghost shows where it will land and how far the branch will lean before you commit.</dd></div>
      <div><dt>Slip</dt><dd>Past 24 degrees birds start to slip. A lower branch catches them if you left room; otherwise they fly off into the dark.</dd></div>
      <div><dt>Goodnight</dt><dd>Once the night's quota is home, Goodnight banks it. Every bird past the quota is worth more than the last.</dd></div>
      <div><dt>Seven nights</dt><dd>A run is seven nights and three hearts. A night with nobody lost gives a heart back. Wind comes after every third bird.</dd></div>
      <div><dt>Twelve birds</dt><dd>The Dove calms its neighbours. The Pigeon never settles. The Puffin grips hardest. The Hummingbird weighs almost nothing.</dd></div>
      <div><dt>The Daily</dt><dd>The same birds and the same branch for every player, once a day, one try.</dd></div>
    </dl>
  </div>
</section>
<section class="section" id="play" aria-labelledby="play-title">
  <div class="wrap">
    <p class="eyebrow">In play</p>
    <h2 id="play-title">Captured from the App Store build.</h2>
    <ul class="wall">
{chr(10).join(shot_li(*s) for s in SHOTS[1:])}
    </ul>
  </div>
</section>
<section class="section" id="price" aria-labelledby="price-title">
  <div class="wrap">
    <p class="eyebrow">What it costs</p>
    <h2 id="price-title">Spring is free. All of it.</h2>
    <div class="split">
      <div class="panel">
        <h3>Free</h3>
        <ul><li>All seven nights of Spring, as often as you like</li><li>Every Daily</li><li>The whole Birdbook</li><li>No ads, no subscription, no account</li></ul>
      </div>
      <div class="panel">
        <h3>The Full Flock, one optional purchase</h3>
        <ul><li>Summer, Autumn and Winter, each one windier</li><li>The last two bring an extra bird every night</li><li>Pay once, shared with Family Sharing</li><li>Offered once, after you win Spring, never mid-play</li></ul>
      </div>
    </div>
  </div>
</section>
<section class="section closing" aria-labelledby="closing-title">
  <div class="wrap">
    <h2 id="closing-title">Tuck the flock in.</h2>
    <p>Sway is on the App Store for iPhone.</p>
    <div class="cta"><a class="btn" href="{STORE}">Download on the App Store</a></div>
  </div>
</section>
</main>
""" + FOOT

SUPPORT = head("Sway support", "Help with Sway, a balance game for iPhone: how it plays, the optional purchase, where your progress is saved, and how to get in touch.", "support.html") + f"""<main id="main" class="doc">
<h1>Support</h1>
<p class="updated">Help with Sway</p>
<div class="contact-card">
<h2>Get in touch</h2>
<p>Email <a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a>. It helps to include your iPhone model, your iOS version, what you were doing and what you expected to happen. A screenshot is welcome. A person reads every message.</p>
<div class="cta"><a class="btn" href="mailto:info@jakeawilliams.com?subject=Sway%20support">Email support</a></div>
</div>
<h2>Playing</h2>
<div class="faq">
{faq("How do I perch a bird?", "Drag up from anywhere and move the bird over a branch. A ghost shows where it will land and how far the branch will lean. Let go to perch it. A quick tap does nothing, so a stray touch never drops a bird.")}
{faq("Why did my bird slip?", "Past 24 degrees of lean, birds start to slip. A slipping bird is caught by a lower branch if one has room; otherwise it flies off and costs a heart.")}
{faq("When should I say Goodnight?", "Goodnight lights up once the night's quota is home and banks the night. Every bird past the quota is worth more than the last, so you can push on, but a bird lost costs a heart.")}
{faq("How do hearts work?", "A run has three hearts across seven nights. A night where no bird is lost gives a heart back.")}
{faq("What is the Daily?", "The same birds and the same branch for every player, once a day, with one try.")}
{faq("Can I play with VoiceOver?", "Yes. Each branch offers its spots as actions that say what the tilt would be, so you can choose where to perch by ear. Sway also follows Reduce Motion and Dynamic Type.")}
</div>
<h2>The Full Flock</h2>
<div class="faq">
{faq("What is free?", "All seven nights of Spring, replayable as often as you like, every Daily and the whole Birdbook. No ads and no subscription.")}
{faq("What does The Full Flock add?", "Summer, Autumn and Winter. Each is windier, and the last two bring an extra bird every night. It is one payment, and Family Sharing is supported. The price is shown in the App Store in your own currency.")}
{faq("How do I restore it on a new iPhone?", "Settings (the gear on the title screen) &gt; Restore Purchases, signed in with the Apple Account that bought it.")}
{faq("How do I get a refund?", "Refunds are handled by Apple at reportaproblem.apple.com.")}
</div>
<h2>Your data</h2>
<div class="faq">
{faq("Where is my progress saved?", "On your iPhone only. Sway has no account and no server, so there is no copy anywhere else, and deleting the app deletes your progress.")}
{faq("What happens when I share a clip?", "Sway hands the clip to the iOS share sheet and you choose where it goes. Nothing is sent unless you choose to share.")}
</div>
</main>
""" + FOOT

PRIVACY = head("Sway privacy policy", "Sway collects no personal data. No account, no ads, no analytics and no tracking. Your progress and settings stay on your iPhone.", "privacy-policy.html") + f"""<main id="main" class="doc">
<h1>Privacy Policy</h1>
<p class="updated">Last updated {UPDATED}</p>
<div class="summary">
<h2>The short version.</h2>
<ul>
<li>Sway collects no personal data.</li>
<li>No account, no ads, no analytics and no tracking.</li>
<li>Your game progress and settings are saved on your iPhone only.</li>
<li>The one optional purchase, The Full Flock, is handled entirely by Apple.</li>
<li>Sharing a clip uses the iOS share sheet. Nothing is sent unless you choose to share.</li>
</ul>
</div>
<h2>1. Who we are</h2>
<p>Sway is a game for iPhone made by Jake Williams ("we", "us"). This policy explains what information the game handles, where it goes and the choices you have. It covers TestFlight builds as well as the App Store version. Questions: <a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a>.</p>
<h2>2. What the game handles</h2>
<div class="table-wrap"><table>
<tr><th>Information</th><th>What it is used for</th><th>Where it goes</th></tr>
<tr><td>Game progress, best scores, the Birdbook and settings</td><td>Letting you continue and remembering your preferences.</td><td>Saved on your iPhone only. Never sent to us or anyone else.</td></tr>
<tr><td>The Full Flock purchase</td><td>Unlocking Summer, Autumn and Winter.</td><td>Handled by Apple through the App Store. Sway checks Apple's signed record on your iPhone. We do not see your name, payment details or purchase history.</td></tr>
<tr><td>A shared clip</td><td>Sharing the last few seconds of play, when you choose to.</td><td>Passed to the iOS share sheet, then only to the app or person you pick.</td></tr>
<tr><td>Crash reports</td><td>Fixing bugs.</td><td>Sway sends none itself. If you have chosen to share analytics with app developers in iOS Settings, Apple may share crash reports with us that do not identify you. For TestFlight builds, Apple may share crash data and feedback you send.</td></tr>
</table></div>
<h2>3. No server of its own</h2>
<p>Sway has no server and no backend, and contains no advertising, analytics or tracking software. It works offline.</p>
<h2>4. Tracking and permissions</h2>
<p>Sway does not track you across other companies' apps and websites, so it never shows the App Tracking Transparency prompt. It does not use your location, camera, microphone, contacts or photo library. If you save a shared clip to Photos from the share sheet, iOS may ask whether Sway may add it.</p>
<h2>5. What we do not do</h2>
<ul><li>No accounts or sign-in of our own.</li><li>No advertising, and no advertising identifier.</li><li>No analytics and no tracking.</li><li>No sale or sharing of personal information.</li></ul>
<h2>6. Keeping and deleting your data</h2>
<p>Your progress and settings stay on your iPhone until you delete the game, which removes everything Sway stored. Because we hold none of your data, there is nothing for us to delete on our side. Your purchase stays with your Apple Account and can be restored.</p>
<h2>7. Children</h2>
<p>Sway collects no personal information from anyone, including children. Purchases can be restricted by a parent with Screen Time and Ask to Buy. If you believe a child has sent us personal information by email, contact us and we will delete it.</p>
<h2>8. Your rights</h2>
<p>Depending on where you live, laws such as the GDPR or the CCPA give you rights to access, correct, delete or restrict the use of your personal data. Sway keeps your data on your own iPhone, so you can exercise these rights directly by deleting the game. If you have a request we can help with, write to <a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a>.</p>
<h2>9. This website</h2>
<p>This site is hosted by GitHub Pages. It sets no cookies and uses no analytics, tracking or third-party resources; its fonts and images are served from the site itself. GitHub may keep standard server logs, such as IP addresses, under the GitHub Privacy Statement.</p>
<h2>10. App Store privacy label</h2>
<p>Sway's App Store privacy label is "Data Not Collected", matching this policy. If you ever find the two disagree, tell us and we will correct it.</p>
<h2>11. Changes</h2>
<p>If this policy changes, we will update the date at the top of this page.</p>
<h2>12. Contact</h2>
<p>Jake Williams, <a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a></p>
</main>
""" + FOOT

TERMS = head("Sway terms of use", "The terms for playing Sway, a balance game for iPhone.", "terms-of-service.html") + f"""<main id="main" class="doc">
<h1>Terms of Use</h1>
<p class="updated">Last updated {UPDATED}</p>
<h2>1. These terms</h2>
<p>These terms cover Sway, a game for iPhone made by Jake Williams ("we", "us"). By playing Sway you agree to them. Apple's Licensed Application End User License Agreement also applies.</p>
<h2>2. The game</h2>
<p>Sway is a single-player game. You perch birds on a hanging branch across runs of seven nights, with a Daily and a Birdbook. It has no account of its own and works offline.</p>
<h2>3. Price and the optional purchase</h2>
<p>Sway is free to download. All of Spring, every Daily and the Birdbook are free. One optional in-app purchase, The Full Flock, unlocks Summer, Autumn and Winter; it is a one-time purchase, not a subscription. There are no ads. Payment and refunds are handled by Apple under its own terms; you can request a refund at reportaproblem.apple.com.</p>
<h2>4. Your use</h2>
<p>You may play Sway for your own, non-commercial use. Please do not reverse-engineer it, or use it to break the law.</p>
<h2>5. Ownership</h2>
<p>The game, its design, artwork, sound, text and code belong to us and are protected by law. Screenshots and clips you capture of your own play are yours to share. Press and creators are welcome to use the materials in the press kit.</p>
<h2>6. Changes and availability</h2>
<p>We may update Sway, add or change features, or stop offering it. Updates may be required to keep playing. Anything you have bought stays tied to your Apple Account.</p>
<h2>7. No warranty</h2>
<p>Sway is provided "as is". To the fullest extent the law allows, we make no warranties beyond those that cannot be excluded.</p>
<h2>8. Liability</h2>
<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special, consequential or punitive damages, or for lost profits, data or goodwill, arising from your use of Sway. Our total liability for any claim will not exceed what you paid for it.</p>
<h2>9. Governing law</h2>
<p>These terms are governed by the laws of the place where the developer lives, without regard to conflict-of-law rules, unless consumer law where you live gives you the right to bring a claim locally.</p>
<h2>10. Apple</h2>
<p>These terms are between you and us, not Apple. Apple is not responsible for Sway or its content and has no obligation to provide maintenance or support for it; we are. If Sway fails to conform to any applicable warranty, you may notify Apple and Apple will refund the purchase price of any in-app purchase; Apple has no other warranty obligation. We, not Apple, are responsible for any claims relating to Sway, including product liability, legal or regulatory compliance and intellectual property claims. You confirm that you are not in a country subject to a U.S. Government embargo and not on any U.S. Government list of prohibited or restricted parties. Apple and its subsidiaries are third-party beneficiaries of these terms and may enforce them against you.</p>
<h2>11. Contact</h2>
<p><a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a></p>
</main>
""" + FOOT

PRESS = head("Sway press kit", "Facts, descriptions, the app icon and captures of Sway, a balance game for iPhone.", "press.html") + f"""<main id="main" class="doc">
<h1>Press kit</h1>
<p class="lede">Sway is a balance game for iPhone: get the birds to bed before the branch tips. Everything on this page is yours to use when writing about the game.</p>
<h2>Facts</h2>
<dl class="facts">
  <div><dt>Name</dt><dd>Sway</dd></div>
  <div><dt>Developer</dt><dd>Jake Williams, solo</dd></div>
  <div><dt>Platform</dt><dd>iPhone, iOS 18 or later</dd></div>
  <div><dt>Released</dt><dd>November 24, 2026</dd></div>
  <div><dt>Price</dt><dd>Free to download, with all of Spring free. One optional purchase, The Full Flock, adds Summer, Autumn and Winter. No ads, no subscription.</dd></div>
  <div><dt>App Store</dt><dd><a href="{STORE}">{STORE}</a></dd></div>
  <div><dt>Contact</dt><dd><a href="mailto:info@jakeawilliams.com">info@jakeawilliams.com</a></dd></div>
</dl>
<h2>Short description</h2>
<p>Get the birds to bed before the branch tips.</p>
<h2>Long description</h2>
<p>Birds arrive one at a time and you perch each one on a hanging branch. A ghost shows where it will land and how far the branch will lean. Past 24 degrees they slip; a lower branch can catch them, or they fly off into the dark.</p>
<p>Once the night's quota is home, Goodnight banks it, and every bird past the quota is worth more than the last. A run is seven nights and three hearts. Twelve birds each behave differently, and they fill the Birdbook as you meet them. A Daily gives every player the same birds and the same branch once a day.</p>
<h2>Icon</h2>
<p><a href="assets/press/sway-icon-1024.png">Icon, 1024 px</a> · <a href="assets/press/sway-icon-dark-1024.png">Dark icon, 1024 px</a></p>
<h2>Captures</h2>
<ul class="wall">
{chr(10).join(shot_li(*s) for s in SHOTS)}
</ul>
</main>
""" + FOOT

for name, text in [("index.html", INDEX), ("support.html", SUPPORT), ("privacy-policy.html", PRIVACY),
                   ("terms-of-service.html", TERMS), ("press.html", PRESS)]:
    (ROOT / name).write_text(text)
    print("wrote", name)
