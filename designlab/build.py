#!/usr/bin/env python3
"""Build script for Polar DesignLab static site."""
import os

PAGES = {
    "home": ("index.html", "Home"),
    "bespoke-design": ("bespoke-design.html", "Bespoke Design"),
    "uk-manufacturing": ("uk-manufacturing.html", "UK Manufacturing"),
    "thermal-testing": ("thermal-testing.html", "Thermal Testing"),
    "technical-reports": ("technical-reports.html", "Technical Reports"),
    "portfolio": ("portfolio.html", "Product Portfolio"),
    "our-work": ("our-work.html", "Our Work & Clients"),
    "start": ("start.html", "Start a Project"),
}

NAV_ITEMS = [
    ("home", "Home", "index.html"),
    ("capabilities", "Capabilities", "#capabilities"),
    ("portfolio", "Product Portfolio", "portfolio.html"),
    ("our-work", "Our Work", "our-work.html"),
]


def nav(active, depth=""):
    items = []
    for key, label, href in NAV_ITEMS:
        cls = ' class="active"' if key == active else ""
        url = depth + href if not href.startswith("#") else href
        items.append(f'<li><a href="{url}"{cls}>{label}</a></li>')
    return "\n          ".join(items)


def header(active, depth=""):
    return f"""<header class="site-header">
  <a href="{depth}index.html" class="logo">
    <img src="{depth}assets/images/logo/polardesignlab-logo-on-light.png" alt="Polar DesignLab" class="logo-lockup">
  </a>
  <nav class="main-nav">
    <ul>
      {nav(active, depth)}
    </ul>
    <a href="{depth}start.html" class="btn btn-primary">Discuss Your Project</a>
  </nav>
</header>"""


def footer(depth=""):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>
          <img src="{depth}assets/images/logo/polardesignlab-logo.png" alt="" class="footer-logo-icon">
          Polar DesignLab
        </h4>
        <p>Concept. Design. Validate. A division of Polar Thermal Packaging Ltd — precision thermal packaging engineered and manufactured in the UK.</p>
      </div>
      <div>
        <h4>Capabilities</h4>
        <ul>
          <li><a href="{depth}bespoke-design.html">Bespoke Design</a></li>
          <li><a href="{depth}uk-manufacturing.html">UK Manufacturing</a></li>
          <li><a href="{depth}thermal-testing.html">Thermal Testing</a></li>
          <li><a href="{depth}technical-reports.html">Technical Reports</a></li>
        </ul>
      </div>
      <div>
        <h4>Portfolio</h4>
        <ul>
          <li><a href="{depth}portfolio.html">Product Portfolio</a></li>
          <li><a href="{depth}our-work.html">Our Work &amp; Clients</a></li>
          <li><a href="{depth}start.html">Discuss Your Project</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <ul>
          <li>Polar House, Roman Way,<br>Crusader Park, Warminster,<br>Wiltshire, BA12 8SP</li>
          <li><a href="tel:+441985214111">01985 214 111</a></li>
          <li><a href="mailto:sales@polarthermal.com">sales@polarthermal.com</a></li>
        </ul>
      </div>
    </div>
    <div class="accreditations-strip">
      <p>Accreditations &amp; Memberships</p>
      <div class="accreditations-logos">
        <img src="{depth}assets/images/accreditations/mib-logo.jpg" alt="MIB">
        <img src="{depth}assets/images/accreditations/coldchainfederaion-logo.png" alt="Cold Chain Federation">
        <img src="{depth}assets/images/accreditations/joscar-logo.png" alt="JOSCAR">
        <img src="{depth}assets/images/accreditations/nhs-approved-logo.png" alt="NHS Approved">
        <img src="{depth}assets/images/accreditations/iso9001-logo.jpg" alt="ISO 9001">
        <img src="{depth}assets/images/accreditations/iso14001-logo.png" alt="ISO 14001">
        <img src="{depth}assets/images/accreditations/mod-bae-logo.png" alt="MOD/BAE">
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Polar Thermal Packaging Ltd. UK Registered Company No. 08251766.</span>
      <span>
        <a href="https://polarthermal.com/privacy-policy">Privacy Policy</a>
        <a href="https://polarthermal.com/terms-conditions">Terms &amp; Conditions</a>
        <a href="https://polarthermal.com/modern-slavery-statement">Modern Slavery Statement</a>
      </span>
    </div>
  </div>
