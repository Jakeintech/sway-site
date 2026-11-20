# sway-site

Public website for **Sway**, a game for iPhone about building a hanging mobile.
*Build a hanging mobile. Every piece tips everything above it.*

Sway is in development, so the site says "Coming soon to the App Store" and has no App Store link. The switch for launch day is described under [Store live](#store-live).

Not published yet. The pages assume the same home as the other sites, <https://jakeintech.github.io/sway-site/> (GitHub Pages, from `main` /). That address is in each page's `canonical`, `og:url` and `og:image` tags and in the JSON-LD on the home page; if the site goes somewhere else, replace it everywhere (`grep -rl jakeintech.github.io/sway-site .`).

| Page | URL |
|---|---|
| Home (App Store marketing URL) | `/` |
| Press kit | `/press.html` |
| Support and FAQ (App Store support URL) | `/support.html` |
| Privacy Policy (App Store privacy URL) | `/privacy-policy.html` |
| Terms of Use | `/terms-of-service.html` |

Once App Store Connect points at the support, privacy and marketing URLs, keep them exactly as they are.

## How it is built

Plain HTML and one stylesheet (`assets/site.css`). No build step, no JavaScript, and no third-party requests of any kind: fonts, images and the video are served from this repo, and there are no analytics, cookies or CDNs. The structure and the legal pages follow `nightsignal-site` and `snowline-site`. The look is Sway's own.

- **Look:** the Sway Design System, the same tokens as `SwayApp/Sources/Theme/Theme.swift` in the game repo. Warm paper, fine black wire, flat painted shapes. No gradients, no blur, no gloss, no emoji. The only shadow is a flat offset copy (6px 10px 0, ink at 8%; deeper at night, as on the app icon). Radius 10 / 18 / 24 / pill.
- **Colour:** Paper theme: paper `#F3EDE1`, paper-2 `#E9E1D2`, card `#F6F1E7`, ink `#1B1A17`, muted `#625C52`, hairline `#CDBFA5`, red `#D2412E`, blue `#2356A8`, yellow `#E8B436`, brass `#B98B3E`. Night gallery (through `prefers-color-scheme`): paper `#1A1816`, paper-2 `#262320`, card `#302C28`, ink `#F3EDE1`, muted `#B8AFA1`, hairline `#4A443D`, red `#E2553F`, blue `#4C7FD1`, yellow `#F0C24E`, brass `#D2A65A`. Text is only ever ink or muted; the piece colours are fills. Every text pairing meets WCAG AA (the lowest is muted on paper-2 at 5.1:1).
- **Type:** DM Serif Display for the name and big headings, DM Sans (400, 600, 700) for everything else. The four TTFs are copied unchanged from `SwayApp/Resources/Fonts/` into `assets/fonts/`, with their SIL Open Font License texts beside them.
- **Hero:** an inline SVG of the design system's cover mobile, hung from the header's bottom rule. Each rod turns about its pivot with a CSS animation and the strings stay plumb. It is still under `prefers-reduced-motion`.
- **Buttons:** pills at least 44px tall. Primary is ink with paper text, secondary is a 1.5px hairline outline. The "Coming soon" pill is a status, not a link.
- **Accessibility:** skip link, landmarks, one `h1` per page, alt text that says what each capture shows, 44px targets, visible focus rings, AA contrast in both themes. Mobile first: 16px gutters and no sideways scroll at 390px.
- **Voice:** short, plain and warm, like a gallery placard. Second person, present tense. Numbers carry a label. No exclamation marks.
- **Honesty:** every claim comes from the game's spec or can be seen in a capture. The captures are real, from the practice mode of a development build, and are captioned that way. No release date, ratings, awards or quotes.

## Where the files come from

Nothing here is generated on publish. These were made once by hand from the game repo (`~/Developer/GitHub/Sway`); remake them when the sources change.

| File here | Source in the Sway repo |
|---|---|
| `assets/fonts/*.ttf` | `SwayApp/Resources/Fonts/` (copied unchanged) |
| `assets/img/favicon.png` (64), `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png`, `assets/press/sway-icon-{1024,512}.png` | `SwayApp/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon.png`, resized with `sips` |
| `assets/img/icon-192-dark.png`, `assets/press/sway-icon-dark-1024.png` | the same folder's `AppIcon-Dark.png` |
| `assets/img/shots/01-merge.png`, `03-level.png` (600 x 1221) | `captures/raw/m1-b.png`, `m1-c.png`: the empty status area at the top cropped off, then resized |
| `assets/img/shots/02-ghost.png` | the frame at 19.3 s of `captures/m2-merge-catch-gust-score.mp4`, cropped the same way |
| `assets/video/sway-play-30s.mp4` | `captures/m2-merge-catch-gust-score.mp4`, remuxed for progressive playback (`ffmpeg -c copy -movflags +faststart`), no re-encode, no audio track |
| `assets/video/sway-play-30s-poster.png` | the frame at 25.0 s of the same recording |
| `assets/press/sway-capture-*.png` | the same three captures at full size, uncropped |
| `assets/img/og.png` (1200 x 630) | drawn from the design system's cover geometry and the two typefaces |

## Store live

The site has two states. Which one it is in is decided by the text between marker comments in the pages, and `scripts/store.py` rewrites that text. It uses only the Python standard library, changes nothing outside the markers, and never commits or pushes.

```bash
python3 scripts/store.py status                      # coming soon, or live with which App Store id
python3 scripts/store.py live --app-id 1234567890 --price 3.99
python3 scripts/store.py soon                        # back to coming soon
```

| Marker | Page | Coming soon | Live |
|---|---|---|---|
| `<!-- appmeta -->` | every page | empty | `<meta name="apple-itunes-app" content="app-id=...">` (the Smart App Banner) |
| `<!-- store-cta -->` | index (twice) | "Coming soon to the App Store", a status pill with no link | "Download on the App Store", a primary button linking to `apps.apple.com/app/id...` |
| `<!-- store-note -->` | index | "In development, with no release date yet." | empty |
| `<!-- store-closing -->` | index | "Coming to the App Store." | "Hang the first piece." |
| `<!-- store-release -->` | press | "In development. Coming to the App Store, with no release date yet." | "Out now on the App Store" with the link |
| `<!-- store-faq -->` | support | "When does Sway come out?" and "What will it cost?" | "Where do I get Sway?" and "How do I get a refund?" |
| `<!-- ld -->` | index | JSON-LD `VideoGame` | the same, plus `downloadUrl` and, with `--price`, the offer |

The App Store id exists as soon as the App Store Connect record does, long before release. Run `live` only once Sway is actually on the App Store.

### Launch day, by hand

The script does not touch these. Search for them and edit:

- "The planned price is USD 3.99" (index, and in `scripts/store.py` for the coming-soon FAQ) and "Planned at USD 3.99" (press): state the real price.
- "Captured from a development build" (index) and the Captures note (press): replace the captures and the wording once there are captures of the shipping game.
- "It is in development" (press lede, privacy policy section 1) and "Sway is not on the App Store yet" (privacy policy section 13): state the App Store privacy label as it was actually declared.
- The "Last updated" dates on the privacy policy and the terms.

## First publish

This folder is a git repository with no commits and no remote. To publish: read every page, commit, create the GitHub repository, add it as `origin`, push `main`, and turn on GitHub Pages from `main` / (root). Then check that the URLs in the table at the top load.

## Contact

info@jakeawilliams.com
