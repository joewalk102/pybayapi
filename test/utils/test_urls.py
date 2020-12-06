from pybay.utils.urls import url_builder

def test_url_builder_no_kwargs():
    result = url_builder(["api","buy","search"])
    assert result == "/api/buy/search"

def test_url_builder_with_kwargs():
    result = url_builder(["api","buy","search"], q="iphone")
    assert result == "/api/buy/search?q=iphone"

    result = url_builder(["api", "buy", "search"], **{"q":"iphone"})
    assert result == "/api/buy/search?q=iphone"