</footer>"""


def cta_band(depth=""):
    return f"""<section class="cta-band">
  <div class="container">
    <h2>Ready to bring your thermal challenge to life?</h2>
    <a href="{depth}start.html" class="btn btn-outline">Discuss Your Project</a>
  </div>
</section>"""


def page(title, active, body, depth=""):
    css = f"{depth}css/style.css"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Polar DesignLab</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
{header(active, depth)}
{body}
{footer(depth)}
</body>
</html>"""


def build_index():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">concept / design / validate</p>
      <h1>Your Challenge.<br>Our Design.<br>Proven Performance.</h1>
      <p>Polar DesignLab engineers bespoke thermal packaging solutions — from first concept through UK manufacturing to validated performance data.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
        <a href="portfolio.html" class="btn btn-outline" style="border-color:#fff;color:#fff;">View Portfolio</a>
      </div>
    </div>
    <div class="hero-image">
      <div class="hero-slideshow">
        <img src="assets/images/hero/dotbox-hero.png" alt="Dotbox thermal packaging">
        <img src="assets/images/hero/polarpod-hero.png" alt="PolarPod thermal packaging">
        <img src="assets/images/hero/polar-pods-hero.png" alt="Polar Pods thermal packaging">
        <img src="assets/images/hero/cook-hero.png" alt="Cook medical packaging">
        <img src="assets/images/hero/ld3-hero.png" alt="LD3 thermal packaging">
      </div>
    </div>
  </div>
</section>

<div class="tagline-strip">concept / design / validate</div>

