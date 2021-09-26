from trycourier import Courier

client = Courier(auth_token="dk_prod_HNRW641YEZM9N8NEA8Z3JT3RC6ZV")

resp = client.send(
  event="B2R86X49QHMHX5KF0YECJ75MCM7V",
  recipient="8262c669-6362-41ed-b62d-337803658bdd",
  profile={
    "phone_number": "786-351-8694",
  },
  data={
    "name": "Rogelio",
    "support_phone": "800-273-8255",
    "chat_web": "suicidepreventionlifeline.org/chat/",
  },
)

print(resp['messageId'])