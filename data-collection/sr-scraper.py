from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    for season in range(1993, 2024):
        s_r_url = "https://www.sports-reference.com/cbb/seasons/men/{}-advanced-school-stats.html".format(str(season))
        page.goto(s_r_url, timeout = 0)
        page.wait_for_selector("(//li[@class='hasmore'])[6]")
        page.locator("(//li[@class='hasmore'])[6]").click()
        page.click("(//button[@class='tooltip'])[3]")
        temp_txt = page.locator("//pre[@id='csv_adv_school_stats']").inner_text()
        split_on = ",,Overall,Overall,Overall,Overall,Overall,Overall,,Conf.,Conf.,,Home,Home,,Away,Away,,Points,Points,,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced,School Advanced\n"
        txt = temp_txt.split(split_on)[1]
        
        with open("season-stats-{}.csv".format(str(season)), "w") as file:
            file.write(txt)