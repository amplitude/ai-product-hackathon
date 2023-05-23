# [Amplitude](https://amplitude.com/)

Amplitude is a product analytics tool that helps companies understand what their users are doing in order to build better products.

## Challenge

Amplitude is awarding a $5,000 prize for the project that best uses AI in combination with the Amplitude product.

## Getting Started

Here are some steps to get started using Amplitude. They can be done before the hackathon starts!

1. [Sign up for an Amplitude account](https://analytics.amplitude.com/signup) if you don't have one already.
1. Follow the onboarding flow for sending data into Amplitude (we recommend the [Python SDK](https://www.docs.developers.amplitude.com/data/sdks/sdk-quickstart/#python)).
1. Remember to `pip install -r requirements.txt` into your (ideally virtual) environment.
1. See `generate_data.py` for starter code for sending whatever data you want.
1. See `rest_api.py` for starter code for querying the [Dashboard REST API](https://www.docs.developers.amplitude.com/analytics/apis/dashboard-rest-api/).

## Documentation

Full documentation for the SDKs (to send data to Amplitude) and the APIs (to programmatically access Amplitude features) can be around at [docs.developers.amplitude.com](https://www.docs.developers.amplitude.com/).

## Ideas

- Use LLMs that understand code to automatically instrument product actions into Amplitude.
- Come up with a way to instrument AI-powered products, and build interesting charts/dashboards to evaluate the effectiveness of AI in the product.
- Build a browser extension to automate creating Amplitude charts from other contexts (JIRA, GitHub, etc).
- Fine tune a chatbot to teach users how to use Amplitude in different situations.
- Build predictive models for retention, churn, likelihood of purchase, etc on top of a behavioral dataset.
