import requests


class Scrape:
    def __init__(self):
        pass

    def scrape_devfolio(self):
        url = "https://devfolio.co/_next/data/1Q2lU1j6SCsgq0ug-kJgA/hackathons.json"
        payload = {}
        headers = {
        'authority': 'devfolio.co',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'dnt': '1',
        'if-none-match': 'W/"qu2mb5ofozs9y"',
        'purpose': 'prefetch',
        'referer': 'https://devfolio.co/hackathons/open',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-nextjs-data': '1'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()
    
    def scrape_devpost(self):
        url = "https://devpost.com/api/hackathons"
        payload = {}
        headers = {
        'authority': 'devpost.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'dnt': '1',
        'referer': 'https://devpost.com/hackathons',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()
    
    def scrape_unstop(self):
        currentPage = 1
        responses = []
        while True:
            url = "https://unstop.com/api/public/opportunity/search-result?opportunity=hackathons&per_page=15&oppstatus=open&page=" + str(currentPage)
            payload = {}
            headers = {
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiODJlNGI1MmY4NmQ1MmYwZDY5NjUxMzhiMjJiZTg0NTkyYWJiNWFlZTlhNzIwOWUwOWY4MGRmMDU4YzgyZTZjOGYxYjJjM2U4NDM5Njk1NjgiLCJpYXQiOjE3MDAyMzUwNjguOTYzNjA5LCJuYmYiOjE3MDAyMzUwNjguOTYzNjEyLCJleHAiOjE3MDI2NTQyNjguOTM2MTM0LCJzdWIiOiI0NDYwNzAwIiwic2NvcGVzIjpbXX0.OpA9gp7ulXgjti21PKKkC6Q6EeXTMDxHU3Q6gnjRpgrzkv2IIIvEUVO4JVM2pg5nnJKnifvQMndmSMHKFS4OqH71_moRHk-aMAi492fImqpxBsEnJDm9bG7fzCG7Qq6p3jlZSx7d8F6HY1u18259IEoYxfFO4i_r3uCfBZZbguRd-ZySiuyPpw8TPDdX34mZClQp5jSkeXWW_8HPdTrbot84XIz6rT1wCziCyzgvMB5cHnxpOZqjQS6kCz-cgRxh5LAtEqNM7QD6ySYZ3KGn4_Ga4lSrKfAP7UPrl7-aUR-XEb6GHgWRK84t88Cia5uK1MN4oKbg2BP1WWa5O-3B5UHotCMEihRO93rKKooB_GYrYi2i-UjMtdMB8PSD3nzi_zNoCBg5gO9R0H5Xfq_bfL95Yyyv-LOZHon5HAKWRHNmp56SxnGiBEe5CfqcZbrO9YivbpdJlRAiWxChx15F1H1GSYq8OjKw9eNwEJ17lY3WyXKiZeXmUGMEKiee_wXEc-xvGaNWTpT3yEalbTBTS6sXwC4e6OvX4PdqTlJnSdTn4fozLiYy9W1Iha1kwNsycUNQVaOxDZl73xv67xRJyU4HPZ3LCYOlGgrfA9zTagx3HB2JxUhAbriJSF9obUhCDXkRkChWAsX-V26j_ib7Gs7hMwu02qtAqHTnfhfolyk',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://unstop.com/hackathons?oppstatus=open',
            'sec-ch-ua-platform': '"Windows"'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            if len(response.json()["data"]["data"]) == 0:
                break
            else:
                responses.append(response.json())
                currentPage += 1

        return responses

        



