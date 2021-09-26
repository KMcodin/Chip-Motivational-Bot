from trycourier import Courier
import read_names

phone = []
phone = read_names.nameNPhone
phone_length = len(phone)
i = 0
selected_phone = ""
selected_name = ""

while i < phone_length:
  selected_phone = phone[i][1]
  selected_name = phone[i][0]
  i += 1

  client = Courier(auth_token="dk_prod_HNRW641YEZM9N8NEA8Z3JT3RC6ZV")

  resp = client.send(
    event="B2R86X49QHMHX5KF0YECJ75MCM7V",
    recipient="8262c669-6362-41ed-b62d-337803658bdd",
    profile={
      "phone_number": selected_phone,
    },
    data={
      "name": selected_name,
      "support_phone": "800-273-8255",
      "chat_web": "suicidepreventionlifeline.org/chat/",
    },
  )

  print(resp['messageId'])