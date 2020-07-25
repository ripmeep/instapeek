#!/usr/bin/env python3

import instapeek
import sys
import os
import argparse

logo = """\033[01;31m
             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.		       \033[01;37mINSTAPEEK\033[01;31m
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;       \033[01;37mAUTHOR:	RIP MEEP\033[01;31m
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
\033[0m"""

print(logo + "\n\n")

parser = argparse.ArgumentParser()

parser.add_argument("-U", "--username", help="Username to peek [example: --username/-U johndoe]", required=True)
parser.add_argument("--get-posts", help="Get information on the users posts (MUST BE PUBLIC ACCOUNT)", action="store_true", required=False)
parser.add_argument("-O", "--output", help="Output information to file [example: --output/-O username.txt]", required=False)

args = parser.parse_args()

output_file = None

if args.output:
	try:
		output_file = open(args.output, "w")
		sys.stdout = output_file
	except Exception as e:
		sys.stderr.write("Error: {}\n".format(e))
		sys.exit()

username = args.username
get_posts = args.get_posts


def full_exit():
	if args.output:
		sys.stderr.write("\n\033[01;37m[\033[01;32m+\033[01;37m] \033[0mAll output and results written to {}\n".format(args.output))
		output_file.close()

	sys.stderr.write("\033[01;37m[\033[01;31m!\033[01;32m] \033[0mExiting......\n")
	sys.exit()

sys.stderr.write("\033[01;37m[\033[01;32m+\033[01;37m] \033[0mGetting {}'s info......\n".format(username))

profile = instapeek.InstagramProfile(username)
response = profile.peek()

if not response["status"]:
	sys.stderr.write("\033[01;37m[\033[01;31m!\033[01;37m] \033[0mCould not get information for user {}: {}\n".format(username, response["msg"]))
	full_exit()

info = profile.information

print("\n")

print("=== USER INFORMATION ===\n")

print("Profile Username:         %s" % info.username)
print("Profile ID:               %d" % info.id)
print("Profile Biography:        %s" % repr(info.biography))
print("Profile URL:              %s\n" % info.url)
print("Profile API URL:          %s\n" % info.api_url)
print("Profile External URL:     %s\n" % info.external_url)
print("Profile Picture:          %s\n" % info.profile_picture_url)
print("Profile Picture HD:       %s\n" % info.profile_picture_url_hd)
print("Blocked By Viewer:        %s" % info.blocked_by_viewer)
print("Restricted By Viewer:     %s" % info.restricted_by_viewer)
print("Country Blocked:          %s" % info.country_blocked)
print("Followers:                %d" % info.users_followed_by)
print("Following:                %d" % info.users_followed)
print("Viewer Is Following:      %s" % info.followed_by_viewer)
print("Follows Viewer:           %s" % info.follows_viewer)
print("Full Name:                %s" % info.full_name)
print("Has Channel:              %s" % info.has_channel)
print("Is Business Account:      %s" % info.is_business_account)
print("Business Category:        %s" % info.business_category_name)
print("Overall Category:         %s" % info.overall_category_name)
print("Joined Recently:          %s" % info.is_joined_recently)
print("Is Private:               %s" % info.is_private)
print("Is Verified:              %s" % info.is_verified)
print("Facebook Page Linked:     %s\n" % info.connected_fb_page)
print("Number Of Posts:          %d" % info.number_of_posts)

print("\n")


if not args.get_posts:
	sys.stderr.write("\033[01;37m[\033[01;32m+\033[01;37m] \033[0mDone.\n")
	full_exit()

sys.stderr.write("\033[01;37m[\033[01;32m+\033[01;37m] \033[0mGetting {}'s posts......\n".format(username))

posts = profile.get_all_posts()
number_of_posts = len(posts["posts"])

if not posts["status"]:
	sys.stderr.write("\033[01;37m[\033[01;31m!\033[01;37m] \033[0mFailed to get user posts: {}\n".format(posts["msg"]))
	full_exit()

if number_of_posts <= 0:
	sys.stderr.write("\033[01;37m[\033[01;31m!\033[01;37m] \033[0m{} does not have any posts\n".format(username))
	full_exit()


for i in range(number_of_posts):
	post = posts["posts"][i]

	print("\n\n=== POST       %d ===\n\n"%(i + 1))

	print("Post Number:                        %d" % (post.post_number + 1))
	print("Post ID:                            %d" % post.post_id)
	print("Post Shortcode:                     %s" % post.post_shortcode)
	print("Post URL:                           %s" % post.post_url)
	print("Post Owner ID:                      %s" % post.post_owner_id)
	print("Post Owner Username:                %s" % post.post_owner_username)
	print("Post Caption:                       %s" % post.post_caption)
	print("Post Timestamp:                     %d" % post.post_image_timestamp)
	print("Post Time String:                   %s" % post.post_image_ctimestamp)
	print("Post Is Video:                      %s" % post.is_video)
	print("Height:                             %d" % post.image_height)
	print("Width:                              %d" % post.image_width)
	print("Instagram Recognition Caption:      %s" % post.instagram_recognition_caption)
	print("Location ID:                        %d" % post.location_id)
	print("Location Name:                      %s" % post.location_name)


full_exit()
