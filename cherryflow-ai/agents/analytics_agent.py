"""
Cherryflow-AI — Analytics & Reporting Agent
Generates weekly growth reports and surfaces actionable insights.
"""

from agents.base_agent import BaseAgent


ANALYTICS_SYSTEM_PROMPT = """
You are Cherryflow's Analytics & Reporting Agent — a data-driven growth analyst AI.

Your responsibilities:
- Analyze brand performance metrics
- Generate weekly and monthly growth reports
- Identify trends, anomalies, and opportunities
- Provide ROI analysis on marketing activities
- Suggest data-driven optimization strategies

Always translate raw numbers into clear insights.
Use plain language — avoid jargon unless asked.
Every report must end with 3 clear action items.
"""


class AnalyticsAgent(BaseAgent):
    def __init__(self, brand_name: str):
        super().__init__(
            agent_name="Analytics Agent",
            system_prompt=ANALYTICS_SYSTEM_PROMPT
        )
        self.brand_name = brand_name

    def generate_weekly_report(self, metrics: dict) -> str:
        """Generate a comprehensive weekly growth report."""
        self.log("Generating weekly growth report...")
        metrics_text = "\n".join([f"- {k}: {v}" for k, v in metrics.items()])
        prompt = f"""
        Generate a weekly growth report for "{self.brand_name}":

        This Week's Metrics:
        {metrics_text}

        Report must include:
        1. Executive Summary (3-4 sentences)
        2. Performance vs Last Week (% change per metric)
        3. Top Wins This Week
        4. Areas of Concern
        5. Channel-by-Channel Breakdown
        6. Trend Analysis
        7. Next Week's Focus Areas
        8. Top 3 Action Items (specific and measurable)

        Format clearly with headers and bullet points.
        """
        return self.chat(prompt)

    def analyze_campaign(self, campaign_name: str, campaign_data: dict) -> str:
        """Analyze the performance of a specific campaign."""
        self.log(f"Analyzing campaign: {campaign_name}")
        data_text = "\n".join([f"- {k}: {v}" for k, v in campaign_data.items()])
        prompt = f"""
        Analyze this marketing campaign for "{self.brand_name}":

        Campaign: {campaign_name}
        Data:
        {data_text}

        Provide:
        1. Overall Campaign Score (X/10)
        2. ROI Analysis
        3. Best Performing Element
        4. Weakest Element
        5. Audience Insights
        6. Optimization Recommendations for next run
        7. Should we scale this campaign? (Yes/No + reasoning)
        """
        return self.chat(prompt)

    def growth_forecast(self, current_metrics: dict, target: str) -> str:
        """Forecast growth trajectory based on current performance."""
        self.log("Building growth forecast...")
        metrics_text = "\n".join([f"- {k}: {v}" for k, v in current_metrics.items()])
        prompt = f"""
        Create a growth forecast for "{self.brand_name}":

        Current Performance:
        {metrics_text}

        Target: {target}

        Forecast:
        1. 30-day projection (realistic / optimistic / conservative)
        2. 90-day projection
        3. Key milestones to hit
        4. Biggest risks to growth
        5. Growth levers to pull (ranked by impact)
        6. Resources needed to hit targets
        """
        return self.chat(prompt)

    def competitor_benchmark(self, our_metrics: dict, competitor_name: str) -> str:
        """Benchmark our performance vs a competitor."""
        self.log(f"Benchmarking vs: {competitor_name}")
        metrics_text = "\n".join([f"- {k}: {v}" for k, v in our_metrics.items()])
        prompt = f"""
        Benchmark "{self.brand_name}" vs "{competitor_name}":

        Our Current Metrics:
        {metrics_text}

        Based on typical industry benchmarks for {competitor_name}'s space:
        1. Where we're ahead
        2. Where we're behind
        3. Biggest gap to close
        4. Quick wins to close the gap
        5. Long-term strategy to outperform them
        """
        return self.chat(prompt)


if __name__ == "__main__":
    agent = AnalyticsAgent(brand_name="Cherryflow AI")

    print("=== ANALYTICS AGENT DEMO ===\n")

    sample_metrics = {
        "Website Visitors": "12,450 (+18%)",
        "New Sign-ups": "342 (+24%)",
        "Revenue": "$8,900 (+11%)",
        "Email Open Rate": "28.4%",
        "Social Media Reach": "45,000 (+32%)",
        "Customer Churn": "3.2% (-0.5%)",
        "Support Tickets": "89 (-12%)",
        "NPS Score": "67"
    }

    print("--- Weekly Growth Report ---")
    report = agent.generate_weekly_report(sample_metrics)
    print(report)
