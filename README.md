# AI Newsletter Project

## Overview
The **AI Newsletter Project** automates the creation of AI newsletters by leveraging a structured workflow of agents and tasks. It fetches, analyzes, and compiles AI-related news into a markdown-formatted newsletter. The project uses virtual agents to ensure the process is efficient and consistent.

---

## Workflow Summary
The workflow is orchestrated in `main.py`, which:
1. Initializes the agents and tasks.
2. Executes the tasks sequentially:
   - **Fetch News Task**: Gathers the latest AI news.
   - **Analyze News Task**: Summarizes and formats the news.
   - **Compile Newsletter Task**: Compiles the summaries into a markdown file.
3. Saves the generated newsletter using a custom `save_markdown` function.

---

## Agents
- **Editor**: Ensures the newsletter is engaging and consistent.
- **NewsFetcher**: Fetches the latest AI news using DuckDuckGo.
- **NewsAnalyzer**: Analyzes and distills news into key insights.
- **NewsletterCompiler**: Combines the analyzed data into a cohesive newsletter format.

---

## Tasks
1. **Fetch News Task**:
   - Retrieves top AI news articles, including titles, URLs, and summaries.
2. **Analyze News Task**:
   - Summarizes each article with key points and a "Why it matters" section.
3. **Compile Newsletter Task**:
   - Produces a complete markdown-formatted newsletter ready for distribution.
