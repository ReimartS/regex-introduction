import unittest
from solution import extract_links

input1 = """
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""
input2 = """
<div class="portal" role="navigation" id='p-navigation'>
<h3>Navigation</h3>
<div class="body">
<ul>
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div>
"""

class TestInput(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(extract_links(input1), ["http://www.quackit.com/html/tutorial/html_links.cfm,Example Link","http://www.quackit.com/html/examples/html_links_examples.cfm,More Link Examples..."])

    def test_input_2(self):
        self.assertEqual(extract_links(input2), ["/wiki/Main_Page,Main page","/wiki/Portal:Contents,Contents","/wiki/Portal:Featured_content,Featured content","/wiki/Portal:Current_events,Current events","/wiki/Special:Random,Random article","//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en,Donate to Wikipedia"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