<section class="section" id="capabilities">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What We Do</p>
      <h2>End-to-End Thermal Packaging Solutions</h2>
      <p>From initial brief to production-ready packaging, Polar DesignLab manages every stage in-house — giving you a single point of accountability.</p>
    </div>
    <div class="panels">
      <a href="bespoke-design.html" class="panel">
        <div class="panel-media design">BESPOKE DESIGN</div>
        <div class="panel-body">
          <h3>Bespoke Design</h3>
          <p>Custom thermal packaging engineered to your exact payload, temperature range, and duration requirements.</p>
          <ul>
            <li>Payload & temperature profiling</li>
            <li>Material selection & simulation</li>
            <li>Prototype iteration</li>
            <li>Design freeze & documentation</li>
          </ul>
          <span class="btn btn-outline">Learn More</span>
        </div>
      </a>
      <a href="uk-manufacturing.html" class="panel">
        <div class="panel-media manufacture">UK MANUFACTURING</div>
        <div class="panel-body">
          <h3>UK Manufacturing</h3>
          <p>Vertically integrated production at our UK facility — fast lead times, full traceability, no overseas supply chain risk.</p>
          <ul>
            <li>In-house foam & insulation fabrication</li>
            <li>PCM integration & filling</li>
            <li>Quality inspection at every stage</li>
            <li>Scalable from pilot to volume</li>
          </ul>
          <span class="btn btn-outline">Learn More</span>
        </div>
      </a>
      <a href="thermal-testing.html" class="panel">
        <div class="panel-media testing">THERMAL TESTING</div>
        <div class="panel-body">
          <h3>Thermal Testing</h3>
          <p>Rigorous real-world validation in our temperature-controlled chambers before your packaging ships.</p>
          <ul>
            <li>Summer & winter profile testing</li>
            <li>Duration & worst-case simulations</li>
            <li>Data-logged performance records</li>
            <li>ISTA & bespoke protocol support</li>
          </ul>
          <span class="btn btn-outline">Learn More</span>
        </div>
      </a>
      <a href="technical-reports.html" class="panel">
        <div class="panel-media validate">TECHNICAL REPORTS</div>
        <div class="panel-body">
          <h3>Technical Reports</h3>
          <p>Detailed engineering documentation for regulatory submissions, tender bids, and supply chain sign-off.</p>
          <ul>
            <li>Performance validation certificates</li>
            <li>Temperature excursion analysis</li>
            <li>Payload compatibility statements</li>
            <li>Regulatory-ready formatting</li>
          </ul>
          <span class="btn btn-outline">Learn More</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Our Process</p>
      <h2>How We Work</h2>
      <p>A structured four-stage process that takes your thermal packaging from concept to validated production.</p>
    </div>
    <div class="process-steps">
      <div class="step">
        <div class="step-num">1</div>
        <h4>Brief</h4>
        <p>We understand your payload, temperature requirements, transit duration and regulatory constraints.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h4>Design</h4>
        <p>Our engineers develop and iterate a bespoke solution, selecting materials and geometry for optimum performance.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h4>Validate</h4>
        <p>Prototype testing in our chambers confirms performance before you commit to production tooling.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <h4>Manufacture</h4>
        <p>UK production with full traceability. We scale with you from pilot batches to volume supply.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Who We Work With</p>
      <h2>Trusted Across Regulated Industries</h2>
      <p>Polar DesignLab serves clients where temperature control is critical and failure is not an option.</p>
    </div>
    <div class="facts-grid">
      <div class="fact"><strong>2–8°C</strong><span>Cold chain precision</span></div>
      <div class="fact"><strong>-80°C</strong><span>Ultra-cold capability</span></div>
      <div class="fact"><strong>96h+</strong><span>Validated durations</span></div>
      <div class="fact"><strong>UK</strong><span>Designed & manufactured</span></div>
    </div>
    <div class="clients-strip">
      <span class="client-name">Pharmaceutical</span>
      <span class="client-name">Biotech</span>
      <span class="client-name">Diagnostics</span>
      <span class="client-name">Clinical Trials</span>
      <span class="client-name">Veterinary</span>
      <span class="client-name">Food &amp; Beverage</span>
    </div>
  </div>
</section>
"""
    return page("Home", "home", body + cta_band())


def build_bespoke_design():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Capability</p>
      <h1>Bespoke Thermal Packaging Design</h1>
      <p>Every thermal challenge is unique. We engineer packaging from the ground up to match your exact payload, temperature profile, and operational constraints.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="service-hero">
      <div>
        <p class="eyebrow">Our Approach</p>
        <h2>Engineered for Your Exact Requirements</h2>
        <p>Off-the-shelf thermal packaging rarely delivers optimal performance. Polar DesignLab designs around your specific payload — its geometry, thermal mass, and criticality — not around a standard box size.</p>
        <ul class="spec-list">
          <li>Payload characterisation and thermal mass calculation</li>
          <li>Temperature range definition (ambient, +2–8°C, -20°C, -80°C)</li>
          <li>Transit duration and worst-case scenario modelling</li>
          <li>Material selection: VIP, PU foam, PCM, gel packs</li>
          <li>Geometric optimisation for payload fit and void minimisation</li>
          <li>Prototype build and iterative refinement</li>
        </ul>
        <a href="start.html" class="btn btn-primary">Start a Design Brief</a>
      </div>
      <div>
        <div class="card-media" style="height:360px;border-radius:12px;background:linear-gradient(135deg,#0b2d44,#1c5478);display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.2rem;font-weight:700;">Bespoke Design Studio</div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Design Process</p>
      <h2>From Brief to Validated Prototype</h2>
    </div>
    <div class="process-steps">
      <div class="step"><div class="step-num">1</div><h4>Requirements</h4><p>Define temperature range, duration, payload dimensions, regulatory context and quantities.</p></div>
      <div class="step"><div class="step-num">2</div><h4>Concept</h4><p>Multiple concept directions explored — geometry, insulation strategy, PCM type and configuration.</p></div>
      <div class="step"><div class="step-num">3</div><h4>Prototype</h4><p>Rapid prototyping of the preferred concept, ready for thermal validation testing.</p></div>
      <div class="step"><div class="step-num">4</div><h4>Iterate</h4><p>Test data informs refinement cycles until design performance targets are met.</p></div>
      <div class="step"><div class="step-num">5</div><h4>Freeze</h4><p>Design freeze documentation, BOM and manufacturing drawings handed to production.</p></div>
    </div>
  </div>
</section>
"""
    return page("Bespoke Design", "capabilities", body + cta_band())


