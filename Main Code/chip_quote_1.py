from trycourier import Courier
import read_file
import read_names

t = read_file.text
selected_quote = t

phone = []
phone = read_names.nameNPhone
phone_length = len(phone)
i = 0
selected_phone = ""

while i < phone_length:
  selected_phone = phone[i][1]
  i += 1

  client = Courier(auth_token="dk_prod_HNRW641YEZM9N8NEA8Z3JT3RC6ZV")

  resp = client.send(
    event="14KEADED0JMCVTH4D7QFW5C5R9XV",
    recipient="13df3e64-d21a-4cc9-b391-6e36dc073c41",
    profile={
      "phone_number": selected_phone,
    },
    data={
      "quote": selected_quote,
    },
  )

  print(resp['messageId'])