import requests
from playwright.sync_api import Page, expect

# command to run with printing:  pipenv run pytest -s --headed

def test_example(page: Page) -> None:
     print("**************FIRST TEST****************************")
     url = 'https://google.co.il'
     page.goto(url)
     page.locator('css=[id="APjFqb"]').fill("Java")
     page.click("input[type=\"submit\"]")
     page.click("div[id=\"rso\"]")

     search_results =  page.locator("h3[class=\"LC20lb MBeuO DKV0Md\"]").locator("span[dir=\"ltr\"]").all_text_contents()
     print(search_results)

     first_result =  page.locator("h3[class=\"LC20lb MBeuO DKV0Md\"]").locator( "span[dir=\"ltr\"]").first.text_content()
     assert first_result.__contains__("Java")

     second_result =  page.locator("h3[class=\"LC20lb MBeuO DKV0Md\"]").locator("span[dir=\"ltr\"]").last.text_content()
     assert second_result.__contains__("Interview") is False



def test_apiTest() -> None:
     print("**************SECOND TEST****************************")
     url = 'https://api.publicapis.org/entries'
     resp = requests.get(url)
     data = resp.json()
     response_list = []

     for item in data['entries']:
         if ('Authentication & Authorization' == item['Category']):
                response_list.append(item['Category'])

     assert len(response_list) == 7
     print(response_list)