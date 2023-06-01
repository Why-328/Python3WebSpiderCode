html = """
<div class="wrap">
    Hello,World
    <p>This is paragraph</p>
</div>
"""

from pyquery import PyQuery as pq

doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').append('123')
print(wrap.text())
wrap.find('p').prepend('123')
print(wrap.text())
wrap.find('p').empty()
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