def build_uk_manufacturing():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Capability</p>
      <h1>UK Manufacturing</h1>
      <p>Vertically integrated thermal packaging production at our UK facility — fast lead times, full traceability, and no overseas supply chain exposure.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="service-hero">
      <div>
        <p class="eyebrow">Made in the UK</p>
        <h2>Production Under One Roof</h2>
        <p>By manufacturing in-house, Polar DesignLab maintains direct control of quality, lead times, and specification compliance — with no dependency on third-party manufacturers.</p>
        <ul class="spec-list">
          <li>Rigid and flexible insulation fabrication</li>
          <li>PCM filling, sealing and integration</li>
          <li>Vacuum insulation panel (VIP) handling</li>
          <li>Outer carton and liner assembly</li>
          <li>Labelling and outbound preparation</li>
          <li>Full batch traceability records</li>
        </ul>
        <a href="start.html" class="btn btn-primary">Discuss Your Volume</a>
      </div>
      <div>
        <video autoplay muted loop playsinline style="width:100%;border-radius:12px;display:block;">
          <source src="https://poladesignlab.com/assets/videos/polar-factory_lores.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Capabilities</p>
      <h2>What We Manufacture</h2>
    </div>
    <div class="product-grid">
      <div class="card"><div class="panel-body"><span class="tag">Insulation</span><h3>Rigid Foam Fabrication</h3><p>CNC-cut EPS, EPP and PIR foam components to tight tolerances for consistent thermal performance.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">PCM</span><h3>Phase Change Integration</h3><p>In-house filling and sealing of PCM panels and pouches across a range of transition temperatures.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">VIP</span><h3>Vacuum Insulation Panels</h3><p>Careful handling, cutting and integration of VIPs for ultra-low wall-thickness applications.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Assembly</span><h3>Complete Pack Assembly</h3><p>Final assembly, liner fitting, PCM conditioning and pack closure for dispatch-ready units.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Scale</span><h3>Pilot to Volume</h3><p>From 50-unit pilot batches to high-volume supply — production scales to match your demand curve.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Quality</span><h3>Inspection & Traceability</h3><p>In-process inspection, dimensional checks and batch records maintained for every production run.</p></div></div>
    </div>
  </div>
