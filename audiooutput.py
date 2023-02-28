import os
import boto3

os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA6O32WPVH5RKA7TGP'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
voice_id = 'Arthur'
# Create a client for the Amazon Polly service
polly = boto3.client('polly', region_name='us-east-1')

# Set the input text and voice
text = 'Hello, world!'

def speak_response(response):
    # Generate the speech using Amazon Polly
    response = polly.synthesize_speech(Text=response, OutputFormat='mp3', VoiceId=voice_id, Engine="neural")
    # Save the speech as an audio file
    with open('recentoutput.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())


