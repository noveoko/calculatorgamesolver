import FetchData, App

def test_checkIfDisambiguation():
    normal_page = FetchData.checkIfDisambiguation('Germany')
    disamb_page = FetchData.checkIfDisambiguation('Activity')
    assert not normal_page
    assert disamb_page == 'disambiguation_page'

def test_isList():
    alist = FetchData.isList('List_of_record_labels:_A–H')
    nolist = FetchData.isList('Germany')
    assert alist
    assert not nolist

def test_findNearestWord():
    perfect_match = FetchData.findNearestWord('abc',[['abc','alph.html'],['RZZ32','abc.js']])
    distant_match = FetchData.findNearestWord('abc',[['B$RZ','d.txt'],['^^sfdz+Z)','a.txt']])
    assert perfect_match[0] == 1.0
    assert distant_match[0] < 0.5

def test_fetch_wiki_HTML():
    page = FetchData.fetchWikipediaHTML('Sarwark')
    assert 2000 < len(page) < 3000

def test_randomWikipediaPages():
    results = FetchData.randomWikipediaPages()
    assert len(results) > 0

# def test_topicCrumbtrail():
#     results = FetchData.topicCrumbtrail('Germany')
#     assert len(results) > 10 and type(results) == list