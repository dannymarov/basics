usernames = ['admin', 'neo', 'patrick', 'morpheus', 'naja']
for username in usernames:
    if username == 'admin':
        print(f'Welcome Admin would you like a status report?')
    else:
        print(f'Greetings {username.title()} and welcome to our web site')

#########OPtion #1
# nums1 = range(1, 11)
# nums2 = range(1, 11)
# for num1 in nums1:
#     for num2 in nums2:
#         print(f'{num1}*{num2}={num1*num2}'.ljust(7), end='\t')
#     print()

#########Option #2
# nums1 = range(1, 11)
# nums2 = range(1, 11)
# for num1 in nums1:
#     for num2 in nums2:
#         print(f'\t{num1}*{num2}={num1*num2}'.ljust(7),end='\t')
#     print()

