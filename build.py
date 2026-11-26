"""Static page builder for the O.J. Ekoja & Co. website.

Every page shares one header, footer and set of templates, defined here.
Edit content below, then run:   python build.py
The generated .html files are committed, so the site works on any static host (e.g. GitHub Pages).
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent

FIRM = "O.J. Ekoja &amp; Co."
PHONE_1, PHONE_1_TEL = "+234 816 919 8384", "+2348169198384"
PHONE_2, PHONE_2_TEL = "+234 705 030 8648", "+2347050308648"
EMAIL = "ojekojaandco@gmail.com"
ADDRESS = "CR-9, Plot 239, P.W.O. Mafemi Crescent, Utako, FCT-Abuja, Nigeria"
ADDRESS_HTML = "CR-9, Plot 239, P.W.O. Mafemi Crescent,<br>Utako, FCT-Abuja, Nigeria"

# ---------------------------------------------------------------- icons (24px line icons)
def icon(name, cls="ico"):
    paths = ICONS[name]
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

ICONS = {
    "gavel": '<path d="M13.5 3.5l7 7"/><path d="M10.5 6.5l7 7"/><path d="M12 5L7 10"/><path d="M19 12l-5 5"/><path d="M9.5 12.5L3 19l2 2 6.5-6.5"/><path d="M13 21h8"/>',
    "coins": '<ellipse cx="9" cy="6" rx="6" ry="2.5"/><path d="M3 6v4c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V6"/><path d="M3 10v4c0 1.4 2.7 2.5 6 2.5"/><ellipse cx="15" cy="14" rx="6" ry="2.5"/><path d="M9 14v4c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5v-4"/>',
    "building": '<path d="M4 21V5l8-3 8 3v16"/><path d="M2 21h20"/><path d="M8 8h2M14 8h2M8 12h2M14 12h2M8 16h2M14 16h2"/><path d="M10 21v-3h4v3"/>',
    "search": '<path d="M14 3H6a1 1 0 00-1 1v16a1 1 0 001 1h5"/><path d="M14 3l4 4v3"/><path d="M8 8h5M8 11h3"/><circle cx="16" cy="16" r="3.5"/><path d="M18.5 18.5L21 21"/>',
    "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 00-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0012 3z"/><path d="M12 7v3l2 1"/>',
    "house": '<path d="M3 11l9-7 9 7"/><path d="M5 10v11h14V10"/><path d="M10 21v-6h4v6"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "scales": '<path d="M12 3v18M7 21h10"/><path d="M4 7h16"/><circle cx="12" cy="4.5" r="1.3"/><path d="M6 7l-3 7a3 3 0 006 0z"/><path d="M18 7l-3 7a3 3 0 006 0z"/>',
    "handshake": '<path d="M2 12l4-4 4 1 3-2 3 1 6 4"/><path d="M6 8l-4 4 6 6 2-1 2 2 2-1 2 1 2-2 2-1-4-5"/><path d="M10 9l-2 3 2 1 3-2"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "chat": '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.5-3.6 3.2-6 6.5-6s6 2.4 6.5 6"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.2c2.8.1 4.9 2.2 5.4 5.3"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
}

SCALES_MARK = ('<svg viewBox="0 0 120 110" aria-hidden="true"><g fill="none" stroke="#C9A24A" stroke-width="2.4" '
               'stroke-linecap="round" stroke-linejoin="round"><circle cx="60" cy="22" r="8"/><path d="M18 40 H102"/>'
               '<path d="M60 30 V90 a13 13 0 0 1 -26 0"/><path d="M18 40 L8 66 M18 40 L28 66 M102 40 L92 66 M102 40 L112 66"/>'
               '<path d="M4 66 H32 a14 10 0 0 1 -28 0 Z M88 66 H116 a14 10 0 0 1 -28 0 Z"/></g></svg>')

CREST = ('<svg viewBox="0 0 120 140" aria-hidden="true"><path d="M60 4 L112 18 V64 C112 100 88 124 60 136 C32 124 8 100 8 64 V18 Z" fill="#0E1E3A"/>'
         '<path d="M60 12 L105 24 V64 C105 96 84 117 60 128 C36 117 15 96 15 64 V24 Z" fill="none" stroke="#C9A24A" stroke-width="1.5"/>'
         '<g transform="translate(22.8 30) scale(0.62)" fill="none" stroke="#C9A24A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
         '<circle cx="60" cy="22" r="8"/><path d="M18 40 H102"/><path d="M60 30 V90 a13 13 0 0 1 -26 0"/>'
         '<path d="M18 40 L8 66 M18 40 L28 66 M102 40 L92 66 M102 40 L112 66"/>'
         '<path d="M4 66 H32 a14 10 0 0 1 -28 0 Z M88 66 H116 a14 10 0 0 1 -28 0 Z" fill="#C9A24A"/></g></svg>')

# ---------------------------------------------------------------- content
PRACTICE = [
    dict(slug="litigation", title="Litigation", icon="gavel",
         short="Representation before courts and tribunals in civil, commercial and corporate disputes, from strategy to judgment and enforcement.",
         intro="We represent clients in all types of civil, commercial, business and corporate matters before courts and tribunals. Our approach combines careful preparation with practical strategy, so you understand your position and options at every stage.",
         points=["Commercial and contractual disputes", "Corporate and shareholder disputes", "Property and land disputes", "Enforcement of judgments"]),
    dict(slug="debt-recovery", title="Debt Recovery", icon="coins",
         short="Demand letters, negotiated settlements and recovery proceedings to help individuals and businesses recover what they are owed.",
         intro="Unpaid debts strain relationships and cash flow. We help individuals and businesses recover what they are owed promptly and professionally, escalating only as far as each matter requires.",
         points=["Pre-action demand letters", "Negotiated repayment and settlement", "Recovery proceedings in court", "Enforcement of judgments"]),
    dict(slug="corporate-finance-advisory", title="Corporate Finance &amp; Advisory", icon="building",
         short="Company formation, governance, restructuring, financing arrangements and ongoing advice for businesses at every stage.",
         intro="From incorporation to growth and restructuring, we advise businesses on the legal side of their corporate and financing decisions, helping them stay compliant and well protected.",
         points=["Company registration and corporate filings", "Corporate governance and board advisory", "Financing and loan documentation", "Restructuring and reorganisation"]),
    dict(slug="due-diligence", title="Due Diligence", icon="search",
         short="Legal, corporate and title investigations that surface risk before you invest, acquire, lend or enter a partnership.",
         intro="Before you invest, acquire, lend or partner, we investigate the legal position thoroughly, so you can decide with a clear view of the risks.",
         points=["Corporate searches and records review", "Land and property title searches", "Review of contracts, licences and permits", "Clear, practical due diligence reports"]),
    dict(slug="intellectual-property", title="Intellectual Property", icon="bulb",
         short="Registration, protection and enforcement of trademarks, copyrights, patents and designs, plus licensing arrangements.",
         intro="Your ideas, brands and creative works are valuable assets. We help you register, protect, license and enforce your intellectual property rights.",
         points=["Trademark registration and protection", "Copyright advice and protection", "Patent and industrial design registration", "Licensing and enforcement"]),
    dict(slug="real-estate-property", title="Real Estate &amp; Property", icon="house",
         short="Acquisitions, sales, leases, title perfection, Certificates of Occupancy and property dispute resolution.",
         intro="Property transactions demand care. We guide buyers, sellers, landlords and tenants through each step, protecting your interest in the property and your investment.",
         points=["Sales, purchases and leases", "Title perfection and Governor&rsquo;s consent", "Certificates of Occupancy", "Property dispute resolution"]),
    dict(slug="regulatory-compliance", title="Regulatory Compliance &amp; Consultancy", icon="shield",
         short="Guidance on licensing, filings and the regulatory frameworks that apply to your business or sector.",
         intro="Regulation shapes how businesses operate. We provide legal consultancy on the rules that apply to you and help you meet your obligations with confidence.",
         points=["Regulatory licences and permits", "Statutory filings and returns", "Compliance reviews", "Legal opinions and consultancy"]),
    dict(slug="arbitration", title="Arbitration", icon="scales",
         short="Efficient, confidential resolution of commercial disputes, with representation of parties in arbitral proceedings.",
         intro="Arbitration offers a private and often faster route to resolving commercial disputes. We advise on arbitration agreements and represent parties throughout the process.",
         points=["Drafting arbitration clauses", "Representation in arbitral proceedings", "Recognition and enforcement of awards"]),
    dict(slug="mediation-conciliation", title="Mediation &amp; Conciliation", icon="handshake",
         short="Negotiated outcomes that preserve relationships and save time and cost compared with litigation.",
         intro="Not every dispute needs a courtroom. Through mediation and conciliation we help parties reach workable, lasting agreements while preserving important relationships.",
         points=["Representation in mediation", "Conciliation proceedings", "Drafting settlement agreements"]),
]

VALUES = [
    ("clock", "Responsiveness", "Prompt attention and timely delivery, because deadlines and deals rarely wait."),
    ("chat", "Clear Communication", "We keep you informed through in-person, phone and electronic channels throughout your matter."),
    ("shield", "Integrity", "Honest advice and the highest standards of professional conduct in every instruction."),
    ("globe", "National Reach", "Professional relationships across all six geopolitical zones support matters in many jurisdictions."),
]

PARTNER = dict(
    slug="oche-ekoja", name="Oche Thankgod Ekoja", role="Managing Partner", photo="images/oche-ekoja.jpg",
    bio="Oche Ekoja leads O.J. Ekoja &amp; Co. from its principal office in Abuja. The Principal Counsel brings technical legal competence together with a client-centred approach, guiding the firm&rsquo;s work across litigation, corporate advisory and dispute resolution.",
    areas=["Litigation", "Corporate Advisory", "Dispute Resolution"],
)

TEAMWORK = "At O. J. Ekoja &amp; Co., we value collaboration and shared expertise, bringing our collective experience together to deliver effective legal solutions and exceptional service to our clients."
MISSION = "To provide strategic, innovative, and result-oriented legal solutions that protect our clients&rsquo; interests and address their evolving legal needs."
ABOUT_SHORT = "The firm is distinguished by its commitment to excellence, prompt service delivery and the highest standards of professional integrity."

NAV = [("index.html", "Home", "home"), ("about.html", "About Us", "about"), ("practice-areas.html", "Practice Areas", "practice"),
       ("team.html", "Our Team", "team"), ("contact.html", "Contact Us", "contact")]

# ---------------------------------------------------------------- layout
def page(path, title, desc, nav_key, body, crumbs=None):
    depth = path.count("/")
    p = "../" * depth  # relative prefix back to site root
    nav = "".join(f'<a href="{p}{href}"{" class=\"active\" aria-current=\"page\"" if key == nav_key else ""}>{label}</a>' for href, label, key in NAV)
    title_bar = ""
    if crumbs:
        trail = f'<a href="{p}index.html">Home</a>' + "".join(
            (f'<a href="{p}{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>') for t, h in crumbs)
        title_bar = (f'<section class="page-title"><div class="container"><h1 data-anim>{title}</h1>'
                     f'<nav class="breadcrumbs" aria-label="Breadcrumb" data-anim>{trail}</nav></div></section>')
    plinks = "".join(f'<a href="{p}practice/{a["slug"]}.html">{a["title"]}</a>' for a in PRACTICE[:5])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {FIRM}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{p}logo/ojekoja-icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="{p}index.html"><img src="{p}logo/ojekoja-logo-horizontal.svg" alt="{FIRM} — Barristers, Solicitors &amp; Legal Consultants" width="290" height="60"></a>
    <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
    <a class="header-phone" href="tel:{PHONE_2_TEL}">{icon("phone", "")}<span>{PHONE_2}</span></a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
{title_bar}
{body}
</main>
<footer class="site-footer">
  <div class="container footer-top">
    <div>
      <img class="footer-logo" src="{p}logo/ojekoja-logo-reversed.svg" alt="{FIRM}" width="280" height="58" loading="lazy">
      <p>A duly registered Nigerian law firm offering practical, prompt and principled legal services from Abuja to clients across the country.</p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <div class="f-links">{nav}</div>
    </div>
    <div>
      <h4>Get in Touch</h4>
      <ul class="f-contact">
        <li>{icon("pin", "")}<span>{ADDRESS}</span></li>
        <li>{icon("phone", "")}<span><a href="tel:{PHONE_1_TEL}">{PHONE_1}</a><br><a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></span></li>
        <li>{icon("mail", "")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span id="year">2026</span> {FIRM} All rights reserved.</span>
    <span>Information on this website is general and is not legal advice.</span>
  </div>
</footer>
<script src="{p}assets/js/site.js" defer></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html.replace("\n\n\n", "\n"), encoding="utf-8")
    print("built", path)

# ---------------------------------------------------------------- shared blocks
def heading(label, title, center=False, text=""):
    cls = "heading center" if center else "heading"
    t = f"<p>{text}</p>" if text else ""
    return f'<div class="{cls}" data-anim><span class="label">{label}</span><h2>{title}</h2><div class="sep"></div>{t}</div>'

def practice_card(a, p=""):
    return (f'<article class="card">{icon(a["icon"])}<h3>{a["title"]}</h3><p>{a["short"]}</p>'
            f'<a class="more" href="{p}practice/{a["slug"]}.html" aria-label="Read more about {a["title"]}">Read more</a></article>')

def practice_grid(areas, p=""):
    return f'<div class="cards" data-stagger="0.2">{"".join(practice_card(a, p) for a in areas)}</div>'

def strip(p=""):
    return (f'<section class="strip"><div class="container"><h4 data-anim>We are ready to protect your interests.</h4>'
            f'<a class="btn btn-outline-light" href="{p}contact.html" data-anim>Contact Us</a></div></section>')

def art(size_cls="media-art"):
    return f'<div class="{size_cls}">{SCALES_MARK}</div>'

def values_section():
    items = "".join(f'<div class="value">{icon(i)}<div><h4>{t}</h4><p>{d}</p></div></div>' for i, t, d in VALUES)
    return (f'<section class="section grey"><div class="container">'
            f'<div class="heading center" data-anim><h2>What You Can Expect From Us</h2><div class="sep"></div></div>'
            f'<div class="values" data-stagger="0.2">{items}</div></div></section>')

def callback(p=""):
    opts = "".join(f"<option>{a['title']}</option>" for a in PRACTICE)
    return f"""<section class="callback">
  <div class="container">
    <h2 data-anim>Request a Call Back</h2>
    <p class="sub" data-anim>Leave your details and we will call you back promptly.</p>
    <form class="cb-form" data-send="whatsapp" data-subject="Call back request" data-anim>
      <input name="name" data-label="Name" placeholder="Your name" required autocomplete="name" aria-label="Your name">
      <input name="phone" data-label="Phone" type="tel" placeholder="Phone number" required autocomplete="tel" aria-label="Phone number">
      <select name="area" data-label="Practice area" aria-label="Practice area"><option value="">Practice area</option>{opts}</select>
      <button class="btn btn-solid" type="submit" value="whatsapp">Submit</button>
    </form>
  </div>
