<p align="center"><a href="https://www.linkedin.com/in/sandeepnaysrania"><img src="assets/terminal-card.svg?v=5" alt="Terminal card: Sandeep Kumar Naysrania, quality and security engineer, Ireland" width="100%"></a></p>

<p align="center">
  <a href="https://www.linkedin.com/in/sandeepnaysrania"><img src="assets/badge-linkedin.svg?v=5" alt="LinkedIn" height="38"></a>
  <a href="https://github.com/Naysrania18"><img src="assets/badge-github.svg?v=5" alt="GitHub" height="38"></a>
</p>
<!-- TODO(owner): add email and portfolio badges when you want them public. -->

<p align="center"><img src="assets/metrics-pills.svg?v=5" alt="210+ Python tests, 66 Java tests, 20+ security labs documented, 90/85/90 coverage gates, 22-finding LLM triage evaluation, 4 planted defects documented" width="100%"></p>

<p align="center">
I design layered test strategies and security tooling for web and API systems.<br>
My work spans automated suites in CI, OWASP-aligned API checks and LLM-assisted triage with human review.<br>
Public projects use demo systems and fake data, and security tools refuse to run without authorization.
</p>

<p align="center"><b>Open to QA and security-focused testing roles in Ireland.</b></p>
<!-- TODO(owner): confirm the "Open to" line. It comes from your previous profile text. -->

<!-- Impact (experience) omitted: no verified roles, employers or dates were available. TODO(owner): add from LinkedIn. -->

## How I test & secure applications

My process follows the ideas in OWASP ASVS, OWASP SAMM and the Microsoft SDL: shift testing left, treat every stage as a gate, and loop findings back through retest.

<p align="center"><img src="assets/ssdlc-workflow.svg?v=5" alt="Animated secure development lifecycle: Plan, Code, Build, Test, Release. Each stage lists its automated and manual checks." width="100%"></p>

<details>
<summary>The five stages as text</summary>
<ol>
<li><b>Plan & threat model</b> (before code is written):<br>Test strategy: acceptance criteria, edge cases (defined)<br>Threat model: STRIDE, trust boundaries (mapped)</li>
<li><b>Code & static analysis</b> (CI, pre-merge gates):<br>Secrets + lint: GitLeaks, markdownlint (pass)<br>Unit + integration: pytest, Vitest, TestNG (pass)<br>SAST: Bandit, Semgrep (2 flagged)</li>
<li><b>Build & infrastructure</b> (before deployment):<br>Container + CI: Docker, GitHub Actions (pass)<br>Resilience: Toxiproxy fault injection (1 gap)</li>
<li><b>Dynamic QA & security</b> (staging environment):<br>E2E + API QA: Playwright, Postman, Pact (pass)<br>Automated DAST: OWASP ZAP (pass)<br>Manual pentest: Burp Suite, OWASP Top 10 (IDOR found)</li>
<li><b>Release, monitor & remediate</b> (production):<br>Retest loop: triage, fix, verify (all fixed)<br>Release gate: no critical or high open (approved)<br>Monitoring: smoke tests, runtime alerts (live)</li>
</ol>
<p><i>Statuses are illustrative examples, not client results. The tools named are ones used in my public repositories.</i></p>
</details>

## Featured systems

