import json
import re

from loguru import logger
from requests import request
from requests.exceptions import RequestException

from configurations import Regexes, HEADERS, QUERY_STRING, URL, PHOTO_DIMENSION


def scrap_all_data(url: str, header: dict, query_params: dict) -> dict:
    """
    Scraps all data from a given URL
    Args:
        url(str): url from which we scrap the data
        header(dict): header of the request
        query_params(dict): query parameters of the request
    Returns:
        data(dict): a dict containing all scraped data
    """
    data = dict()
    try:
        response = request("GET", url, headers=header, params=query_params)
        data = response.json()
    except RequestException as error:
        logger.error("Something went wrong while fetching data from the url {} \n".format(url))
        logger.error(str(error))
    return data


def clean_photos_url(photo_url: str, photo_dimension: str) -> str:
    """
    Reformat photo url
    Args:
        photo_url(str): url of the photo to be reformatted
        photo_dimension(str): dimension of the photo
    Returns:
        photo_url(str): reformatted url

    """
    photo_url = re.sub(Regexes.remove_http, "", photo_url)
    photo_url = photo_url.replace(Regexes.remove_slashes, "")
    photo_url = re.sub(Regexes.remove_dimension, str(photo_dimension), photo_url)
    return photo_url


def clean_data(scraped_data: dict) -> list:
    """
    Get all products from the scrapped data and reformat attributes
    Args:
        scraped_data(str): dict containing scraped data
    Returns:
        products(list): a list containing all product with their relevant information

    """
    products = []
    try:
        for product in scraped_data["data"]["attributes"]["product_list"]["data"]:
            photo_url = clean_photos_url(product["attributes"]["visuel"], PHOTO_DIMENSION)
            product_info = {"name": product["attributes"]["designation"],
                            "price_in_euros": float(product["attributes"]["prix"]),
                            "price_in_euros_without_taxes": float(product["attributes"]["prix_ht"]),
                            "photo_url": photo_url}
            products.append(product_info)
    except KeyError as error:
        logger.error(str(error))
        logger.error("The data scrapped has an invalid schema")
    return products


def store_data_json(products_infos: list) -> None:
    """
    Stores all products' information in a json file
    Args:
        products_infos(list): list containing products information

    """
    with open('product_information.json', 'w') as file:
        json.dump(products_infos, file)