</section>"""

def sidebar_contact(p=""):
    return (f'<div class="side-box"><h4>Need legal advice?</h4><p>Speak with our team today.</p>'
            f'<a href="tel:{PHONE_2_TEL}">{PHONE_2}</a><a href="mailto:{EMAIL}">{EMAIL}</a>'
            f'<a class="btn btn-solid" href="{p}contact.html">Book a Consultation</a></div>')

# ---------------------------------------------------------------- pages
def build_home():
    slides = f"""<section class="hero" aria-roledescription="carousel" aria-label="Introduction">
  <div class="slide">
    <div class="slide-bg art-scales" data-photo="images/hero-teamwork.jpg"></div>
    <div class="slide-art">{SCALES_MARK}</div>
    <div class="container slide-content">
      <span class="slide-kicker anim">{FIRM}</span>
      <h1 class="anim">Teamwork</h1>
      <p class="anim">{TEAMWORK}</p>
      <div class="btns anim"><a class="btn btn-solid" href="about.html">About the Firm</a><a class="btn btn-outline-light" href="practice-areas.html">Practice Areas</a></div>
    </div>
  </div>
  <div class="slide">
    <div class="slide-bg art-library" data-photo="images/hero-mission.jpg"></div>
    <div class="container slide-content">
      <span class="slide-kicker anim">A dynamic, dedicated team of legal practitioners</span>
      <h2 class="anim">Our Mission</h2>
      <p class="anim">{MISSION}</p>
      <div class="btns anim"><a class="btn btn-solid" href="practice-areas.html">Our Practice Areas</a><a class="btn btn-outline-light" href="contact.html">Contact Us</a></div>
    </div>
  </div>
  <button class="hero-arrow prev" aria-label="Previous slide"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M15 5l-7 7 7 7"/></svg></button>
  <button class="hero-arrow next" aria-label="Next slide"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 5l7 7-7 7"/></svg></button>
  <div class="hero-dots"></div>