<table>
<tr><td width="50%" valign="top"><b><a href="https://github.com/Naysrania18/insurance-quality-engineering">insurance-quality-engineering</a></b><br><a href="https://github.com/Naysrania18/insurance-quality-engineering/actions/workflows/ci.yml"><img src="https://github.com/Naysrania18/insurance-quality-engineering/actions/workflows/ci.yml/badge.svg" alt="CI status for insurance-quality-engineering"></a> <code>MIT</code><br><br>A demo commercial-insurance platform with a layered test approach: unit, API, contract, SQL, event-driven, UI, migration, security, performance and resilience. It runs in CI with coverage and smoke gates, and four planted defects are documented.<br><br><sub><code>TypeScript</code> <code>Playwright</code> <code>Pact</code> <code>k6</code> <code>OWASP ZAP</code> <code>Toxiproxy</code></sub></td><td width="50%" valign="top"><b><a href="https://github.com/Naysrania18/issue-tracker-quality-lab">issue-tracker-quality-lab</a></b><br><a href="https://github.com/Naysrania18/issue-tracker-quality-lab/actions/workflows/ci.yml"><img src="https://github.com/Naysrania18/issue-tracker-quality-lab/actions/workflows/ci.yml/badge.svg" alt="CI status for issue-tracker-quality-lab"></a> <code>MIT</code><br><br>A demo issue tracker with 210+ Python tests, 66 Java tests, Swift XCTest and Selenium browser tests. It adds an MCP server and a human-reviewed AI triage agent.<br><br><sub><code>Python</code> <code>Java</code> <code>Swift</code> <code>pytest</code> <code>TestNG</code> <code>Jenkins</code></sub></td></tr>
<tr><td width="50%" valign="top"><b><a href="https://github.com/Naysrania18/llm-vuln-triage">llm-vuln-triage</a></b><br><a href="https://github.com/Naysrania18/llm-vuln-triage/actions/workflows/ci.yml"><img src="https://github.com/Naysrania18/llm-vuln-triage/actions/workflows/ci.yml/badge.svg" alt="CI status for llm-vuln-triage"></a> <code>MIT</code><br><br>A CLI that triages Bandit and Semgrep findings with an LLM and checks every claim against the real code to flag hallucinations. It is evaluated on 22 labelled findings and reports SARIF.<br><br><sub><code>Python</code> <code>Bandit</code> <code>Semgrep</code> <code>SARIF</code></sub></td><td width="50%" valign="top"><b><a href="https://github.com/Naysrania18/api-security-toolkit">api-security-toolkit</a></b><br><a href="https://github.com/Naysrania18/api-security-toolkit/actions/workflows/ci.yml"><img src="https://github.com/Naysrania18/api-security-toolkit/actions/workflows/ci.yml/badge.svg" alt="CI status for api-security-toolkit"></a> <code>MIT</code><br><br>Reads an OpenAPI spec and checks a live API for BOLA, broken authentication, data exposure and injection. It refuses to run without an explicit authorization flag and writes JSON, Markdown and SARIF reports.<br><br><sub><code>Python</code> <code>OWASP API Top 10</code> <code>SARIF</code> <code>GitHub Actions</code></sub></td></tr>
</table>

<details>
<summary>More projects</summary>

<table>
<tr><td><a href="https://github.com/Naysrania18/SDET-framework">SDET-framework</a></td><td>One Python framework across API, UI, database and ETL tests with BDD and CI.</td></tr>
<tr><td><a href="https://github.com/Naysrania18/fund-etl-testing">fund-etl-testing</a></td><td>Data-quality and reconciliation tests for a financial ETL pipeline.</td></tr>
<tr><td><a href="https://github.com/Naysrania18/ai-test-generator">ai-test-generator</a></td><td>CLI that analyzes Python code and user stories to generate pytest cases.</td></tr>
<tr><td><a href="https://github.com/Naysrania18/iOS-Localization-UI-Test-Automation">iOS-Localization-UI-Test-Automation</a></td><td>SwiftUI localization demo with XCUITests and LLM translation review tools.</td></tr>
<tr><td><a href="https://github.com/Naysrania18/BSCP-2026">BSCP-2026</a></td><td>Solved web security labs with written walkthroughs, from Burp Suite Certified Practitioner preparation.</td></tr>
</table>

</details>

## Stack

<p align="center"><a href="#stack"><img src="assets/stack.svg?v=5" alt="Tech stack: Python, TypeScript, Java, Swift, SQL; pytest, Playwright, Selenium, Next.js, FastAPI; GitHub Actions, Jenkins, Docker, Cloudflare; Burp Suite, OWASP ZAP, Postman" width="100%"></a></p>

<p align="center"><img src="assets/languages.svg?v=5" alt="Public repositories by primary language: Python 79%, TypeScript 14%, HTML 7%" width="100%"></p>

<!-- Recognition and Certifications omitted: no verified entries. TODO(owner): add from LinkedIn. -->

## Education

M.Sc. Cybersecurity, Atlantic Technological University, Ireland
<!-- TODO(owner): confirm status and year. -->

## GitHub stats

<p align="center">
  <img src="assets/github-stats-dark.svg?v=5#gh-dark-mode-only" alt="GitHub stats: contributions in the last 12 months, public repositories, pull requests" width="100%">
  <img src="assets/github-stats-light.svg?v=5#gh-light-mode-only" alt="GitHub stats: contributions in the last 12 months, public repositories, pull requests" width="100%">
</p>

<p align="center">
  <img src="assets/activity-dark.svg?v=5#gh-dark-mode-only" alt="Contribution graph, last 12 months" width="100%">
  <img src="assets/activity-light.svg?v=5#gh-light-mode-only" alt="Contribution graph, last 12 months" width="100%">
</p>
