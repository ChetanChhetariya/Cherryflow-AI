"""
Cherryflow-AI — SEO Content Agent
Optimizes content for search engines to drive organic brand growth.
"""

from agents.base_agent import BaseAgent


SEO_SYSTEM_PROMPT = """
You are Cherryflow's SEO Content Agent — an expert in search engine optimization and content strategy.

Your responsibilities:
- Conduct keyword research and analysis
- Optimize existing content for SEO
- Generate SEO-optimized blog posts and landing pages
- Build content clusters and topic authority
- Analyze competitor SEO strategies

Always follow Google's E-E-A-T principles (Experience, Expertise, Authoritativeness, Trustworthiness).
Focus on search intent — informational, navigational, transactional, or commercial.
Recommend realistic, actionable strategies for organic growth.
"""


class SEOAgent(BaseAgent):
    def __init__(self, brand_name: str, website: str = "", niche: str = ""):
        super().__init__(
            agent_name="SEO Agent",
            system_prompt=SEO_SYSTEM_PROMPT
        )
        self.brand_name = brand_name
        self.website = website
        self.niche = niche

    def keyword_research(self, seed_keyword: str, num_keywords: int = 20) -> str:
        """Generate keyword ideas with intent and difficulty analysis."""
        self.log(f"Researching keywords for: {seed_keyword}")
        prompt = f"""
        Perform keyword research for "{self.brand_name}" in the {self.niche} niche.

        Seed Keyword: {seed_keyword}

        Generate {num_keywords} keyword ideas including:
        - Short-tail keywords (1-2 words)
        - Long-tail keywords (3-5 words)
        - Question-based keywords (how/what/why/best)
        - Commercial intent keywords (buy/best/top/vs)

        For each keyword provide:
        | Keyword | Search Intent | Difficulty (Low/Med/High) | Content Type |

        End with top 5 priority keywords to target first.
        """
        return self.chat(prompt)

    def optimize_content(self, content: str, target_keyword: str) -> str:
        """Optimize existing content for a target keyword."""
        self.log(f"Optimizing content for keyword: {target_keyword}")
        prompt = f"""
        SEO-optimize this content for the target keyword: "{target_keyword}"

        Original Content:
        {content}

        Provide:
        1. SEO Score of original (X/100)
        2. Optimized Title Tag (60 chars max)
        3. Optimized Meta Description (155 chars max)
        4. Keyword placement recommendations
        5. Missing LSI keywords to add
        6. Internal linking suggestions
        7. Fully optimized rewrite of the content

        Follow Google's content guidelines strictly.
        """
        return self.chat(prompt)

    def content_cluster_plan(self, pillar_topic: str) -> str:
        """Build a topic cluster strategy for authority building."""
        self.log(f"Building content cluster for: {pillar_topic}")
        prompt = f"""
        Create a content cluster strategy for "{self.brand_name}" around:

        Pillar Topic: {pillar_topic}
        Niche: {self.niche}

        Provide:
        1. PILLAR PAGE — Main topic, target keyword, word count
        2. CLUSTER ARTICLES — 8-10 supporting articles with:
           - Title
           - Target keyword
           - Search intent
           - How it links to the pillar
        3. Internal linking structure diagram (text-based)
        4. Publishing timeline recommendation (12 weeks)
        """
        return self.chat(prompt)

    def competitor_seo_analysis(self, competitor_url: str) -> str:
        """Analyze competitor SEO strategy."""
        self.log(f"Analyzing competitor: {competitor_url}")
        prompt = f"""
        Analyze the SEO strategy for competitor: {competitor_url}

        Based on typical strategies for sites in the {self.niche} space, provide:
        1. Likely content strategy (blog frequency, content types)
        2. Probable keyword focus areas
        3. Backlink strategy assessment
        4. Content gaps we can exploit
        5. Top 5 opportunities for "{self.brand_name}" to outrank them

        Give actionable, specific recommendations.
        """
        return self.chat(prompt)

    def generate_meta_tags(self, page_title: str, page_content: str) -> str:
        """Generate optimized meta tags for a page."""
        self.log(f"Generating meta tags for: {page_title}")
        prompt = f"""
        Generate complete SEO meta tags for this page:

        Brand: {self.brand_name}
        Page Title: {page_title}
        Page Content Summary: {page_content}

        Provide:
        1. <title> tag (50-60 chars)
        2. <meta description> (140-155 chars)
        3. Open Graph tags (og:title, og:description, og:image suggestion)
        4. Twitter Card tags
        5. Schema markup recommendation (JSON-LD type)

        Format as ready-to-use HTML code snippets.
        """
        return self.chat(prompt)


if __name__ == "__main__":
    agent = SEOAgent(
        brand_name="Cherryflow AI",
        website="cherryflow.ai",
        niche="AI Marketing & Brand Automation"
    )

    print("=== SEO AGENT DEMO ===\n")

    print("--- Keyword Research ---")
    keywords = agent.keyword_research(
        seed_keyword="AI marketing automation",
        num_keywords=15
    )
    print(keywords)

    print("\n--- Content Cluster Plan ---")
    agent.reset_conversation()
    cluster = agent.content_cluster_plan("AI agents for brand growth")
    print(cluster)
