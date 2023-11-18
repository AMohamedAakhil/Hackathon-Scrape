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
        'cookie': 'rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX18NmUZoBJHwLQFNLNUGZLn9OI8xcYKx66A%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19K8KNuhAuqbzqOkD77MY34KKJBE%2FNUA5w%3D; devfolio_user=eyJ1dWlkIjoiYjA5OTFjOWFiMTRhNGUxNmI3MDg2ZDM2YzZkNWFjMTUiLCJyb2xlcyI6W3siaWQiOjIsInV1aWQiOiI5MTE3YjY0ZTc1YWU0ZDI5YjAyMTRjMGM0N2RjYTBiOCIsIm5hbWUiOiJ1c2VyIiwiZGVzYyI6IkRlZmF1bHQgcm9sZSBmb3IgdXNlcnMiLCJjcmVhdGVkX2F0IjoiMjAxOC0wNi0wN1QxNzozODowNi4wMDBaIiwidXBkYXRlZF9hdCI6IjIwMTgtMDYtMDdUMTc6Mzg6MDYuMDAwWiJ9XX0; devfolio_auth=s%3AeyJhY2Nlc3NfdG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKMWRXbGtJam9pWWpBNU9URmpPV0ZpTVRSaE5HVXhObUkzTURnMlpETTJZelprTldGak1UVWlMQ0owZVhCbElqb2lZV05qWlhOelgzUnZhMlZ1SWl3aWFXRjBJam94TnpBd016UTBNRGN6TENKbGVIQWlPakUzTURBME16QTBOek45Lk9fMm9vNzl0bkVpVmJ2ZWdXQUtONzZ3czZmaElVeU54Rk5KLUhiUjB4MGMiLCJyZWZyZXNoX3Rva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFkV2xrSWpvaVlqQTVPVEZqT1dGaU1UUmhOR1V4Tm1JM01EZzJaRE0yWXpaa05XRmpNVFVpTENKMGVYQmxJam9pY21WbWNtVnphRjkwYjJ0bGJpSXNJbWxoZENJNk1UWTVOek01TkRjeU5pd2laWGh3SWpveE56STRPVE13TnpJMmZRLkNpc0oxUVp6QlRjRU5BSFRpbEM1T3FZTDkyRUxPRDlFa1BXVU1HelNrV3cifQ.W4ij%2F6KMUPCV3uxnV5QEJkKP1zPdrVhsnE%2B4uGBYGjU; rl_user_id=RudderEncrypt%3AU2FsdGVkX18uIdn2unwGAuSaZAAEaON2NE274A0gwSABxx9vg2pI4kPtUChG7jqcwQgska%2B8dTzbOPdPGd0vig%3D%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2F7evzD3%2Fu3Jer5axbW3MSMqx11cp%2BCAtY%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18RNpnkYEj7VbjbtY0vscvF1fmLJ94I7D0%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18LqYo1Q8b2kmgcxe7f%2FTbXq6ifReRzecw%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Fqpdxf%2FoCESjYuIr8zoRBAmOx7K%2BXmon%2FKNiJUDzltJjXT7VseMoFy7%2Fa66lfOYAyF7XKwKp2tzw%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2F9rJYLIGrkDnP7PWWKVhPXWI8oWLCV%2FeOGNHBWJNz5UGw%2FPrXCNbr0%2BlGXT82XhQ1pbJoEkK6syRO%2FM1y5qXJRPBmawlf3qXCdv8u6uIWsT6NmnMb10fwBZaGV%2FXuUgSjY5OnKRFy0RQ%3D%3D',
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
        'cookie': 'AWSALB=Z35Zx0xwvClooNc8GsQ5JMu1tE7aA6hnbNVCp3oVrBjmyRwa1/wY0jGQE+y11ZBAlqCuGafX09xz60C+KBfb6VFVt2k8g66Is2WyJPwSDPFlSvClz8lCgPOh5uLn; AWSALBCORS=Z35Zx0xwvClooNc8GsQ5JMu1tE7aA6hnbNVCp3oVrBjmyRwa1/wY0jGQE+y11ZBAlqCuGafX09xz60C+KBfb6VFVt2k8g66Is2WyJPwSDPFlSvClz8lCgPOh5uLn; _devpost=N2VQRkUyaThpL291MmVDQXNEVE45UGpWRytQK3dhN0NRZlRyTG80MTMvaW1kSVF0ckpJdVN5Q3c1dWdxNzR4R2hTNXA2UG1GbDBreEtyTlJBdExCNVBZV0I3Q0dpSVUwU2FGOGlxV0t1MXc1YjdxZUpVM3JPZEwzTnBOOTFTYUNFYkhoc0pnUk1qTHlpKzdJczRwSmxTTnJlbFhjR1daTU1QcUJLNlpyUVFmaVFDMmVkS3U0b3ZHWmpYcWEwVmN6NENiRG96THE0OVY4bzJpQms0VGhkY0FvTVI3eXN0SzZXSnU2a29Rd0h6NVlDVnRMdSt6U3FPRXZyRGEwY0NGaFNiQXREMDVhenBIZVdSSmxiNUtBdzZmRTFvNjdqMjhRc0thT3o1QXZCY1RQcDZMRW1HU29QUWNUWWRORlRPaDlCZlNrS2xSUFRhTmZab3JweWJOM3RMTXpmYmUvVDBjTklrK2g3L2NZRHhQeHRjSWk4Znc2Z3k1M3pQaFZOazRpcEZYTk9OSHZqVTIyWCtkUTBkNVNGK1NVSFB5TlNVMjB2NlBnZHJ2NEJUaz0tLUFNQkRhcTRnblZ2NW9SQWx3MHlFYXc9PQ%3D%3D--f7bf95c18d286327037ecf9d34f0dfcf33c5b757; mp_1c828346e9fae00dbc3a117657f65895_mixpanel=%7B%22distinct_id%22%3A%20%225d78a18cc97ea62ae30ba180f10ed411e74589660aee23628e4311d3328087049016b5d423f293b01efbf74e2af95bbc1885%22%2C%22%24device_id%22%3A%20%2218be4783a22ad2-0f8818eff7c605-26031051-1fa400-18be4783a22ad3%22%2C%22%24user_id%22%3A%20%225d78a18cc97ea62ae30ba180f10ed411e74589660aee23628e4311d3328087049016b5d423f293b01efbf74e2af95bbc1885%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _gcl_au=1.1.1385068152.1700345167; _ga_0YHJK3Y10M=GS1.1.1700345166.1.0.1700345166.0.0.0; __mp_opt_in_out_1c828346e9fae00dbc3a117657f65895=1; _ga=GA1.2.1870426334.1700345167; _gid=GA1.2.1879761458.1700345168; _gat_UA-2233558-21=1; AWSALB=e3f1EckDVfLFbK6jZbjFmLeG2yFp0LVEb3ixc36M41gMjoJk+E8NaGMBOk2Nbuv0fUQES5MyQ3rB81vvSZusTwsmuHECNr2Ql5PRPbZX5rHMzHGMnruHsfDhay2D; AWSALBCORS=e3f1EckDVfLFbK6jZbjFmLeG2yFp0LVEb3ixc36M41gMjoJk+E8NaGMBOk2Nbuv0fUQES5MyQ3rB81vvSZusTwsmuHECNr2Ql5PRPbZX5rHMzHGMnruHsfDhay2D; _devpost=N3laQ2c1NWVITEpVME1sazlSUHpMVVNCQi9uZVRvbDhWb0t5Q1lPS0Y5cHFycE5tSHEzbEtOT0czYU9uaE9xOS9YeW5vVXFNRmIrL2NJZXlEd0ExbHV4ZmdxNW9tN1ZsWlV6Tm1UT2hCZnY3UWdhc1ROZTEwc0dZcWg0TDVqcUpHREZwTURXdHRiWE04SktSSlBJQmdKeDVrVUV6VXQ5VEF5YUVyZ3Nia2J1WG9ZSXM2U0ZYR0RSMmd0TERobk5HMXpLRTVpaWxCbm1uVVF0STl2VzB5N0paa2E4UkVzRHZrMzlFajNEVHF4SGRxNEYwQjVTd2o2MVJXVEV1eTJhVUdwYnI4T1hlYnZEbUxmbU9IdkxtMVU4c2NaV2hvekFpaXhjaVdpb3JvTzVRd1hQaGtoWGFGcWZ5L3ZibU9rbFVXTXFtL1N3TENmeDNVZTZTYnQ0YTl2TzVKNVowR0swUVNZZXFrU3pPeDVjeU5ZZWxCemNER0NsbU5UN3NCUTBaNzE3YXB3VXB1U0p2Y3MwZXVNd2VJUjkxOWlaeUg0YWlEQlE1WWg2RnhDdz0tLXNNRWQvQkRKVGE0ZkdKYUR6b3djUkE9PQ%3D%3D--43b66423977843a6c57705995a8bdd928c66552f',
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

        



