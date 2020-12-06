from typing import List
from typing import Union

from const.sort import Sort
from utils.urls import url_builder


class Browse:
    uri_start = ["buy", "browse"]

    def __init__(self, client):
        self._client = client
        self.search_args = {
            "q",
            "gtin",
            "charity_ids",
            "fieldgroups",
            "compatibility_filter", "auto_correct", "category_ids",
            "filter", "sort", "limit", "offset", "aspect_filter", "epid"
        }
        self.search_results_model=""

    def search(self, **kwargs):
        """
        Search API Reference Page:
        https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search

        q: str,
        gtin: str,
        charity_ids: List[str],
        fieldgroups: List[str],
        category_ids: Union[str, int],
        filter: dict,
        sort: Sort,
        limit: int,
        offset: int,
        epid:Union[str, int]
        """
        api_query_args = dict()
        for arg in self.search_args:
            if arg in kwargs:
                api_query_args[arg] = kwargs[arg]
        uri = url_builder(self.uri_start + [self._client.api_ver] + ["item_summary", "search"],
            **api_query_args)
        return self._client.api_query(uri, "GET", self.search_results_model)