</section>
"""
    return page("UK Manufacturing", "capabilities", body + cta_band())


def build_thermal_testing():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Capability</p>
      <h1>Thermal Performance Testing</h1>
      <p>Rigorous real-world validation in our temperature-controlled chambers — so you know your packaging performs before your payload ships.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="service-hero">
      <div>
        <p class="eyebrow">Testing Capability</p>
        <h2>Validate Before You Ship</h2>
        <p>Polar DesignLab operates temperature-controlled test chambers capable of simulating seasonal ambient profiles, extreme scenarios, and custom duration profiles matched to your real-world transit conditions.</p>
        <ul class="spec-list">
          <li>Summer profile: +35°C ambient simulation</li>
          <li>Winter profile: -20°C ambient simulation</li>
          <li>Extended duration tests: up to 120 hours and beyond</li>
          <li>Data-logged internal payload temperature throughout</li>
          <li>ISTA 7D protocol support</li>
          <li>Bespoke protocol design for unusual routes or payloads</li>
        </ul>
        <a href="start.html" class="btn btn-primary">Submit a Test Brief</a>
      </div>
      <div>
        <div class="card-media" style="height:360px;border-radius:12px;background:linear-gradient(135deg,#4a1a2a,#8a0f20);display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.2rem;font-weight:700;">Thermal Test Chambers</div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Test Types</p>
      <h2>Testing Protocols We Offer</h2>
    </div>
    <div class="panels">
      <div class="panel">
        <div class="panel-media design">QUALIFICATION</div>
        <div class="panel-body">
          <h3>Qualification Testing</h3>
          <p>Full performance qualification of a new packaging design against defined acceptance criteria.</p>
          <ul>
            <li>Worst-case seasonal profiles</li>
            <li>Pass/fail determination</li>
            <li>Qualification report issued</li>
          </ul>
        </div>
      </div>
      <div class="panel">
        <div class="panel-media validate">VALIDATION</div>
        <div class="panel-body">
          <h3>Validation &amp; Re-validation</h3>
          <p>Periodic re-validation testing to confirm ongoing performance, or after design changes.</p>
          <ul>
            <li>Periodic re-test scheduling</li>
            <li>Change-control validation</li>
            <li>Comparative performance records</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    return page("Thermal Testing", "capabilities", body + cta_band())


def build_technical_reports():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Capability</p>
      <h1>Technical Reports</h1>
      <p>Engineering documentation that stands up to regulatory scrutiny — performance certificates, excursion analysis, and payload compatibility statements.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="service-hero">
      <div>
        <p class="eyebrow">Documentation</p>
        <h2>Reports That Pass Scrutiny</h2>
        <p>Whether you need documentation for an internal qualification process, a regulatory submission, or a customer tender, Polar DesignLab produces clear, data-rich technical reports that stand up to expert review.</p>
        <ul class="spec-list">
          <li>Performance validation certificates with raw data appendices</li>
          <li>Temperature excursion risk assessments</li>
          <li>Payload compatibility statements</li>
          <li>Design justification documents</li>
          <li>GDP-aligned packaging qualification reports</li>
          <li>Bespoke report formats to match your SOPs</li>
        </ul>
        <a href="start.html" class="btn btn-primary">Request a Report</a>
      </div>
      <div>
        <div class="card-media" style="height:360px;border-radius:12px;background:linear-gradient(135deg,#b38600,#ffc000);display:flex;align-items:center;justify-content:center;color:#0b2d44;font-size:1.2rem;font-weight:700;">Technical Documentation</div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Report Types</p>
      <h2>What We Produce</h2>
    </div>
    <div class="product-grid">
      <div class="card"><div class="panel-body"><span class="tag">Qualification</span><h3>Performance Qualification Report</h3><p>Full test data, protocol description, pass/fail criteria and conclusion — ready for QA sign-off.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Risk</span><h3>Excursion Risk Assessment</h3><p>Identifies scenarios where payload temperature could be breached and quantifies likelihood.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Regulatory</span><h3>GDP Qualification Pack</h3><p>Documentation package structured for GDP-compliant pharmaceutical cold chain qualification.</p></div></div>
      <div class="card"><div class="panel-body"><span class="tag">Payload</span><h3>Compatibility Statement</h3><p>Engineering statement confirming packaging suitability for a specific product and route.</p></div></div>
    </div>
  </div>
</section>
"""
    return page("Technical Reports", "capabilities", body + cta_band())


