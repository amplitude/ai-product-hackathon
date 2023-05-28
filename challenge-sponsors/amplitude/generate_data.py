import os

from amplitude import Amplitude, BaseEvent

# store your amplitude api key in an environment variable
# find keys on your project's page (fill in your org-url): https://analytics.amplitude.com/<org-url>/settings/projects
api_key = os.getenv('AMPLITUDE_API_KEY')
amplitude = Amplitude(api_key)

# customize the events you want to track
amplitude.track(
    BaseEvent(
        event_type='test event',
        user_id='test user',
        event_properties={
            'test property': 'test value',
        }
    )
)

# flush and shutdown to make sure all events are sent
amplitude.flush()
amplitude.shutdown()
