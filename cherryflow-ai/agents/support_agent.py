"""
Cherryflow-AI — Customer Support Agent
Handles customer queries 24/7 with brand-specific tone and knowledge.
"""

from agents.base_agent import BaseAgent


SUPPORT_SYSTEM_PROMPT = """
You are Cherryflow's Customer Support Agent — a friendly, empathetic, and highly efficient support AI.

Your responsibilities:
- Answer customer questions accurately and quickly
- Resolve complaints with empathy and solutions
- Escalate complex issues when needed
- Maintain the brand's tone in every response
- Collect feedback and identify common pain points

Rules:
- Always greet the customer by name if provided
- Acknowledge their frustration before solving
- Never argue or be defensive
- Offer a solution OR a clear next step in every response
- End with a check: "Is there anything else I can help you with?"
"""


class SupportAgent(BaseAgent):
    def __init__(self, brand_name: str, tone: str = "friendly", faq_data: dict = None):
        super().__init__(
            agent_name="Support Agent",
            system_prompt=SUPPORT_SYSTEM_PROMPT
        )
        self.brand_name = brand_name
        self.tone = tone
        self.faq_data = faq_data or {}

    def respond_to_query(self, customer_name: str, query: str) -> str:
        """Respond to a customer support query."""
        self.log(f"Handling query from: {customer_name}")
        prompt = f"""
        You are the support agent for "{self.brand_name}". Tone: {self.tone}.

        Customer Name: {customer_name}
        Customer Query: {query}

        Provide a helpful, empathetic, and complete response.
        If you need more info, ask one specific question.
        """
        return self.chat(prompt)

    def handle_complaint(self, customer_name: str, complaint: str, order_id: str = None) -> str:
        """Handle a customer complaint with empathy."""
        self.log(f"Handling complaint from: {customer_name}")
        prompt = f"""
        Handle this customer complaint for "{self.brand_name}":

        Customer: {customer_name}
        Order ID: {order_id or 'Not provided'}
        Complaint: {complaint}

        Response must:
        1. Acknowledge the issue sincerely
        2. Apologize (if brand is at fault)
        3. Provide a concrete resolution
        4. Offer compensation if appropriate (discount / refund / replacement)
        5. Set a timeline for resolution
        6. Close warmly

        Tone: {self.tone} but professional.
        """
        return self.chat(prompt)

    def generate_faq(self, product_or_service: str, num_questions: int = 10) -> str:
        """Generate FAQ document for a product or service."""
        self.log(f"Generating FAQ for: {product_or_service}")
        prompt = f"""
        Create {num_questions} frequently asked questions (FAQ) for:

        Brand: {self.brand_name}
        Product/Service: {product_or_service}

        For each FAQ:
        - Question (realistic, what customers actually ask)
        - Answer (clear, concise, 2-4 sentences max)

        Group them into categories:
        - General Questions
        - Pricing & Plans
        - Technical Support
        - Refunds & Cancellations
        """
        return self.chat(prompt)

    def analyze_feedback(self, feedback_list: list) -> str:
        """Analyze customer feedback and surface insights."""
        self.log("Analyzing customer feedback...")
        feedback_text = "\n".join([f"- {fb}" for fb in feedback_list])
        prompt = f"""
        Analyze this customer feedback for "{self.brand_name}":

        {feedback_text}

        Provide:
        1. Overall sentiment (Positive / Neutral / Negative %)
        2. Top 3 things customers love
        3. Top 3 pain points / complaints
        4. Actionable improvement suggestions
        5. Priority fix recommendations (High / Medium / Low)
        """
        return self.chat(prompt)

    def draft_review_response(self, review: str, rating: int, platform: str = "Google") -> str:
        """Draft a response to a public customer review."""
        self.log(f"Drafting response to {rating}-star {platform} review...")
        sentiment = "positive" if rating >= 4 else "negative" if rating <= 2 else "neutral"
        prompt = f"""
        Write a response to this {platform} review for "{self.brand_name}":

        Rating: {rating}/5 stars ({sentiment})
        Review: {review}

        Response must:
        - Be under 100 words
        - Match tone to rating (grateful for positive, empathetic for negative)
        - Include brand name naturally
        - For negative: offer to resolve offline (provide contact)
        - For positive: reinforce what they loved
        """
        return self.chat(prompt)


if __name__ == "__main__":
    agent = SupportAgent(
        brand_name="Cherryflow AI",
        tone="warm and professional"
    )

    print("=== SUPPORT AGENT DEMO ===\n")

    print("--- Handling Customer Query ---")
    response = agent.respond_to_query(
        customer_name="Priya",
        query="I signed up yesterday but I can't find where to connect my Instagram account. Help!"
    )
    print(response)

    print("\n--- Handling Complaint ---")
    agent.reset_conversation()
    complaint_response = agent.handle_complaint(
        customer_name="Raj",
        complaint="Your content agent posted something completely wrong on my brand's LinkedIn. This is embarrassing!",
        order_id="CF-2024-0892"
    )
    print(complaint_response)
