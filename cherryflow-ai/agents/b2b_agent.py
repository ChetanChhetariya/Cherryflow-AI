"""
Cherryflow-AI — B2B Lead Generation Agent
Finds, qualifies, and tracks potential business clients automatically.
"""

from agents.base_agent import BaseAgent


B2B_SYSTEM_PROMPT = """
You are Cherryflow's B2B Lead Generation Agent — an expert business development AI.

Your responsibilities:
- Identify high-quality business leads based on target criteria
- Write personalized, compelling outreach emails
- Qualify leads by analyzing their business fit
- Generate sales proposals tailored to each prospect
- Suggest follow-up strategies

Always be professional, data-driven, and focused on value delivery.
Format all outputs clearly with sections and bullet points.
"""


class B2BLeadAgent(BaseAgent):
    def __init__(self, brand_name: str, target_industry: str, company_size: str = "10-500"):
        super().__init__(
            agent_name="B2B Lead Agent",
            system_prompt=B2B_SYSTEM_PROMPT
        )
        self.brand_name = brand_name
        self.target_industry = target_industry
        self.company_size = company_size

    def find_leads(self, location: str = "Global", limit: int = 10) -> str:
        """Generate a list of ideal lead profiles."""
        self.log(f"Finding leads in {self.target_industry} industry...")
        prompt = f"""
        Generate {limit} detailed ideal customer profiles (ICPs) for a B2B brand called "{self.brand_name}".

        Target Criteria:
        - Industry: {self.target_industry}
        - Company size: {self.company_size} employees
        - Location: {location}

        For each lead profile include:
        1. Company type & description
        2. Decision maker title (who to contact)
        3. Pain points they likely have
        4. Why they would need our services
        5. Best outreach channel (email/LinkedIn/call)

        Make them realistic and specific.
        """
        return self.chat(prompt)

    def write_outreach_email(self, company_name: str, pain_point: str) -> str:
        """Write a personalized cold outreach email."""
        self.log(f"Writing outreach email for {company_name}...")
        prompt = f"""
        Write a highly personalized cold outreach email for:

        - Our Brand: {self.brand_name}
        - Target Company: {company_name}
        - Their Pain Point: {pain_point}

        Requirements:
        - Subject line that gets opened (A/B test 2 versions)
        - Max 150 words in body
        - One clear CTA (call to action)
        - Human, not salesy tone
        - End with a soft ask (15-min call)

        Format: Subject Line / Email Body / PS line
        """
        return self.chat(prompt)

    def generate_proposal(self, company_name: str, requirements: str) -> str:
        """Generate a business proposal for a prospect."""
        self.log(f"Generating proposal for {company_name}...")
        prompt = f"""
        Create a professional B2B sales proposal for:

        - Our Brand: {self.brand_name}
        - Client: {company_name}
        - Their Requirements: {requirements}

        Include:
        1. Executive Summary
        2. Problem Statement
        3. Our Solution
        4. Deliverables & Timeline
        5. Pricing Tiers (Basic / Pro / Enterprise)
        6. Why Choose Us
        7. Next Steps

        Keep it persuasive, clear, and results-focused.
        """
        return self.chat(prompt)

    def qualify_lead(self, company_info: str) -> str:
        """Assess if a lead is worth pursuing."""
        self.log("Qualifying lead...")
        prompt = f"""
        Analyze this company and give a lead qualification score:

        Company Info: {company_info}
        Our Target: {self.target_industry} companies with {self.company_size} employees

        Provide:
        - Score: X/10
        - Fit Analysis (budget, authority, need, timeline — BANT)
        - Recommendation: Pursue / Nurture / Skip
        - Suggested approach if pursuing
        """
        return self.chat(prompt)


if __name__ == "__main__":
    agent = B2BLeadAgent(
        brand_name="Cherryflow AI",
        target_industry="E-commerce & Retail",
        company_size="20-300"
    )

    print("=== B2B LEAD AGENT DEMO ===\n")

    print("--- Finding Leads ---")
    leads = agent.find_leads(location="India & USA", limit=3)
    print(leads)

    print("\n--- Writing Outreach Email ---")
    agent.reset_conversation()
    email = agent.write_outreach_email(
        company_name="ShopNow India",
        pain_point="Struggling to scale customer acquisition without increasing ad spend"
    )
    print(email)
