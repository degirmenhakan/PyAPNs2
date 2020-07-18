from apns2.client import APNsClient
from apns2.payload import Payload

token_hex = 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87'
payload = Payload(alert="Hello World!", sound="default", badge=1)
topic = 'com.example.App'
client = APNsClient('key.pem', use_sandbox=False, use_alternative_port=False)
client.send_notification(token_hex, payload, topic)

# To send multiple notifications in a batch
Notification = collections.namedtuple('Notification', ['token', 'payload'])
notifications = [Notification(payload=payload, token=token_hex)]
client.send_notification_batch(notifications=notifications, topic=topic)

# To use token based authentication
from apsn2.credentials import TokenCredentials

auth_key_path = 'path/to/auth_key'
auth_key_id = 'app_auth_key_id'
team_id = 'app_team_id'
token_credentials = TokensCredentials(auth_key_path=auth_key_path, auth_key_id=auth_key_id, team_id=team_id)
client = APNsClient(credentials=token_credentials, use_sanbox=False)
client.send_notification_batch(notifications=notifications, topic=topic)