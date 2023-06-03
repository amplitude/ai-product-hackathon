# Amplitude Demo Datasets

First-party user behavior data is really unique and quite hard to come by. Although we can't share the data of real customers for privacy reasons, we've seen enough of it that our demo datasets are fairly representative of real product data.

Here are three demo datasets that we've made available for this hackathon. They all live in a public S3 bucket `com-amplitude-2023-ai-product-hack-public` and documentation on the structure of the events can be found [here](https://www.docs.developers.amplitude.com/analytics/apis/export-api/#response-schema).

## Datasets

The datasets live in separate folders within the `datasets/` folder inside the bucket.

- `datasets/amplitunes/`: AmpliTunes (music streaming product, ~1 day)
- `datasets/teamchat/`: TeamChat (B2B messaging product, ~2 weeks)
- `datasets/amplifinancials/`: AmpliFinancials (consumer fintech product, ~5 months)

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


## Getting Data into Amplitude

If you want to import one of these datasets into Amplitude, you can use the [Amplitude S3 Import](https://www.docs.developers.amplitude.com/data/sources/amazon-s3/#give-amplitude-access-to-your-s3-bucket) feature in your own Amplitude account. Here is the relevant configuration.
- ARN: `arn:aws:iam::601785421554:role/AmplitudeReadRole`
- External ID: `BE8WKg3ot2OTc7gcXp6y0VD1`

And once you configure the source, switch to manual converter setup and use this JSON:
```
{
    "converterConfig": {
        "fileType": "json",
        "compressionType": "gzip",
        "convertToAmplitudeFunc": {
            "insert_id": "$insert_id",
            "adid": "adid",
            "city": "city",
            "country": "country",
            "device_brand": "device_brand",
            "carrier": "device_carrier",
            "device_id": ["ifelse",
                ["eq", "device_id", ["value", ""]],
                ["value", null],
                "device_id"
            ],
            "device_manufacturer": "device_manufacturer",
            "device_model": "device_model",
            "device_type": "device_type",
            "dma": "dma",
            "event_id": "event_id",
            "event_properties": "event_properties",
            "time": ["iso_time_to_ms", "event_time"],
            "event_type": "event_type",
            "group_properties": "group_properties",
            "groups": "groups",
            "idfa": "idfa",
            "ip": "ip_address",
            "language": "language",
            "library": "library",
            "location_lat": "location_lat",
            "location_lng": "location_lng",
            "os_name": "os_name",
            "os_version": "os_version",
            "platform": "platform",
            "region": "region",
            "session_id": "session_id",
            "user_id": ["ifelse",
                ["eq", "user_id", ["value", ""]],
                ["value", null],
                "user_id"
            ],
            "user_properties": "user_properties",
            "app_version": "version_name"
        }
    },
    "keyValidatorConfig": {
        "filterPattern": ".*"
    }
}
```

Come find an Ampliteer if you have any issues with this!
