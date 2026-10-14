<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/wordmark-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/wordmark-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/wordmark-dark.svg">
  <img src="assets/wordmark.svg" alt="Alibi Kabessov — Software Developer" width="800">
</picture>

### I build products, tools and the systems behind them.

**Software Developer · Computer Science Educator**

I take ideas from interface to infrastructure: React and Next.js applications, Python APIs, background workers, Electron desktop tools and Docker deployments. My projects span education, document workflows, personal music libraries and robotics.

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

<p><img src="assets/divider.svg" width="100%" height="1" alt=""></p>

### <img src="assets/icons/window.svg" width="26" height="26" alt=""> &nbsp; Noctune

**Your own music collection, with a player built around it.**

Built a private web application for uploading, organizing and listening to personal MP3 files, with a responsive desktop and mobile interface.

- **Library management:** multi-file uploads, ID3 metadata and embedded artwork, duplicate detection, search, album and artist grouping, playlists and liked songs.
- **Playback:** continuous audio across navigation, editable queue, shuffle and repeat, seeking, listening history and Media Session controls.
- **Private storage:** Supabase authentication, PostgreSQL row-level security, private audio and artwork buckets, signed playback URLs and direct-to-storage uploads.

`Next.js` `React` `TypeScript` `Tailwind CSS` `Supabase` `PostgreSQL` `Vercel`

<a href="https://github.com/paifln/noctune"><strong>Explore Noctune</strong> <img src="assets/icons/arrow-up-right.svg" width="16" height="16" alt=""></a> &nbsp; / &nbsp; <a href="https://github.com/paifln/noctune/blob/main/docs/DEPLOY_RU.md">Deployment guide</a>

<p><img src="assets/divider.svg" width="100%" height="1" alt=""></p>

### <img src="assets/icons/document.svg" width="26" height="26" alt=""> &nbsp; ZiyatAI

**From a teacher's curriculum plan to differentiated classroom assignments.**

Building a workspace for computer science teachers in Kazakhstan: import a calendar and thematic plan (KTP), review extracted lessons, confirm topics and learning objectives, and prepare assignments at three difficulty levels.

- **Teacher-led workflow:** review imported rows, edit assignment versions and export teaching materials as DOCX or PDF. The interface supports Kazakh and Russian, with separate language choices for source documents and assignments.
- **Document and AI pipeline:** Python document processing and a structured OpenAI provider, with long-running imports, generation and exports handled by a separate worker.
- **Durable jobs:** PostgreSQL-backed state, private S3-compatible file storage, job leases, heartbeats and recovery of interrupted work.

**Status:** verified locally; public production deployment and live AI validation are pending.

`Next.js` `React` `TypeScript` `Python` `PostgreSQL` `S3` `OpenAI SDK` `Docker`

<a href="https://github.com/paifln/ziyatai"><strong>Explore ZiyatAI</strong> <img src="assets/icons/arrow-up-right.svg" width="16" height="16" alt=""></a> &nbsp; / &nbsp; <a href="https://github.com/paifln/ziyatai/blob/main/docs/adr/001_architecture.md">Architecture</a>

<p><img src="assets/divider.svg" width="100%" height="1" alt=""></p>

### <img src="assets/icons/chip.svg" width="26" height="26" alt=""> &nbsp; JECTIVE Robotics Studio

**A desktop workspace for learning robotics through lessons, code and simulation.**

Developing a Windows application within the <a href="https://www.jective.kz/">JECTIVE</a> educational ecosystem, connecting interactive learning with Blockly programming, generated Arduino C++ and robot behavior scenarios.

- **Learning and creation:** interactive lessons, local narration, a Monaco code editor, multi-file projects, version history and recovery. Lessons, editing and simulation work without the online assistant.
- **Robotics workflow:** reproducible simulation scenarios and separate Arduino CLI compilation/upload tools. The simulator models robot behavior rather than executing arbitrary Arduino C++.
- **Application architecture:** React inside Electron, validated IPC contracts and separate domain services for files, simulation and hardware. An optional server-hosted AI assistant keeps the provider key off student devices.

**Status:** active development; full product acceptance and integration with the planned physical JECTIVE kit are pending.

`Electron` `React` `TypeScript` `Blockly` `Monaco Editor` `Arduino CLI` `ESP32`

<a href="https://github.com/paifln/jective_robotics"><strong>Explore JECTIVE Robotics Studio</strong> <img src="assets/icons/arrow-up-right.svg" width="16" height="16" alt=""></a> &nbsp; / &nbsp; <a href="https://github.com/paifln/jective_robotics/blob/main/docs/ARCHITECTURE.md">Architecture</a>

## Technical Stack

My toolkit for applications, automation and hands-on experimentation.

| Area | Technologies |
| :--- | :--- |
| <img src="assets/icons/code.svg" width="20" height="20" alt=""> **Languages** | `Python` `TypeScript` `JavaScript` `Luau` |
| <img src="assets/icons/window.svg" width="20" height="20" alt=""> **Frontend** | `React` `Next.js` `HTML` `CSS` `Tailwind CSS` `Vite` `TanStack Query` `Zustand` `i18next` `Monaco Editor` |
| <img src="assets/icons/chip.svg" width="20" height="20" alt=""> **Desktop & Robotics** | `Electron` `Blockly` `Arduino CLI` `SerialPort` |
| <img src="assets/icons/server.svg" width="20" height="20" alt=""> **Backend** | `FastAPI` `Pydantic` `aiogram` `SQLAlchemy` `Alembic` `ARQ` |
| <img src="assets/icons/database.svg" width="20" height="20" alt=""> **Data** | `PostgreSQL` `SQLite` `Redis` `Supabase` `S3` |
| <img src="assets/icons/document.svg" width="20" height="20" alt=""> **Documents & AI** | `python-docx` `ReportLab` `lxml` `OpenAI SDK` `HTTPX` |
| <img src="assets/icons/workflow.svg" width="20" height="20" alt=""> **Delivery** | `Git` `GitHub Actions` `Docker` `Docker Compose` `Vercel` |
| <img src="assets/icons/check.svg" width="20" height="20" alt=""> **Quality** | `pytest` `Vitest` `Playwright` `Testing Library` `Ruff` `ESLint` `Prettier` |
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
