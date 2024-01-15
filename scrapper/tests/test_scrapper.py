from cora_scrapper import scrap_all_data, clean_data
from .conftest import URL, HEADERS, QUERY_STRING, fake_data


def test_scrap_all_data():
    """
    Tests whether scrap_all_data function can scrap product information from cora.fr
    """
    data = scrap_all_data(URL, HEADERS, QUERY_STRING)
    assert type(data) == dict
    assert len(data)
    assert "data" in data.keys()


def test_clean_data():
    """
    Tests whether clean_all_data can  clean scraped data
    """
    cleaned_data = clean_data(fake_data)
    assert type(cleaned_data) == list
    assert len(cleaned_data)
    assert ["name", "price_in_euros", "price_in_euros_without_taxes", "photo_url"] == list(cleaned_data[0].keys())
