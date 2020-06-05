import shutil
import re


with open('potential-contacts.txt', 'r') as f:
    contents = f.read()
   
    # no (), with a hyphen
    pattern1 = r"\d{3}-\d{3}-\d{4}"

    #starting with a () and hyphens
    pattern2 = r"\(\d{3}\)\d{3}-\d{4}"

    #with a . in between
    pattern3 = r"\d{3}\.\d{3}\.\d{4}"

    # no area code, add 206
    pattern4 = r"\d{3}-\d{4}"

    phone1 = re.findall(pattern1,contents)
    phone2 = re.findall(pattern2,contents)
    phone3 = re.findall(pattern3,contents)
    phone4 = re.findall(pattern4,contents)
    # print(phone4)
  
    phone_numbers = []

    for i in range(len(phone1)):
        phone_numbers.append(phone1[i])

    for i in range(len(phone2)):
        num = phone2[i].replace('(','').replace(')','-')
        phone_numbers.append(num)

    for i in range(len(phone3)):
        num = phone3[i].replace('.','-').replace('.','-')
        phone_numbers.append(num)

    for i in range(len(phone4)):
        phone_numbers.append('206-'+phone4[i])
    
    # remove duplicates
    clean_numbers = list(set(phone_numbers))
    
    # sort
    clean_numbers.sort()

with open('phone_numbers.txt', 'w') as f:
    
    for i in clean_numbers:
        f.write(i+'\n')


########### email ################
with open('potential-contacts.txt', 'r') as f:
    content = f.read()
   
    # .com
    patternA = r"[\w\d]{1,}\.[\w\d]{1,}@[\S\w\d]{1,}\.[a-z]{2,4}"

 
    ### Why does the .com ignore all the regex and only get .com to return?
    # patternB = r"[\w\d]{1,}\.[\w\d]{1,}@[\S\w\d]{1,}(\.com)"



    email1 = re.findall(patternA,content)
    # print(email1)

    clean_email = list(set(email1))

    clean_email.sort()

with open('emails.txt', 'w') as f:
    
    for i in clean_email:
        f.write(i+'\n')










# print(contents)




# phone numbers
# missing area codes should add 206


# for ch in (len(contents)):
#     pattern = 
#     string = 


#     if re.match(pattern, string)





# email
# target the @ symbol and go back to the previous space?



# return phone numbers to phone_numbers.txt

# return emails to emails.txt