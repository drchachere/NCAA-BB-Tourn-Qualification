from playwright.sync_api import sync_playwright
import pandas as pd
import sys
from io import StringIO

df = pd.DataFrame()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={ 'width': 1280, 'height': 56024 })
    page = context.new_page()

    for season in range(1993, 2024): 
        sr_url = "https://www.sports-reference.com/cbb/seasons/men/{}-standings.html".format(str(season))
        page.goto(sr_url, timeout = 0)
        tw_elements = page.locator("//div[@class='table_wrapper']")
        num_of_tw = tw_elements.count()
        for x in range(1,num_of_tw+1):
            page.wait_for_selector("(//div[@class='table_wrapper'])[{}]".format(x))
            temp_selector = page.locator("(//div[@class='table_wrapper'])[{}]".format(x))
            temp_selector.locator("//li[@class='hasmore']//span[contains(text(),'Share & Export')]").click()
            temp_selector.locator("//li[@class='hasmore']//div//ul//li//button[@type='button'][normalize-space()='Get table as CSV (for Excel)']").click()
            temp_txt = temp_selector.locator("//pre").inner_text()
            split_on = ",,,Overall,Overall,Overall,,Conference,Conference,Conference,,PTS/G,PTS/G,,SRS,SRS,,Polls,Polls,Polls,,\n"
            csv_txt = temp_txt.split(split_on)[1]
            df_temp = pd.read_csv(StringIO(csv_txt))
            # with open("temp.csv", "w") as file:
            #     file.write(csv_txt)
            # df_temp = pd.read_csv("temp.csv")
            df_temp.reset_index(drop=True, inplace=True)
            df = pd.concat([df, df_temp], ignore_index=True)
            # print(df_temp)

        df.to_csv("conf-rankings-{}.csv".format(str(season)))
        df = pd.DataFrame()

# print(df)