# AI-Driven Communication Management MVP

This repository contains an MVP solution for Superteam Vietnam's communication management challenges. Our system automates and augments content creation, community inquiries, and social media management using AI-powered modules. All AI inference is handled locally to ensure data privacy.

## Overview

The MVP is comprised of the following modules:

- **Telegram Knowledge Portal Bot:**  
  A Telegram bot that serves as a knowledge base. It retrieves document contexts using a RAG (Retrieval-Augmented Generation) approach and uses a local LLM to generate accurate responses. If no relevant context is found, it responds with "NO".

- **Superteam Member Finder:**  
  A module that uses a JSON database of Superteam members to match queries (e.g., "I want to find a RUST developer for a DEFI project") with the most suitable team member(s). It provides clear explanations for the matches or returns "NO" if no suitable match exists.

- **Twitter Management Assistant:**  
  An assistant that integrates with the Twitter API to propose tweet drafts, refine content through iterative suggestions, and manage publishing. It checks and corrects Twitter handles against a pre-approved list.

- **Content Advisor:**  
  A collaborative tool that assists in creating and refining content for both Telegram and Twitter, ensuring the output aligns with brand tone and style.

## Architecture

- **Modular Microservices:**  
  Each feature is developed as an independent module for ease of maintenance and scalability.
  
- **Local LLM Integration:**  
  The local LLM handles all AI tasks to maintain strict data privacy. This means sensitive data remains on-premise.

- **API Integrations:**  
  The system integrates with Telegram and Twitter APIs to manage communications and social media workflows seamlessly.

## Repository Structure
mvp_project/ ├── main.py # Main entry point to run the MVP ├── members.json # Sample JSON database for Superteam members ├── local_llm/ │ └── llm.py # Local LLM module (placeholder for actual integration) ├── telegram_bot/ │ ├── bot.py # Telegram bot logic and handlers │ └── doc_processing.py # Document processing and retrieval logic ├── member_finder/ │ └── finder.py # Superteam Member Finder module ├── twitter_assistant/ │ └── twitter_manager.py # Twitter assistant module └── content_advisor/ └── advisor.py # Content advisor module


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python libraries (see `requirements.txt` if available)
- Valid API credentials:
  - Telegram Bot Token
  - Twitter API Key, API Secret, Access Token, and Access Token Secret

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ai-communication-mvp.git
   cd ai-communication-mvp

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Configure your credentials:**
   
   Update the placeholder credentials in:
   
    - telegram_bot/bot.py for the Telegram Bot.
   
    - twitter_assistant/twitter_manager.py for Twitter API access.

### Running the MVP
Run the main entry point to start all modules:

   ```bash
   python main.py

- The Telegram bot will start polling for messages.
- Example invocations for the Member Finder, Twitter Assistant, and Content Advisor will be executed.

### Usage

- Telegram Bot:
Start a chat with your bot on Telegram and send any query related to your documents.

- Member Finder:
Test member matching by running queries from the command line (see finder.py).

- Twitter Assistant:
Generate and publish tweets via the integrated Twitter API.

- Content Advisor:
Get content improvement suggestions by interacting with the advisor module.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
