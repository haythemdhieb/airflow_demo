import os
import sys

sys.path.insert(0, os.getcwd())
URL = "https://api.cora.fr/api/magasins/115/navigation-content/C-176673"
PHOTO_DIMENSION = 460
QUERY_STRING = {"filters^\\[NW-13260-corapro^\\]^\\[0^\\]": "NW-13260-corapro~0"}
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

fake_data = {
  "data": {
    "type": "navigation-content",
    "id": "C-176673",
    "attributes": {
      "title": "Hygiène,soin et accessoires chat",
      "description": "Notre rayon animalerie vous propose de nombreux produits d'alimentation et d'accessoires d\u00e9di\u00e9s aux animaux de compagnie et \u00e0 leur bien-\u00eatre.",
      "layout_type": "Grid",
      "pim_category_code": "Hygiène,soin_et_accessoires_chat",
      "product_list": {
        "data": [
          {
            "type": "produits",
            "id": "1004029",
            "attributes": {
              "designation": "Riga sachets plastique",
              "description": "Les sachets plastiques aident à éviter l'usure du bac.",
              "marque": "RIGA",
              "prix": "5.99",
              "prix_ht": "4.99",
              "taux_tva": "20.00",
              "categorie_id": "1347",
              "categorie_parente_id": "1329",
              "qte_max_panier": 20,
              "visuel": "https:\/\/www.cora.fr\/media\/produit\/1659330024\/###DIMENSION###\/R13\/iZQBIWIWILhxwrwreziZwrIWhxOqQB.jpg",
            }
          }
        ]
      }
    }
  }
}
