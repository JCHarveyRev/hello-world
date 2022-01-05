from rev_ai import apiclient
from rev_ai.models import CustomVocabulary
access_token = '02UW0sApy7ARHfhAhHMGXlGPTozxu8U4zJIMlKdWiGa_xVR-4SGT4MY8H3LmjKwo4n8QfImCQLY2rCIa9wBY6dGNahbns'

# (optional) Create custom_vocabularies to submit with job
custom_vocabularies = [CustomVocabulary(["Fetid Corpse"])]

# Create client with your access token
client = apiclient.RevAiAPIClient(access_token)

# Submit job from media url
url_job = client.submit_job_url(media_url="https://drive.google.com/file/d/1--qCZeDqMaezIuRd9_QAl5qxmVR-3c2U/", metadata="My_metadata", callback_url="https://example.com/callback", skip_diarization=True, custom_vocabularies=custom_vocabularies)
