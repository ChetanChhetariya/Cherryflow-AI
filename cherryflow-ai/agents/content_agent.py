"""
Cherryflow-AI — Content Creation Agent
Generates daily social media posts, blogs, ad copy, and brand content.
"""

from agents.base_agent import BaseAgent


CONTENT_SYSTEM_PROMPT = """
You are Cherryflow's Content Creation Agent — a world-class brand content strategist and copywriter.

Your responsibilities:
- Create engaging social media content (Instagram, Twitter/X, LinkedIn)
- Write SEO-optimized blog articles
- Generate high-converting ad copy
- Craft compelling product descriptions
- Develop content calendars

Always match the brand's tone, voice, and audience.
Use proven copywriting frameworks: AIDA, PAS, Hook-Story-Offer.
Every piece of content must have a clear goal and CTA.
"""


class ContentAgent(BaseAgent):
    def __init__(self, brand_name: str, tone: str = "professional", industry: str = "General"):
        super().__init__(
            agent_name="Content Agent",
            system_prompt=CONTENT_SYSTEM_PROMPT
        )
        self.brand_name = brand_name
        self.tone = tone
        self.industry = industry

    def generate_social_posts(self, topic: str, platforms: list = None) -> str:
        """Generate platform-specific social media posts."""
        if platforms is None:
            platforms = ["instagram", "twitter", "linkedin"]

        self.log(f"Creating social posts about: {topic}")
        prompt = f"""
        Create social media posts for "{self.brand_name}" about: {topic}

        Brand tone: {self.tone}
        Industry: {self.industry}

        Generate one post for each platform:
        {', '.join(p.upper() for p in platforms)}

        For each post include:
        - Platform name
        - Post content (with emojis where appropriate)
        - Hashtags (platform-appropriate count)
        - Best time to post
        - Expected engagement type

        Make each post platform-native — LinkedIn formal, Twitter punchy, Instagram visual-first.
        """
        return self.chat(prompt)

    def generate_weekly_calendar(self, week_theme: str) -> str:
        """Generate a full week content calendar."""
        self.log(f"Building weekly content calendar: {week_theme}")
        prompt = f"""
        Create a 7-day content calendar for "{self.brand_name}".

        Week Theme: {week_theme}
        Tone: {self.tone}
        Industry: {self.industry}

        For each day (Mon–Sun) provide:
        - Day & Date placeholder
        - Platform (rotate: Instagram / LinkedIn / Twitter / Blog)
        - Content type (post / reel / article / thread)
        - Topic & angle
        - Key message
        - CTA

        End with a weekly content strategy tip.
        """
        return self.chat(prompt)

    def write_blog_post(self, title: str, keywords: list) -> str:
        """Write a full SEO blog post."""
        self.log(f"Writing blog post: {title}")
        prompt = f"""
        Write a complete SEO-optimized blog post for "{self.brand_name}":

        Title: {title}
        Target Keywords: {', '.join(keywords)}
        Tone: {self.tone}

        Structure:
        1. SEO Title (60 chars max)
        2. Meta Description (155 chars max)
        3. Introduction (hook the reader)
        4. 4-5 Main sections with H2 headings
        5. Conclusion with CTA
        6. FAQ section (3 questions)

        Target length: 800-1000 words.
        Naturally include keywords without stuffing.
        """
        return self.chat(prompt)

    def write_ad_copy(self, product: str, target_audience: str, platform: str = "Facebook") -> str:
        """Generate high-converting ad copy."""
        self.log(f"Writing {platform} ad copy for: {product}")
        prompt = f"""
        Write high-converting ad copy for "{self.brand_name}":

        Product/Service: {product}
        Target Audience: {target_audience}
        Ad Platform: {platform}

        Deliver:
        1. PRIMARY HEADLINE (5-7 words, benefit-focused)
        2. SECONDARY HEADLINE (social proof or offer)
        3. AD BODY (2-3 sentences, PAS framework)
        4. CTA BUTTON TEXT (action word)
        5. VISUAL SUGGESTION (describe what image/video to use)

        Write 2 variations (A/B test versions).
        """
        return self.chat(prompt)

    def generate_product_description(self, product_name: str, features: list) -> str:
        """Write compelling product descriptions."""
        self.log(f"Writing product description for: {product_name}")
        prompt = f"""
        Write a compelling product description for "{self.brand_name}":

        Product: {product_name}
        Key Features: {', '.join(features)}
        Tone: {self.tone}

        Include:
        1. Attention-grabbing opening line
        2. Key benefits (not just features) — 3-5 bullets
        3. Who it's perfect for
        4. Emotional hook
        5. CTA / closing line

        Also write a short version (under 50 words) for category pages.
        """
        return self.chat(prompt)


if __name__ == "__main__":
    agent = ContentAgent(
        brand_name="Cherryflow AI",
        tone="bold and innovative",
        industry="AI & Technology"
    )

    print("=== CONTENT AGENT DEMO ===\n")

    print("--- Social Media Posts ---")
    posts = agent.generate_social_posts(
        topic="How AI agents are replacing entire marketing teams",
        platforms=["instagram", "linkedin", "twitter"]
    )
    print(posts)

    print("\n--- Ad Copy ---")
    agent.reset_conversation()
    ad = agent.write_ad_copy(
        product="AI Brand Growth Platform",
        target_audience="Marketing managers at D2C brands",
        platform="LinkedIn"
    )
    print(ad)
