URL = "https://api.cora.fr/api/magasins/167/navigation-content/C-176673"
CLEAN_DATA_PATH= "./products_information.json"
RAW_DATA_PATH="./raw_products_information.json"
PHOTO_DIMENSION = 460
QUERY_PARAMS= {"filters^\\[NW-13260-corapro^\\]^\\[0^\\]": "NW-13260-corapro~0"}
HEADERS = {
    "cookie": "nlbi_2346747=yex0fLiSjQR0jE%2B0rtkoMQAAAADQAq6HXFNCjjPpM%2FAml4oF; visid_incap_2346747=cwXoJ2WzT66CsSAJH81O%2FoNI6mIAAAAAQUIPAAAAAAA7qTj8sP6QYqPtyYVc%2Fd%2Bb; incap_ses_1576_2346747=g3ShDomB6Epj3IVcyRPfFfVI6mIAAAAA4sWW3sM%2F%2Bm2RkLRZ9xJ8sw%3D%3D",
    "authority": "api.cora.fr",
    "accept": "application/vnd.api.v1+json",
    "accept-language": "en,en-US;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "app-id": "1",
    "app-signature": "BROWSER;WEB;103.0.0.0;;1.37.2;1;2;Chrome;864;1536",
    "cache-control": "no-cache",
    "cora-auth": "apidrive",
    "origin": "https://www.cora.fr",
    "pragma": "no-cache",
    "referer": "https://www.cora.fr/",
    "sec-ch-ua": "^\^.Not/A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "uuid": "fcfe2778-ce2d-41c5-bdbd-dd6c9237d7e8",
    "x-d-token": "3:BQsQ4zv/gq8pBrHmlz6d5g==:9uW16rkSg0oXD7Zs6sMR+0RV7V3/Voj60qjQZyoi1jctBji/2rSXe63xAuCo+X6+i70HTE308r9FZBfbPrBbykAP/xvizxOhwsDq69Sv+llSGNwG9xK5ZCE6PaCw3rSu+kPqCHJ5T4aZiOVV46kEU1frTDcOI5DlMJP52wtgoGV6OamXD61WUxVQywgytwXrUa40vgX2cyK8wJwxSHUIKeG1L8zHvmhzRkq5/RzUmg5K8fPcWVsmiT9DqTyqPYuopeiayEpdvDgNS8EaRKqWsdgPwCceAFLIZ++ntkB/adEQhBKdxzqWTOfdCCkiNkVafhcDU8Ig7fEqKQ9Aw0dji2R8pqabVDi1O3r1xg7JWQLKN7I77q7MW1zhUDuOhBsXaEyrGPkgsgNVjrENY8T4+du8sTAWB1jBPL6K6TkwAgo=:PFA6rBQNJnJim0oFAbgL9QEgkfavKZqwmrOZcebRUYY="
}


class Regexes:
    remove_http = "https:\/\/"
    remove_slashes = "\\"
    remove_dimension = "###DIMENSION###"