</section>"""
    practice = (f'<section class="section grey"><div class="container center">'
                f'{heading("What we do", "Our Practice Areas", center=True)}'
                f'<div style="text-align:left">{practice_grid(PRACTICE[:3])}</div>'
                f'<div class="after-cards" data-anim><a class="btn btn-outline" href="practice-areas.html">View All Practice Areas</a></div>'
                f'</div></section>')
    about = (f'<section class="section"><div class="container split">'
             f'<div class="split-text">{heading("About us", "A dynamic, dedicated team of legal practitioners")}'
             f'<p data-anim>{ABOUT_SHORT}</p>'
             f'<div class="btns" data-anim><a class="btn btn-navy" href="about.html">Read More</a></div></div>'
             f'<div class="split-media" data-anim="fade"><div class="media-frame">{art()}</div></div>'
             f'</div></section>')
    people = (f'<section class="section"><div class="container split reverse">'
              f'<div class="split-text">{heading("Our People", "Managing Partner")}'
              f'<p class="person-name" data-anim>{PARTNER["name"]}</p>'
              f'<span class="person-role" data-anim>{PARTNER["role"]}</span>'
              f'<p data-anim>{PARTNER["bio"]}</p>'
              f'<div class="btns" data-anim><a class="btn btn-navy" href="team/{PARTNER["slug"]}.html">View Profile</a></div></div>'
              f'<div class="split-media" data-anim="fade"><div class="media-frame"><img src="{PARTNER["photo"]}" alt="{PARTNER["name"]}, {PARTNER["role"]}" width="800" height="1200" loading="lazy"></div></div>'
              f'</div></section>')
    body = slides + practice + about + strip() + values_section() + people + callback()
    page("index.html", "Barristers, Solicitors &amp; Legal Consultants, Abuja",
         "O.J. Ekoja & Co. is an Abuja law firm offering litigation, debt recovery, corporate advisory, due diligence, intellectual property, real estate, regulatory compliance and ADR services across Nigeria.",
         "home", body)

ABOUT_TEXT = [
    "O.J. Ekoja &amp; Co. is a duly registered law firm comprising a team of dynamic, innovative and dedicated legal practitioners, with its principal office in the Federal Capital Territory, Abuja, Nigeria. The firm is distinguished by its commitment to excellence, prompt service delivery and the highest standards of professional integrity.",
    "Our practice is founded on the understanding that the essence of legal practice is to serve and protect the interests of clients. This philosophy informs our approach to legal service delivery, combining practical legal solutions, strategic thinking and innovative counsel to address the diverse needs of our clientele.",
    "With our principal office in Abuja and an extensive network of professional relationships across the six geopolitical zones of Nigeria, we are positioned to provide legal support and representation across different jurisdictions.",
    "Under the leadership of our Principal Counsel, Oche Ekoja, Esq., the firm brings together technical legal competence and a client-centred approach to service delivery. We recognise that effective legal representation requires not only a sound understanding of the law but also attentiveness, accessibility and a clear appreciation of each client&rsquo;s unique objectives.",
    "At O.J. Ekoja &amp; Co., we place a premium on responsiveness and timely delivery, recognising that in legal and commercial transactions, time is often of the essence. We are committed to providing prompt, effective and well-considered legal solutions without compromising the quality of our work.",
    "We also recognise that effective communication is fundamental to a successful solicitor-client relationship. We use both conventional and electronic channels to stay accessible and keep clients informed throughout their instructions, and we welcome client feedback to keep improving the quality, efficiency and responsiveness of our services.",
]

def about_menu(active, p=""):
    items = [("about.html", "About Us", "about"), ("team.html", "Our Team", "team"),
             ("practice-areas.html", "Practice Areas", "practice"), ("contact.html", "Contact Us", "contact")]
    links = "".join(f'<a href="{p}{h}"{" class=\"active\"" if k == active else ""}>{t}</a>' for h, t, k in items)
    return f'<nav class="side-menu" aria-label="Company overview"><h4>Company Overview</h4>{links}</nav>'

def build_about():
    paras = "".join(f"<p>{t}</p>" for t in ABOUT_TEXT)
    body = (f'<section class="section"><div class="container with-sidebar right">'
            f'<div class="prose">{heading("Our Expertise", "About O.J. Ekoja &amp; Co.")}<div data-anim>{paras}</div>'
            f'<div class="btns" data-anim><a class="btn btn-navy" href="contact.html">Book a Consultation</a><a class="btn btn-outline" href="team.html">Meet Our Team</a></div></div>'
            f'<aside><div class="sticky" data-anim>{about_menu("about")}{sidebar_contact()}</div></aside>'
            f'</div></section>'
            f'<section class="section grey"><div class="container"><div class="cards" data-stagger="0.2">'
            f'<article class="card">{icon("scales")}<h3>Our Mission</h3><p>{MISSION}</p></article>'
            f'<article class="card">{icon("users")}<h3>Teamwork</h3><p>{TEAMWORK}</p></article>'
            f'<article class="card">{icon("globe")}<h3>Nationwide Reach</h3><p>Principal office in Abuja, with professional relationships across all six geopolitical zones of Nigeria.</p></article>'
            f'</div></div></section>'
            + values_section().replace("section grey", "section")
            + f'<section class="section grey"><div class="container center">{heading("What we do", "Our Practice Areas", center=True)}'
            f'<div style="text-align:left">{practice_grid(PRACTICE)}</div></div></section>'
            + strip())
    page("about.html", "About Us", "About O.J. Ekoja & Co., a registered law firm in Abuja, Nigeria.", "about", body, [("About Us", None)])

def build_practice_index():
    body = (f'<section class="section grey"><div class="container center">'
            f'{heading("What we do", "Counsel Across Civil, Commercial &amp; Corporate Matters", center=True, text="We represent clients in all types of civil, commercial, business and corporate matters. Select a practice area to learn more.")}'
            f'<div style="text-align:left">{practice_grid(PRACTICE)}</div></div></section>' + strip())
    page("practice-areas.html", "Practice Areas", "Practice areas of O.J. Ekoja & Co.", "practice", body, [("Practice Areas", None)])

def build_practice_pages():
    p = "../"
    for a in PRACTICE:
        menu = "".join(f'<a href="{x["slug"]}.html"{" class=\"active\" aria-current=\"page\"" if x is a else ""}>{x["title"]}</a>' for x in PRACTICE)
        pts = "".join(f"<li>{t}</li>" for t in a["points"])
        body = (f'<section class="section"><div class="container with-sidebar">'
                f'<aside><div class="sticky" data-anim><nav class="side-menu" aria-label="Practice areas"><h4>Practice Areas</h4>{menu}</nav>{sidebar_contact(p)}</div></aside>'
                f'<div class="prose"><div class="banner" data-anim="fade">{icon(a["icon"], "")}</div>'
                f'<div data-anim><span class="label">Practice Area</span><h2>{a["title"]}</h2><p class="lead">{a["short"]}</p><p>{a["intro"]}</p>'
                f'<h3>How we can help</h3><ul class="ticks">{pts}</ul></div>'
                f'<div class="btns" data-anim><a class="btn btn-navy" href="{p}contact.html">Discuss Your Matter</a><a class="btn btn-outline" href="{p}practice-areas.html">All Practice Areas</a></div>'
                f'</div></div></section>' + strip(p))
        page(f"practice/{a['slug']}.html", a["title"], f"{a['title']} services at O.J. Ekoja & Co., Abuja.", "practice", body,
             [("Practice Areas", "practice-areas.html"), (a["title"], None)])

def member_card(m, p=""):
    return (f'<article class="member"><a class="photo" href="{p}team/{m["slug"]}.html" tabindex="-1" aria-hidden="true">'
            f'<img src="{p}{m["photo"]}" alt="" width="800" height="1200" loading="lazy"></a>'
            f'<div class="info"><h3>{m["name"]}</h3><span class="person-role">{m["role"]}</span>'
            f'<p>{m["bio"][:150].rsplit(" ", 1)[0]}&hellip;</p><a class="more" href="{p}team/{m["slug"]}.html">View Profile</a></div></article>')

def build_team():
    body = (f'<section class="section"><div class="container split">'
            f'<div class="split-text">{heading("Our Team", "Teamwork")}<p class="lead" data-anim>{TEAMWORK}</p>'
            f'<div class="btns" data-anim><a class="btn btn-navy" href="contact.html">Work With Us</a></div></div>'
            f'<div class="split-media" data-anim="fade"><div class="media-frame">{art()}</div></div></div></section>'
            f'<section class="section grey"><div class="container">{heading("Our People", "Meet the Team", center=True)}'
            f'<div class="team-grid" data-stagger="0.2">{member_card(PARTNER)}</div></div></section>' + strip())
    page("team.html", "Our Team", "Meet the team at O.J. Ekoja & Co.", "team", body, [("About Us", "about.html"), ("Our Team", None)])

def build_profile():
    p = "../"
    m = PARTNER
    tags = "".join(f"<span>{t}</span>" for t in m["areas"])
    body = (f'<section class="section"><div class="container profile">'
            f'<div class="photo-wrap split-media" data-anim="fade"><div class="media-frame"><img src="{p}{m["photo"]}" alt="{m["name"]}, {m["role"]}" width="800" height="1200"></div></div>'
            f'<div class="prose" data-anim><span class="label">{m["role"]}</span><h2>{m["name"]}</h2><div class="heading" style="margin-bottom:24px"><div class="sep"></div></div>'
            f'<p>{m["bio"]}</p><div class="tags">{tags}</div>'
            f'<div class="contact-lines"><a href="tel:{PHONE_2_TEL}">{PHONE_2}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>'
            f'<div class="btns"><a class="btn btn-navy" href="{p}contact.html">Book a Consultation</a><a class="btn btn-outline" href="{p}team.html">Back to Team</a></div></div>'
            f'</div></section>' + strip(p))
    page(f"team/{m['slug']}.html", m["name"], f"{m['name']}, {m['role']} at O.J. Ekoja & Co.", "team", body,
         [("Our Team", "team.html"), (m["name"], None)])

def build_contact():
    opts = "".join(f"<option>{a['title']}</option>" for a in PRACTICE)
    body = f"""<section class="section"><div class="container">
  {heading("Get in touch", "We Are Here to Help", center=True, text="Let us know how we can assist. Call, email or visit our office, or send us a message using the form below.")}
  <div class="info-cols" data-stagger="0.2">
    <div class="info">{icon("phone")}<h4>Call Us</h4><a href="tel:{PHONE_1_TEL}">{PHONE_1}</a><a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></div>
    <div class="info">{icon("mail")}<h4>Email Us</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="info">{icon("pin")}<h4>Visit Us</h4><address>{ADDRESS_HTML}</address></div>
  </div>
