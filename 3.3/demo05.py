html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
print(type(items))
print(items)

print("-------------------------------------")
print("find方法的查找范围是节点的所有子孙节点------")
lis = items.find('li')
print(type(lis))
print(lis)

print("-------------------------------------")
print("children方法只查找子节点----------------")
lis = items.children()
print(type(lis))
print(lis)
lis = items.children('.active')
print(lis)

print("-------------------------------------")
print("parent方法获取某个节点的父节点------------")
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

print("-------------------------------------")
print("parents方法获取某个节点的所有祖先节点------")
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)
parents = items.parents('.wrap')
print(parents)

print("-------------------------------------")
print("siblings方法获取某个节点的兄弟节点------")
items = doc('.list .item-0.active')
siblings = items.siblings()
print(type(siblings))
print(siblings)
siblings = items.siblings('.active')
print(siblings)
