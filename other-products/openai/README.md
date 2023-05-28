# [OpenAI](https://openai.com/)

The OpenAI APIs provide powerful language capabilities including ChatGPT and more. They're useful for tackling just about any language-based task, including:
- Content generation
- Summarization
- Classification, categorization, and sentiment analysis
- Data extraction
- Translation

It's one of the easiest and more powerful ways to include language-related AI in your applications.

## Getting Started

You can find a quickstart tutorial [here](https://platform.openai.com/docs/quickstart). We also recommend checking out this [repository of examples](https://platform.openai.com/examples) which is helpful for both identifying use cases as well as example code. Here's one of them for grammar correction:

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
```

You should create your own OpenAI account with your own billing information. Pricing can be found [here](https://openai.com/pricing), but the short of it is that you get $5 of free credits and then pay per 1,000 tokens.

In our experience, a day of intense development ends up being a few dollars for the `gpt-3.5-turbo` model (equivalent to ChatGPT). There are API calls that are ~100x the price of that one, though, so keep that in mind!

## Other Resources

- If you plan to use the OpenAI APIs, we recommend [New Relic's OpenAI Observability](../../challenge-sponsors/newrelic/README.md) tool to monitor your API calls.
- In addition to the chat/completion APIs, OpenAI has powerful [embedding APIs](https://platform.openai.com/docs/guides/embeddings) as well, which essentially turn text into semantic vectors. You can then store those vectors into something like [LanceDB](../../challenge-sponsors/lancedb/README.md) to perform interesting search and retrieval tasks.
