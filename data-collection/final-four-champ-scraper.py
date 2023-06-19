from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
	browser = p.chromium.launch(headless=False, slow_mo=500)
	context = browser.new_context(viewport={ 'width': 1280, 'height': 56024 })
	page = context.new_page()

	csv_txt = "season,final_four,champ\n"

	for season in range(1993, 2024):
		if season == 2020:
			csv_txt = csv_txt + str(season) + "," + "---" + "," + "" + "\n"
		else:
			s_r_url = "https://www.sports-reference.com/cbb/postseason/men/{}-ncaa.html".format(str(season))
			page.goto(s_r_url, timeout = 0)

			final_four = page.locator("//div[@id='info']/div[@id='meta']/div[2]/p[2]").inner_text()
			final_four = final_four.replace(" and", ",").replace(", ", "-").split(": ")[1].strip()
			print(final_four)
			champ = page.locator("//div[@id='info']/div[@id='meta']/div[2]/p[1]").inner_text()
			champ = champ.split(": ")[1].strip()
			print(champ)

			csv_txt = csv_txt + str(season) + "," + final_four + "," + champ + "\n"

	with open("final-four-champ.csv", "w") as file:
		file.write(csv_txt)