</div></section>
<section class="section grey"><div class="container form-band">
  <div data-anim>
    <span class="label">Feedback form</span><h2 style="margin-bottom:26px">Send Us a Message</h2>
    <form data-send="email" data-subject="Website enquiry">
      <div class="form-grid">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" data-label="Name" required autocomplete="name"></div>
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" data-label="Phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" data-label="Email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="f-area">Practice area</label><select id="f-area" name="area" data-label="Practice area"><option value="">General enquiry</option>{opts}</select></div>
        <div class="field full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" data-label="Message" required></textarea></div>
      </div>
      <div class="btns"><button class="btn btn-navy" type="submit" value="email">Send by Email</button><button class="btn btn-solid" type="submit" value="whatsapp">Send on WhatsApp</button></div>
      <p class="form-note">Sending a message does not create a lawyer&ndash;client relationship. Please do not include confidential documents at this stage.</p>
    </form>
  </div>
  <iframe class="map" data-anim="fade" title="Map of Utako, Abuja" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=P.W.O.+Mafemi+Crescent,+Utako,+Abuja&amp;output=embed"></iframe>
</div></section>"""
    page("contact.html", "Contact Us", "Contact O.J. Ekoja & Co. in Utako, Abuja.", "contact", body, [("Contact Us", None)])

if __name__ == "__main__":
    build_home(); build_about(); build_practice_index(); build_practice_pages(); build_team(); build_profile(); build_contact()
