import app


def test_fetch_wiki_HTML():
    data = app.fetch_wiki_HTML('Germany')
    assert type(data) == str

def test_fetch_random_pages():
    links = app.fetch_random_pages()
    assert len(links) > 0

def test_extract_links():
    result = app.extract_links('Germany')
    assert len(result) > 20
    assert type(result) == list

def test_fetch_all_links():
    result = app.fetch_all_links('Germany',5)
    assert result > 3
