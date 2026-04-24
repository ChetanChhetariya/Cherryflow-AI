"""
Cherryflow-AI — Main Orchestrator
Routes tasks to the right agent and runs automated workflows.
"""

from agents.b2b_agent import B2BLeadAgent
from agents.content_agent import ContentAgent
from agents.support_agent import SupportAgent
from agents.seo_agent import SEOAgent
from agents.analytics_agent import AnalyticsAgent


class CherryflowOrchestrator:
    """
    Central controller for all Cherryflow AI agents.
    Manages agent selection and multi-agent workflows.
    """

    def __init__(self, brand_name: str, industry: str, tone: str = "professional"):
        self.brand_name = brand_name
        self.industry = industry
        self.tone = tone

        # Initialize all agents
        self.b2b = B2BLeadAgent(brand_name, industry)
        self.content = ContentAgent(brand_name, tone, industry)
        self.support = SupportAgent(brand_name, tone)
        self.seo = SEOAgent(brand_name, niche=industry)
        self.analytics = AnalyticsAgent(brand_name)

        print(f"🍒 Cherryflow-AI Orchestrator initialized for: {brand_name}")
        print(f"   Industry: {industry} | Tone: {tone}")
        print(f"   Agents loaded: B2B, Content, Support, SEO, Analytics\n")

    def run_daily_workflow(self, topic: str):
        """Run the daily automated content workflow."""
        print("⚡ Running Daily Workflow...\n")

        print("📝 Step 1: Generating daily content...")
        content = self.content.generate_social_posts(topic)
        print(content)

        print("\n🔍 Step 2: SEO keyword check...")
        keywords = self.seo.keyword_research(topic, num_keywords=5)
        print(keywords)

        return {"content": content, "keywords": keywords}

    def run_lead_generation(self, target: str, location: str = "Global"):
        """Run B2B lead generation workflow."""
        print("🎯 Running Lead Generation Workflow...\n")

        print("🔎 Finding leads...")
        leads = self.b2b.find_leads(location=location, limit=5)
        print(leads)
        return leads

    def run_weekly_report(self, metrics: dict):
        """Generate the weekly analytics report."""
        print("📊 Running Weekly Report Workflow...\n")
        report = self.analytics.generate_weekly_report(metrics)
        print(report)
        return report


if __name__ == "__main__":
    # Initialize Cherryflow for a sample brand
    cherryflow = CherryflowOrchestrator(
        brand_name="Cherryflow AI",
        industry="AI & Marketing Automation",
        tone="bold and innovative"
    )

    # Run daily content workflow
    cherryflow.run_daily_workflow(
        topic="Why AI agents are the future of brand marketing"
    )
