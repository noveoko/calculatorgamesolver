import app


def test_fetch_wiki_HTML():
    pass

def test_fetch_random_pages():
    pass

def test_extract_first_link():
    html = '''<p>The <b>baiji</b> (<a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>: <span lang="zh"><a href="https://en.wiktionary.org/wiki/%E7%99%BD%E9%B1%80%E8%B1%9A" class="extiw" title="wiktionary:白鱀豚">白鱀豚</a></span>; <a href="/wiki/Pinyin" title="Pinyin">pinyin</a>: <i><span lang="zh-Latn-pinyin"><span class="unicode haudio"><span class="fn"><span style="white-space:nowrap;margin-right:.25em;"><a href="/wiki/File:Zh-bai2ji4tun2.ogg" title="About this sound"><img alt="About this sound" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png" width="11" height="11" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x" data-file-width="20" data-file-height="20"></a></span><a href="//upload.wikimedia.org/wikipedia/commons/7/7f/Zh-bai2ji4tun2.ogg" class="internal" title="Zh-bai2ji4tun2.ogg">báijìtún</a></span>&nbsp;<small class="metadata audiolinkinfo" style="cursor:help;">(<a href="/wiki/Wikipedia:Media_help" class="mw-redirect" title="Wikipedia:Media help"><span style="cursor:help;">help</span></a>·<a href="/wiki/File:Zh-bai2ji4tun2.ogg" title="File:Zh-bai2ji4tun2.ogg"><span style="cursor:help;">info</span></a>)</small></span></span></i>, <i>Lipotes vexillifer</i>, <i>Lipotes</i> meaning "left behind", <i>vexillifer</i> "flag bearer") is a functionally extinct species of <a href="/wiki/River_dolphin" title="River dolphin">freshwater dolphin</a> formerly found only in the <a href="/wiki/Yangtze_River" class="mw-redirect" title="Yangtze River">Yangtze River</a> in <a href="/wiki/China" title="China">China</a>. Nicknamed "Goddess of the Yangtze" (<a href="/wiki/Simplified_Chinese_characters" title="Simplified Chinese characters">simplified Chinese</a>: <span lang="zh-Hans">长江女神</span>; <a href="/wiki/Traditional_Chinese_characters" title="Traditional Chinese characters">traditional Chinese</a>: <span lang="zh-Hant">長江女神</span>; <a href="/wiki/Pinyin" title="Pinyin">pinyin</a>: <i><span lang="zh-Latn-pinyin">Cháng Jiāng nǚshén</span></i>) in China, the dolphin is also called <b>Chinese river dolphin</b>, <b>Yangtze River dolphin</b>, <b>whitefin dolphin</b> and <b>Yangtze dolphin</b>. It was regarded as the goddess of protection by local fishermen and boatmen in China (Zhou, 1991).<sup id="cite_ref-:0_5-0" class="reference"><a href="#cite_note-:0-5">[5]</a></sup> It is not to be confused with the <a href="/wiki/Chinese_white_dolphin" title="Chinese white dolphin">Chinese white dolphin</a> or the <a href="/wiki/Finless_porpoise" title="Finless porpoise">finless porpoise</a>.
</p>'''
    result = app.extract_first_link(html)
    print(result)
    assert app.extract_first_link(html) == 'River_dolphin'


def test_return_first_link():
    pass

def test_collect_data():
    pass