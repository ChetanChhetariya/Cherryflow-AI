# 🍒 Cherryflow-AI

<div align="center">

**AI-Powered B2B & B2C Brand Growth Platform Using Autonomous Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange.svg)](https://www.anthropic.com/)
[![Status: Active](https://img.shields.io/badge/Status-Active%20Development-green.svg)]()

> *"Let Intelligence Flow"* — Where AI Automation Meets Brand Excellence

</div>

---

## 🚀 What is Cherryflow-AI?

**Cherryflow-AI** is an open-source agentic AI platform that helps brands grow faster and generate more profit — automatically. It combines multiple AI agents powered by **Claude (Anthropic)** to handle everything from lead generation and content creation to customer support and analytics reporting.

Whether you're a B2B company targeting enterprise clients or a B2C brand engaging millions of customers, Cherryflow-AI provides a complete suite of autonomous agents that work 24/7 on your behalf.

---

## 🎯 Core Features

### 🤖 Autonomous AI Agents
- **B2B Lead Generation Agent** — Automatically finds, qualifies, and tracks potential business clients
- **B2C Customer Engagement Agent** — Personalizes interactions with end consumers at scale
- **Content Creation Agent** — Generates daily social media posts, blogs, and ad copy
- **Customer Support Agent** — 24/7 AI-powered responses to customer queries
- **SEO Content Agent** — Produces search-optimized content to improve brand visibility
- **Outreach Email Agent** — Writes and sends personalized cold outreach emails
- **Competitor Analysis Agent** — Monitors competitor activity and surfaces actionable insights
- **Analytics & Reporting Agent** — Generates weekly performance summaries and growth reports

### ⚙️ Automation Workflows
- Brand onboarding pipeline
- Daily content scheduling
- Weekly growth reporting
- Lead nurturing sequences
- Review monitoring & response

### 🔌 Integrations
- Anthropic Claude API (core AI engine)
- Gmail / SMTP (email automation)
- Twitter / LinkedIn / Instagram APIs (social media)
- Google Analytics (performance tracking)
- Slack (team notifications)
- Webhooks (custom integrations)

---

## 🏗️ Project Structure

```
Cherryflow-AI/
│
├── agents/
│   ├── b2b_agent.py            # B2B lead generation & outreach agent
│   ├── b2c_agent.py            # B2C customer engagement agent
│   ├── content_agent.py        # Social media & blog content agent
│   ├── support_agent.py        # 24/7 customer support agent
│   ├── seo_agent.py            # SEO content optimization agent
│   ├── competitor_agent.py     # Competitor monitoring agent
│   └── analytics_agent.py     # Growth analytics & reporting agent
│
├── tools/
│   ├── lead_generator.py       # Lead scraping & qualification tools
│   ├── email_writer.py         # Personalized email generation
│   ├── competitor_tracker.py   # Competitor data tracking
│   ├── ad_copy_generator.py    # High-converting ad copy tool
│   └── analytics_parser.py    # Analytics data processing
│
├── workflows/
│   ├── brand_onboarding.py     # New brand setup workflow
│   ├── daily_content.py        # Automated daily content pipeline
│   ├── weekly_report.py        # Weekly growth report generation
│   └── lead_pipeline.py        # End-to-end lead nurturing flow
│
├── api/
│   ├── routes/                 # API route definitions
│   ├── middleware/             # Auth & request middleware
│   ├── auth/                   # Authentication logic
│   └── webhooks/               # Incoming webhook handlers
│
├── config/
│   ├── claude_config.py        # Claude API configuration
│   ├── prompts/                # Agent system prompts
│   ├── agent_personas.py       # Agent personality definitions
│   └── model_settings.py      # Model parameters & tuning
│
├── frontend/
│   ├── dashboard/              # Brand dashboard UI
│   ├── components/             # Reusable UI components
│   └── pages/                  # Application pages
│
├── docs/
│   ├── architecture.md         # System architecture overview
│   ├── API_reference.md        # Full API documentation
│   ├── agent_guide.md          # How to use each agent
│   └── setup_guide.md          # Installation & setup guide
│
├── tests/
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── agent_tests/            # Agent behavior tests
│
├── .env.example                # Environment variables template
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
└── README.md                   # You are here
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- An [Anthropic API Key](https://console.anthropic.com/)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ChetanChhetariya/Cherryflow-AI.git
cd Cherryflow-AI

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your ANTHROPIC_API_KEY to the .env file

# 5. Run your first agent
python agents/content_agent.py
```

### Environment Variables

```env
ANTHROPIC_API_KEY=your_claude_api_key_here
CLAUDE_MODEL=claude-sonnet-4-20250514

# Optional integrations
GMAIL_API_KEY=your_gmail_key
TWITTER_API_KEY=your_twitter_key
SLACK_WEBHOOK_URL=your_slack_webhook
```

---

## 🧠 How It Works

```
Brand Input
    │
    ▼
┌─────────────────────────────┐
│     Cherryflow Orchestrator │  ← Routes tasks to the right agent
└─────────────────────────────┘
    │           │           │
    ▼           ▼           ▼
B2B Agent   Content     Support
(Leads)     Agent       Agent
    │       (Posts)     (Replies)
    │           │           │
    └───────────┴───────────┘
                │
                ▼
        Analytics Agent
        (Weekly Reports)
                │
                ▼
        Brand Dashboard
```

Each agent is powered by **Claude AI** with a specialized system prompt and toolset. Agents can work independently or as part of an automated workflow pipeline.

---

## 🤖 Agent Examples

### Content Agent
```python
from agents.content_agent import ContentAgent

agent = ContentAgent(brand_name="Nike", tone="energetic", platforms=["instagram", "twitter"])
posts = agent.generate_weekly_content()
agent.schedule_posts(posts)
```

### B2B Lead Agent
```python
from agents.b2b_agent import B2BLeadAgent

agent = B2BLeadAgent(target_industry="SaaS", company_size="50-200")
leads = agent.find_leads(location="USA", limit=50)
agent.send_outreach(leads)
```

### Support Agent
```python
from agents.support_agent import SupportAgent

agent = SupportAgent(brand_name="YourBrand", tone="friendly")
agent.listen_and_respond(channel="email")  # Runs 24/7
```

---

## 🗺️ Roadmap

- [x] Project structure & architecture
- [ ] Core agent framework with Claude integration
- [ ] B2B Lead Generation Agent (v1)
- [ ] Content Creation Agent (v1)
- [ ] Customer Support Agent (v1)
- [ ] Brand Dashboard (UI)
- [ ] Multi-brand support
- [ ] Agent-to-agent communication
- [ ] Analytics & reporting module
- [ ] SaaS platform launch

---

## 🤝 Contributing

Contributions are welcome! Cherryflow-AI is an open-source project and we'd love your help.

```bash
# Fork the repo, then:
git checkout -b feature/your-agent-name
git commit -m "Add: your feature description"
git push origin feature/your-agent-name
# Open a Pull Request
```

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) before submitting PRs.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Chetan Chhetariya**
- GitHub: [@ChetanChhetariya](https://github.com/ChetanChhetariya)
- Project: [Cherryflow-AI](https://github.com/ChetanChhetariya/Cherryflow-AI)

---

## ⭐ Support

If you find this project useful, please consider giving it a **star** ⭐ on GitHub — it helps a lot!

---

<div align="center">
Built with ❤️ using <a href="https://www.anthropic.com/">Claude AI by Anthropic</a>
<br/>
<i>"Flow Smarter. Grow Faster."</i>
</div>
