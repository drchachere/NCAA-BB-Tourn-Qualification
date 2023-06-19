from playwright.sync_api import sync_playwright
import pandas as pd


tourn_seed_text = ""
formatted_tourn_seed_text = ""



with sync_playwright() as p:
	browser = p.chromium.launch(headless=False, slow_mo=500)
	context = browser.new_context(viewport={ 'width': 1280, 'height': 56024 })
	page = context.new_page()

	for season in range(1993, 2024):
		s_r_url = "https://www.sports-reference.com/cbb/postseason/men/{}-ncaa.html".format(str(season))
		page.goto(s_r_url, timeout = 0)

		# page.locator("//div[@id='content']//div[@class='switcher filter']//a[text()='East']").click()

		for region in range(1,5):
			page.wait_for_selector("//div[@id='content']//div[@class='switcher filter']/div[{}]/a".format(str(region)), timeout = 0)
			page.locator("//div[@id='content']//div[@class='switcher filter']/div[{}]/a".format(str(region))).click()
			team_selectors = page.locator("//div[@class='switcher_content']/div[{}]//div[@id='bracket']//div[@class='round'][1]/div".format(str(region)))
			num_of_teams = team_selectors.count()
			for x in range(1, num_of_teams+1):
				first_round = page.locator("//div[@class='switcher_content']/div[{}]//div[@id='bracket']//div[@class='round'][1]/div[{}]".format(str(region), x))
				# first_round = page.locator("//div[@class='switcher_content']//div[@id='bracket']//div[@class='round'][1]/div[{}]".format(x))

				temp_text = first_round.inner_text().replace(",", "").replace("\n", ",").strip()
				temp_text = temp_text+"\n"
				tourn_seed_text = tourn_seed_text+temp_text

			tourn_seed_list = tourn_seed_text.split("\n")
			tourn_seed_text = "" #

			for line in tourn_seed_list:
				if line != "":
					formatted_tourn_seed_text = formatted_tourn_seed_text + line.split(",")[0]+","+line.split(",")[1]+","+str(region)+"\n"
					formatted_tourn_seed_text = formatted_tourn_seed_text + line.split(",")[3]+","+line.split(",")[4]+","+str(region)+"\n"
				else:
					pass

		with open("tourn-seeds-{}.csv".format(str(season)), "w") as file:
			file.write(formatted_tourn_seed_text)

		formatted_tourn_seed_text = ""

# 2004-06 need to see which region is what, no post season 2019-2020 season