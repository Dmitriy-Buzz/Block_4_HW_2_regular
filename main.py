import re
from pprint import pprint
import csv
from decorator import decorator

pattern_phone = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
sub_phone = r'+7(\3)\6-\8-\10 \12\13'

with open("phonebook_raw.csv", encoding= 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def form_phone():
    form_phone = []
    for contact in contacts_list[1:]:
        new_contact = []
        full_name_str = ','.join(contact[:3])
        result = re.findall(r'(\w+)', full_name_str)
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone_pattern = re.compile(pattern_phone)
        changed_phone = phone_pattern.sub(sub_phone, contact[5])
        new_contact.append(changed_phone)
        new_contact.append(contact[6])
        form_phone.append(new_contact)
    return form_phone
@decorator
def new_phone_book():
    phone_dict = {}
    for contact in form_phone():
        if contact[0] in phone_dict:
            contact_value = phone_dict[contact[0]]
            for i in range(len(contact_value)-1):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
             phone_dict[contact[0]] = contact

    return list(phone_dict.values())

with open("new_phone_book.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_phone_book())