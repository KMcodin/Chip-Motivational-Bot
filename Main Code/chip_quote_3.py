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
selected_name = ""

while i < phone_length:
  selected_phone = phone[i][1]
  selected_name = phone[i][0]
  i += 1

  client = Courier(auth_token="dk_prod_HNRW641YEZM9N8NEA8Z3JT3RC6ZV")

  resp = client.send(
    event="Q1T9R6690R4F1VM67ZF8TCDY6P95",
    recipient="c62aa9a6-c7da-491c-93e7-de7cc48572a3",
    profile={
      "phone_number": selected_phone,
    },
    data={
      "name": selected_name,
      "quote": selected_quote,
    },
  )

  print(resp['messageId'])