# Example implementation for Chain of Thought streaming

import asyncio
from typing import AsyncGenerator

# Example configuration object (in real implementation, import from config module)
class ExampleConfig:
    default_model = "claude-sonnet-4-20250514"
    max_tokens = 3000

config = ExampleConfig()

class ExampleGuideGenerator:
    def __init__(self):
        # In real implementation, this would be the Anthropic client
        self.client = None
        self.system_prompt = "You are an expert educator..."
    
    async def stream_chain_of_thought_guide(self, topic: str) -> AsyncGenerator[str, None]:
        """
        Stream the AI's reasoning process as it develops the guide.
        
        This shows users how the AI thinks through:
        - Understanding the topic
        - Considering the audience
        - Structuring the content
        - Making pedagogical decisions
        """
        
        # Phase 1: Chain of Thought Prompt
        cot_prompt = f"""
        I need to create a learning guide for: {topic}
        
        Let me think through this step by step:
        
        <thinking>
        First, let me analyze what this topic involves...
        What are the key concepts someone needs to understand?
        What prerequisites should they have?
        What are the common challenges learners face with this topic?
        How can I break this down into digestible steps?
        What examples would be most helpful?
        What troubleshooting scenarios should I anticipate?
        </thinking>
        
        Please show your complete reasoning process as you develop a learning guide for {topic}.
        Think out loud about your pedagogical decisions, content structure, and why you're including each section.
        
        After your thinking process, create the actual guide.
        """
        
        # Stream the chain of thought
        try:
            response_stream = await asyncio.to_thread(
                self.client.messages.create,
                model=config.default_model,
                max_tokens=config.max_tokens,
                temperature=0.3,  # Slightly higher for more reasoning
                system=self.system_prompt + "\n\nShow your thinking process clearly before creating content.",
                messages=[{"role": "user", "content": cot_prompt}],
                stream=True
            )
            
            accumulated_content = ""
            reasoning_phase = True
            
            for event in response_stream:
                if hasattr(event, 'type') and event.type == "content_block_delta":
                    if hasattr(event, 'delta') and hasattr(event.delta, 'text'):
                        text_chunk = event.delta.text
                        accumulated_content += text_chunk
                        
                        # Different styling for reasoning vs final content
                        if reasoning_phase and ("thinking>" in text_chunk or "reasoning" in text_chunk.lower()):
                            yield f"🧠 {text_chunk}"  # Thinking indicator
                        elif "# " in text_chunk and reasoning_phase:
                            reasoning_phase = False
                            yield f"\n📝 [bold blue]Final Guide Generation:[/bold blue]\n{text_chunk}"
                        else:
                            yield text_chunk
                            
        except Exception as e:
            raise Exception(f"Failed to generate chain of thought guide: {str(e)}")


    # Alternative: Pure reasoning mode
    async def stream_pure_reasoning(self, topic: str) -> AsyncGenerator[str, None]:
        """
        Stream only the reasoning process, no final document.
        Shows how the AI would approach creating the guide.
        """
        
        reasoning_prompt = f"""
        I want you to think out loud about how you would approach creating a learning guide for: {topic}
        
        Walk me through your thought process:
        1. How would you analyze this topic?
        2. What would you consider about the learners?
        3. How would you structure the content?
        4. What pedagogical decisions would you make and why?
        5. What challenges would you anticipate?
        
        Don't create the actual guide - just show me your reasoning process as an expert educator.
        """
        
        # Stream only the reasoning
        response_stream = await asyncio.to_thread(
            self.client.messages.create,
            model=config.default_model,
            max_tokens=2000,
            temperature=0.4,
            system=self.system_prompt + "\n\nFocus entirely on explaining your thought process and reasoning.",
            messages=[{"role": "user", "content": reasoning_prompt}],
            stream=True
        )
        
        for event in response_stream:
            if hasattr(event, 'type') and event.type == "content_block_delta":
                if hasattr(event, 'delta') and hasattr(event.delta, 'text'):
                    yield f"💭 {event.delta.text}"
