#!/usr/bin/env python

from twython import Twython
import csv

t = Twython(app_key='E4vyeGaubHFV8ws2lImUiGYQt',
            app_secret='D0wjZgRhpY2CAjFv3bjXTnxkzNgoNCAevYV7Bno0JnKxW5yKOr',
            oauth_token='4395343635-nNWpHAp9dgnBg5gcB5fvOBZkcr8WSfMHYv4d9AZ',
            oauth_token_secret='M03Hd9wEPOJoRKL1f170sEnFT1BvJlOcG9cMCaq8L8aZP')

# ids = ""
#
# with open('input_ids.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',')
#     for row in spamreader:
#         ids += ", ".join(row) + ", "
#
# users = t.lookup_user(user_id=ids)
#
# with open('output_location.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',')
#     for entry in users:
#         spamwriter.writerow([entry['id'],
#                              entry['location'],
#                              entry['name']])

ids = ""
i = 0

with open('input_ids.csv', 'rb') as a:
    spamreader = csv.reader(a, delimiter=',')
    for row in spamreader:
        if i < 90:
            i += 1
            ids += ",".join(row).encode('utf-8') + ","
        else:
            try:
                users = t.lookup_user(user_id=ids)
                with open('output_location.csv', 'wb') as b:
                    spamwriter = csv.writer(b, delimiter=',')
                    for entry in users:
                            print entry['location']
                            spamwriter.writerow([entry['id'],
                                                 entry['location'].encode('utf-8')])

            except: # catch *all* exceptions
                print "error"
            i = 0