def build_portfolio():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Portfolio</p>
      <h1>Product Portfolio</h1>
      <p>A selection of validated thermal packaging solutions from the Polar DesignLab range — engineered, manufactured and tested in the UK.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Cold Chain Solutions</p>
      <h2>Validated Packaging for Every Temperature Range</h2>
    </div>
    <div class="product-grid">
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#0b2d44,#1c5478);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">2–8°C</div>
        <div class="card-body">
          <span class="tag">Refrigerated</span>
          <h3>DL-R Series</h3>
          <p>Controlled ambient packaging maintaining +2–8°C for standard pharmaceutical and diagnostic payloads. Available in multiple footprint sizes.</p>
          <a href="start.html" class="btn btn-outline">Enquire</a>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#1a3a1a,#2e6b2e);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">-20°C</div>
        <div class="card-body">
          <span class="tag">Frozen</span>
          <h3>DL-F Series</h3>
          <p>Frozen payload packaging for -20°C products. PCM-optimised design for consistent temperature hold across summer and winter profiles.</p>
          <a href="start.html" class="btn btn-outline">Enquire</a>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#0d1a3a,#0b2d44);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">-80°C</div>
        <div class="card-body">
          <span class="tag">Ultra-Cold</span>
          <h3>DL-UC Series</h3>
          <p>Ultra-cold packaging for -80°C biological and cell therapy payloads using dry ice with controlled sublimation rate and maximum hold time.</p>
          <a href="start.html" class="btn btn-outline">Enquire</a>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#b38600,#ffc000);display:flex;align-items:center;justify-content:center;color:#0b2d44;font-weight:700;">CRT</div>
        <div class="card-body">
          <span class="tag">Ambient</span>
          <h3>DL-A Series</h3>
          <p>Controlled room temperature packaging for +15–25°C products. Protects against both cold excursions in winter and heat in summer.</p>
          <a href="start.html" class="btn btn-outline">Enquire</a>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#4a1a2a,#8a0f20);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">BESPOKE</div>
        <div class="card-body">
          <span class="tag">Custom</span>
          <h3>DL-X Bespoke</h3>
          <p>Fully bespoke designs engineered to your unique payload, temperature target, transit duration and regulatory requirements.</p>
          <a href="start.html" class="btn btn-primary">Start Your Brief</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    return page("Product Portfolio", "portfolio", body + cta_band())


