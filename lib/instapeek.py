#				#
#	AUTHOR: RIP MEEP :)	#
#				#

import requests
import json
import time

class InstagramProfile(object):
	class InstagramInformation(object):
		class InstagramPost(object):
			def __init__(self):
				self.post_number = 0
				self.post_id = 0
				self.post_shortcode = None
				self.post_url = None
				self.post_owner_id = 0
				self.post_owner_username = None
				self.post_caption = None
				self.post_image_timestamp = 0
				self.post_image_ctimestamp = None

				self.is_video = False

				self.location_name = None
				self.location_id = 0

				self.image_height = 0
				self.image_width = 0

				self.instagram_recognition_caption = None

		def __init__(self):
			self.url = None
			self.api_url = None
			self.external_url = None
			self.username = None

			self.profile_picture_url = None
			self.profile_picture_url_hd = None

			self.id = None

			self.biography = None

			self.blocked_by_viewer = False
			self.restricted_by_viewer = False
			self.country_blocked = False

			self.users_followed_by = 0
			self.followed_by_viewer = False
			self.users_followed = 0
			self.follows_viewer = False

			self.full_name = None

			self.has_channel = False

			self.is_business_account = False
			self.business_category_name = None
			self.overall_category_name = None

			self.is_joined_recently = False
			self.is_private = False
			self.is_verified = False

			self.mutual_followers = 0
			self.requested_by_viewer = False
			self.conntected_fb_page = None

			self.number_of_posts = 0
			self.posts = []

	def __init__(self, username):
		self.username = str(username)
		self.profile_url = "https://instagram.com/{}".format(self.username)
		self.profile_api_url = "{}/{}".format(self.profile_url, "?__a=1")

		self.__raw_response = ""
		self.__response = ""

		self.information = self.InstagramInformation()

	def peek(self):
		r = requests.get(self.profile_api_url, headers={"content-type": "application/json"})
		status_code = r.status_code

		if status_code == 404:
			return {"status": False, "msg": "404 :("}

		self.__raw_response = r.text

		try:
			self.__response = json.loads(self.__raw_response)
		except:
			return {"status": False, "msg": "JSON loading failed", "response": {}}

		try:
			self.information.url = self.profile_url
		except:
			pass

		try:
			self.information.api_url = self.profile_api_url
		except:
			pass

		try:
			self.information.external_url = self.__response["graphql"]["user"]["external_url"]
		except:
			pass

		try:
			self.information.username = self.username
		except:
			pass

		try:
			self.information.profile_picture_url = self.__response["graphql"]["user"]["profile_pic_url"]
		except:
			pass

		try:
			self.information.profile_picture_url_hd = self.__response["graphql"]["user"]["profile_pic_url_hd"]
		except:
			pass

		try:
			self.information.id = int(self.__response["graphql"]["user"]["id"])
		except:
			pass

		try:
			self.information.biography = self.__response["graphql"]["user"]["biography"]
		except:
			pass

		try:
			self.information.blocked_by_viewer = self.__response["graphql"]["user"]["has_blocked_viewer"]
		except:
			pass

		try:
			self.information.restricted_by_viewer = self.__response["graphql"]["user"]["restricted_by_viewer"]
		except:
			pass

		try:
			self.information.country_blocked = self.__response["graphql"]["user"]["country_block"]
		except:
			pass

		try:
			self.information.users_followed_by = int(self.__response["graphql"]["user"]["edge_followed_by"]["count"])
		except:
			pass

		try:
			self.information.followed_by_viewer = self.__response["graphql"]["user"]["followed_by_viewer"]
		except:
			pass

		try:
			self.information.users_followed = self.__response["graphql"]["user"]["edge_follow"]["count"]
		except:
			pass

		try:
			self.information.follows_viewer = self.__response["graphql"]["user"]["follows_viewer"]
		except:
			pass

		try:
			self.information.full_name = self.__response["graphql"]["user"]["full_name"]
		except:
			pass

		try:
			self.information.has_channel = self.__response["graphql"]["user"]["has_channel"]
		except:
			pass

		try:
			self.information.is_business_account = self.__response["graphql"]["user"]["is_business_account"]
		except:
			pass

		try:
			self.information.business_category_name = self.__response["graphql"]["user"]["business_category_name"]
		except:
			pass

		try:
			self.information.overall_category_name = self.__response["graphql"]["user"]["overall_category_name"]
		except:
			pass

		try:
			self.information.is_joined_recently = self.__response["graphql"]["user"]["is_joined_recently"]
		except:
			pass

		try:
			self.information.is_private = self.__response["graphql"]["user"]["is_private"]
		except:
			pass

		try:
			self.information.is_verified = self.__response["graphql"]["user"]["is_verified"]
		except:
			pass

		try:
			self.information.connected_fb_page = self.__response["graphql"]["user"]["connected_fb_page"]
		except:
			pass

		try:
			self.information.number_of_posts = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])
		except:
			pass


		return {"status": True, "msg": "success", "return": self.__raw_response}

	def get_post(self, post_n):
		post = InstagramProfile.InstagramInformation.InstagramPost()

		if self.information.number_of_posts <= 0:
			return {"status": False, "msg": "User does not have any posts. If this is incorrect, please run [InstagramProfile].peek() to fill object", "post": post}
		elif self.information.is_private:
			return {"status": False, "msg": "User account is private", "post": post}

		try:
			post.post_number = int(post_n)

			try:
				post.post_id = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["id"])
			except:
				pass

			try:
				post.post_shortcode = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["shortcode"]
			except:
				pass

			try:
				post.post_url = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["display_url"]
			except:
				pass

			try:
				post.post_owner_id = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["owner"]["id"])
			except:
				pass

			try:
				post.post_owner_username = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["owner"]["username"]
			except:
				pass

			try:
				post.post_caption = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
			except:
				pass

			try:
				post.location_id = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["location"]["id"])
			except:
				pass

			try:
				post.location_name = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["location"]["name"]
			except:
				pass

			try:
				post.post_image_timestamp = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["taken_at_timestamp"])
			except:
				pass

			try:
				post.post_image_ctimestamp = time.ctime(post.post_image_timestamp)
			except:
				pass

			try:
				post.is_video = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["is_video"]
			except:
				pass

			try:
				post.image_height = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["dimensions"]["height"])
			except:
				pass

			try:
				post.image_width = int(self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["dimensions"]["width"])
			except:
				pass

			try:
				post.instagram_recognition_caption = self.__response["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][post_n]["node"]["accessibility_caption"]
			except:
				pass

		except:
			return {"status": False, "msg": "Could not get all of the post information", "post": post}

		return {"status": True, "msg": "success", "post": post}

	def get_all_posts(self):
		if self.information.number_of_posts <= 0:
			return {"status": False, "msg": "User does not have any posts", "posts": []}
		elif self.information.is_private:
			return {"status": False, "msg": "User account is private", "posts": []}

		try:
			for i in range(self.information.number_of_posts):
				try:
					self.information.posts.append(self.get_post(i)["post"])
				except:
					continue
		except:
			return {"status": False, "msg": "Could not retrieve all posts", "posts": self.information.posts}

		return {"status": True, "msg": "success", "posts": self.information.posts}



