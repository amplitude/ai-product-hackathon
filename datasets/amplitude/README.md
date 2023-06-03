# Amplitude Demo Datasets

First-party user behavior data is really unique and quite hard to come by. Although we can't share the data of real customers for privacy reasons, we've seen enough of it that our demo datasets are fairly representative of real product data.

Here are three demo datasets that we've made available for this hackathon. They all live in a public S3 bucket `com-amplitude-2023-ai-product-hack-public` and documentation on the structure of the events can be found [here](https://www.docs.developers.amplitude.com/analytics/apis/export-api/#response-schema).

## Datasets

The datasets live in separate folders within the `datasets/` folder inside the bucket.

- `amplitunes/`: AmpliTunes (music streaming product, ~1 day)
- `teamchat/`: TeamChat (B2B messaging product, ~2 weeks)
- `amplifinancials/`: AmpliFinancials (consumer fintech product, ~5 months)

## Downloading the Data

We recommend using the [AWS CLI](https://aws.amazon.com/cli/) to download the data.

For example, you can list the files for the AmpliTunes dataset using:
```
aws s3 ls --no-sign-request s3://com-amplitude-2023-ai-product-hack-public/datasets/amplitunes/
```

And you can download a single file using:
```
aws s3 cp --no-sign-request s3://com-amplitude-2023-ai-product-hack-public/datasets/amplitunes/168342_2023-05-01_0#0.json.gz .
```

Or an entire folder using:
```
aws s3 sync --no-sign-request s3://com-amplitude-2023-ai-product-hack-public/datasets/amplitunes/ amplitunes/
```

As suggested by the filename, the data is compressed using GZIP and stored as a single JSON object per line (representing one event). See [here](https://www.docs.developers.amplitude.com/analytics/apis/export-api/#response-schema) for documentation on the structure of the events.
