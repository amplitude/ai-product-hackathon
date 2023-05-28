# [Hugging Face](https://huggingface.co/)

Hugging Face is primarily a [repository of AI models](https://huggingface.co/models) that people and companies share for a variety of tasks. It contains a lot of the state-of-the-art models that power all sorts of AI applications out there. It also has training and inference platforms.

## Getting Started

While you can download and use models on Hugging Face for free, unfortunately, deploying an inference endpoint does not have a free tier so you'll want to [check out the pricing](https://huggingface.co/pricing) if you go down that route.

Otherwise, it's less obvious how to directly use Hugging Face. Instead, it's often the case that code and projects out there end up building on top of the [transformers library](https://pypi.org/project/transformers/) which is built by Hugging Face. For example, here's [code using a state-of-the art model to do zero-shot object detection in images](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/zero-shot-object-detection-with-grounding-dino.ipynb#scrollTo=psf2DLyLlXvs) that builds on top of the [most popular model on Hugging Face](https://huggingface.co/facebook/dino-vitb16).

## Other Resources

- Hugging Face integrates easily with [SageMaker](../sagemaker/README.md), which you can [learn more about here](https://huggingface.co/docs/sagemaker/inference). This lets you deploy models easily with free AWS credits!
