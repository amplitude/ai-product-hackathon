# [AWS SageMaker](https://aws.amazon.com/sagemaker/)

SageMaker is a powerful tool for building, training, and deploying ML models. You can deploy a bunch of existing models from the AWS Marketplace for things like object detection, text summarization, fraud detection, etc. You can also spin up infrastructure to train your own models or create an inference endpoint from a model that you've trained.

## Getting Started

SageMaker has a number of [tutorials](https://aws.amazon.com/sagemaker/getting-started/) for different use cases and also has a nice [example documentation site](https://sagemaker-examples.readthedocs.io/en/latest/index.html).

Training an entire model during a hackathon is probably a stretch, so we recommend looking into deploying pretrained models that you want to use, e.g. [this tutorial](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/pytorch_bert/deploy_bert_outputs.html) for deploying the BERT NLP model.

You can find [SageMaker pricing here](https://aws.amazon.com/sagemaker/pricing/); it has a very generous free tier that will likely let you develop, test, and deploy models during the entire hackathon for free!

## Other Resources

- SageMaker integrates easily with [Hugging Face](../huggingface/README.md) models, which you can [learn more about here](https://huggingface.co/docs/sagemaker/inference). This gives you a wide variety of models to deploy at your fingertips!
- Here is a [blog post on building AI-powered search](https://aws.amazon.com/blogs/database/building-ai-powered-search-in-postgresql-using-amazon-sagemaker-and-pgvector/) that deploys a pre-trained [SentenceTransformer](../sentence-transformers/README.md) model from [Hugging Face](../huggingface/README.md) to SageMaker and then stores the embeddings using [pgvector](https://github.com/pgvector/pgvector).