def build_our_work():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Our Work &amp; Clients</p>
      <h1>Delivering Proven Performance</h1>
      <p>Polar DesignLab has engineered thermal packaging solutions for clients across pharmaceutical, biotech, diagnostics and food sectors.</p>
      <div class="hero-actions">
        <a href="start.html" class="btn btn-primary">Discuss Your Project</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Case Studies</p>
      <h2>Projects We're Proud Of</h2>
    </div>
    <div class="product-grid">
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#0b2d44,#1c5478);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem;">Pharmaceutical</div>
        <div class="card-body">
          <span class="tag">+2–8°C</span>
          <h3>Biologics Distribution Pack</h3>
          <p>A bespoke 2–8°C pack for an injectable biologic requiring 96-hour hold across summer and winter EU routes. Designed, manufactured and qualified in 14 weeks.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#1a3a1a,#2e6b2e);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem;">Diagnostics</div>
        <div class="card-body">
          <span class="tag">Refrigerated</span>
          <h3>Diagnostic Kit Shipper</h3>
          <p>High-volume refrigerated shipper for a diagnostics manufacturer distributing to European laboratories. Validated to ISTA 7D with GDP qualification report.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-media" style="background:linear-gradient(135deg,#0d1a3a,#0b2d44);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem;">Cell Therapy</div>
        <div class="card-body">
          <span class="tag">-80°C</span>
          <h3>Cell Therapy Transport System</h3>
          <p>Ultra-cold packaging for a cell therapy developer requiring 48-hour -80°C hold for autologous cell products. VIP-enhanced design with dry ice optimisation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Industries</p>
      <h2>Sectors We Serve</h2>
    </div>
    <div class="facts-grid">
      <div class="fact"><strong>Pharma</strong><span>GMP-aware design &amp; GDP qualification</span></div>
      <div class="fact"><strong>Biotech</strong><span>Cell therapies, biologics, biosimilars</span></div>
      <div class="fact"><strong>Diagnostics</strong><span>High-volume, cost-effective shippers</span></div>
      <div class="fact"><strong>Food &amp; Bev</strong><span>Premium ambient and chilled D2C</span></div>
    </div>
    <div class="clients-strip" style="margin-top:48px;">
      <span class="client-name">Pharmaceutical</span>
      <span class="client-name">Biotech</span>
      <span class="client-name">Diagnostics</span>
      <span class="client-name">Clinical Trials</span>
      <span class="client-name">Veterinary</span>
      <span class="client-name">Food &amp; Beverage</span>
    </div>
  </div>
</section>
"""
    return page("Our Work & Clients", "our-work", body + cta_band())


def build_start():
    body = """
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">Start a Project</p>
      <h1>Discuss Your Project</h1>
      <p>Tell us about your thermal packaging challenge. One of our engineers will respond within one working day.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div>
        <div class="contact-card">
          <h4>Phone</h4>
          <a href="tel:+441985214111">01985 214 111</a>
        </div>
        <div class="contact-card">
          <h4>Email</h4>
          <a href="mailto:sales@polarthermal.com">sales@polarthermal.com</a>
        </div>
        <div class="contact-card">
          <h4>Address</h4>
          <p>Polar House, Roman Way,<br>Crusader Park, Warminster,<br>Wiltshire, BA12 8SP</p>
        </div>
        <div class="contact-card">
          <h4>What to Expect</h4>
          <p>After submitting your brief, an engineer will review your requirements and contact you within one working day to arrange a technical call.</p>
        </div>
      </div>
      <div>
        <form action="#" method="post">
          <div class="form-row">
            <div>
              <label for="company">Company *</label>
              <input type="text" id="company" name="company" required placeholder="Your company name">
            </div>
            <div>
              <label for="name">Your Name *</label>
              <input type="text" id="name" name="name" required placeholder="Full name">
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="email">Email *</label>
              <input type="email" id="email" name="email" required placeholder="you@company.com">
            </div>
            <div>
              <label for="phone">Phone</label>
              <input type="tel" id="phone" name="phone" placeholder="+44...">
            </div>
          </div>
          <label for="service">Service Type *</label>
          <select id="service" name="service" required>
            <option value="">Select a service...</option>
            <option value="design">Bespoke Design</option>
            <option value="manufacture">UK Manufacturing</option>
            <option value="testing">Thermal Testing</option>
            <option value="reports">Technical Reports</option>
            <option value="full">Full end-to-end project</option>
          </select>
          <div class="form-row">
            <div>
              <label for="application">Application / Product Type *</label>
              <input type="text" id="application" name="application" required placeholder="e.g. injectable biologic">
            </div>
            <div>
              <label for="temp">Target Temperature Range *</label>
              <input type="text" id="temp" name="temp" required placeholder="e.g. +2–8°C">
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="duration">Transit Duration *</label>
              <input type="text" id="duration" name="duration" required placeholder="e.g. 48 hours">
            </div>
            <div>
              <label for="quantity">Estimated Annual Quantity</label>
              <input type="text" id="quantity" name="quantity" placeholder="e.g. 5,000 units">
            </div>
          </div>
          <label for="payload">Payload Description</label>
          <input type="text" id="payload" name="payload" placeholder="Dimensions, weight, fragility notes...">
          <label for="description">Project Description *</label>
          <textarea id="description" name="description" rows="5" required placeholder="Tell us more about your project, timeline, and any specific requirements..."></textarea>
          <label for="file">Supporting Files (optional)</label>
          <input type="file" id="file" name="file" accept=".pdf,.doc,.docx,.xls,.xlsx,.png,.jpg">
          <button type="submit" class="btn btn-primary" style="width:100%;padding:14px;">Submit Brief</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
    return page("Start a Project", "start", body)


def main():
    os.makedirs(".", exist_ok=True)

    pages = [
        ("index.html", build_index()),
        ("bespoke-design.html", build_bespoke_design()),
        ("uk-manufacturing.html", build_uk_manufacturing()),
        ("thermal-testing.html", build_thermal_testing()),
        ("technical-reports.html", build_technical_reports()),
        ("portfolio.html", build_portfolio()),
        ("our-work.html", build_our_work()),
        ("start.html", build_start()),
    ]

    for filename, content in pages:
        with open(filename, "w") as f:
            f.write(content)
        print(f"Built {filename}")

    print(f"\nBuilt {len(pages)} pages.")


if __name__ == "__main__":
    main()
