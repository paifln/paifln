<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/wordmark-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/wordmark-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/wordmark-dark.svg">
  <img src="assets/wordmark.svg" alt="Alibi Kabessov — Software Developer" width="800">
</picture>

### I build products, tools and the systems behind them.

**Software Developer · Computer Science Educator**

I take ideas from interface to infrastructure: React applications, Python APIs, background workers and Docker deployments. I build practical tools for real users and explore ideas through personal projects.

[Selected Work](#selected-work) &nbsp; / &nbsp; [Technical Stack](#technical-stack) &nbsp; / &nbsp; [Engineering Approach](#engineering-approach) &nbsp; / &nbsp; [Contact](#contact)

## Selected Work

### <img src="assets/icons/code.svg" width="26" height="26" alt=""> &nbsp; CodeArena

**From a classroom network to a complete programming contest.**

Built a self-hosted platform where educators create problems, organize individual or team contests, and track live standings. Students write and submit solutions directly in the browser.

- **Execution engine:** automatic judging in isolated Docker containers, with support for six programming languages.
- **Contest operations:** scoring, frozen standings and reveal, clarifications, rejudging, and teacher-controlled participation.
- **Complete product:** React interface with Monaco Editor, role-based access, database migrations, backups, and English, Russian and Kazakh localization.

`Python` `FastAPI` `React` `TypeScript` `SQLite` `SQLAlchemy` `Docker`

<a href="https://github.com/paifln/codeArena"><strong>Explore CodeArena</strong> <img src="assets/icons/arrow-up-right.svg" width="16" height="16" alt=""></a> &nbsp; / &nbsp; <a href="https://github.com/paifln/codeArena/tree/main/backend/judge">Judging engine</a>

<p><img src="assets/divider.svg" width="100%" height="1" alt=""></p>

### <img src="assets/icons/document.svg" width="26" height="26" alt=""> &nbsp; DOCUMENTOR

**Academic document review, developed for a university.**

Built for **Makhambet Utemisov West Kazakhstan University** to help review student papers. A Telegram interface turns a DOCX submission into a structured PDF report covering formatting, document structure, language and academic style.

- **Document processing:** extracts DOCX content, checks formatting against configurable rules, and generates reports with actionable feedback.
- **AI integration:** combines deterministic checks with AI-assisted analysis; incomplete analysis is explicitly reported.
- **Asynchronous architecture:** PostgreSQL stores review jobs, Redis queues background work, and delivery retries do not rerun the analysis. Supports English, Russian and Kazakh.

`Python` `aiogram` `PostgreSQL` `Redis` `ARQ` `python-docx` `ReportLab` `Docker`

<a href="https://github.com/paifln/documentor_bot"><strong>Explore DOCUMENTOR</strong> <img src="assets/icons/arrow-up-right.svg" width="16" height="16" alt=""></a> &nbsp; / &nbsp; <a href="https://github.com/paifln/documentor_bot/blob/main/docs/ARCHITECTURE.md">Architecture</a>

## Technical Stack

My toolkit for applications, automation and hands-on experimentation.

| Area | Technologies |
| :--- | :--- |
| <img src="assets/icons/code.svg" width="20" height="20" alt=""> **Languages** | `Python` `TypeScript` `JavaScript` `Luau` |
| <img src="assets/icons/window.svg" width="20" height="20" alt=""> **Frontend** | `React` `HTML` `CSS` `Tailwind CSS` `Vite` `TanStack Query` `Zustand` `i18next` `Monaco Editor` |
| <img src="assets/icons/server.svg" width="20" height="20" alt=""> **Backend** | `FastAPI` `Pydantic` `aiogram` `SQLAlchemy` `Alembic` `ARQ` |
| <img src="assets/icons/database.svg" width="20" height="20" alt=""> **Data** | `PostgreSQL` `SQLite` `Redis` |
| <img src="assets/icons/document.svg" width="20" height="20" alt=""> **Documents & AI** | `python-docx` `ReportLab` `lxml` `OpenAI SDK` `HTTPX` |
| <img src="assets/icons/workflow.svg" width="20" height="20" alt=""> **Delivery** | `Git` `GitHub Actions` `Docker` `Docker Compose` |
| <img src="assets/icons/check.svg" width="20" height="20" alt=""> **Quality** | `pytest` `Vitest` `Testing Library` `Ruff` `Prettier` |
| <img src="assets/icons/chip.svg" width="20" height="20" alt=""> **Hardware** | `Arduino` `ESP32` |

## Engineering Approach

<img src="assets/icons/workflow.svg" width="20" height="20" alt=""> **Build the whole workflow.** Connect the interface, API, data model and background processing around the task a user needs to complete.

<img src="assets/icons/check.svg" width="20" height="20" alt=""> **Design for failure and recovery.** Isolate code execution, retry document delivery, preserve review state, and provide backup and recovery paths.

<img src="assets/icons/code.svg" width="20" height="20" alt=""> **Make complex tools usable.** Teaching computer science informs how I structure interfaces, explain results and build software for people with different technical backgrounds.

**Current interests:** algorithms, backend engineering, system design, developer tools and robotics.

## Contact

<img src="assets/icons/briefcase.svg" width="22" height="22" alt=""> **Let's talk about software engineering opportunities.**

Open to software engineering roles, product teams and collaboration on useful tools.

<p>
  <a href="mailto:kabessovalibi007@gmail.com"><img src="assets/icons/mail.svg" width="20" height="20" alt=""> <strong>Email</strong></a>
  &nbsp; / &nbsp;
  <a href="https://www.linkedin.com/in/alibi-kabessov-60b97b43a/"><img src="assets/icons/linkedin.svg" width="20" height="20" alt=""> <strong>LinkedIn</strong></a>
  &nbsp; / &nbsp;
  <a href="https://github.com/paifln"><img src="assets/icons/code.svg" width="20" height="20" alt=""> <strong>GitHub</strong></a>
</p>
