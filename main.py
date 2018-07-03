import selenium
from selenium import webdriver as wd
import time
from collections import Counter

tag_list = []

explore_url = "https://www.instagram.com/explore/tags"

top_posts = '_9AhH0'

# open chrome headless
op = wd.ChromeOptions()
op.add_argument('headless')
# b = wd.Chrome(chrome_options=op)
b = wd.Chrome()

# adjust these params
search_list = ['nycspc','magnumphotos','wearethestreet','storyofthestreet']
search_len = 5

for s in range(search_len):
	print('Searching #' + search_list[s])
	b.get(explore_url+'/'+search_list[s])

	# print(b.page_source)
	time.sleep(3)

	# close login prompt
	if (len(search_list)==1):
		b.find_elements_by_class_name('Ls00D')[0].click()

	# get posts
	posts = b.find_elements_by_class_name(top_posts)

	# only get tags from the top 9 posts
	for i in range(9):
	# for i in range(1):

		# click on the first post
		posts[i].click()
		time.sleep(1)
		# print(b.page_source)

		# get all hashtag links
		tags = b.find_elements_by_partial_link_text('#')

		for t in tags:
			try:
				tag_list.append(t.get_attribute('innerHTML').encode()) 
			except UnicodeEncodeError:
				print('Could not add tag: ' + t.get_attribute('innerHTML'))
		# print(tag_list)

		b.find_element_by_class_name('ckWGn').click()
		time.sleep(1)

	# print(Counter(tag_list))

	most_common_tags = Counter(tag_list).most_common()

	next_search_idx = 0
	while(most_common_tags[next_search_idx][0][1:] in search_list):
		next_search_idx = next_search_idx+1
	search_list.append(most_common_tags[next_search_idx][0][1:])

print(zip(*Counter(tag_list).most_common(30))[0])
b.close()
	# if __name__ == "__main__":
# 	main();