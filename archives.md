---
layout: page
title: 归档
permalink: /archives/
windbell:
  position: top
  items:
    - label: "晚枫集"
      url: /wanfeng/
      color: "#339933"
    - label: "沐雨集"
      url: /muyu/
      color: "#3399cc"
    - label: "雨鱼集"
      url: /yuyu/
      color: "#ff66cc"
    - label: "缘溪集"
      url: /yuanxi/
      color: "#ddddbb"
    - label: "海风集"
      url: /haifeng/
      color: "#006666"
    - label: "小猫集"
      url: /xiaomao/
      color: "#cccc66"
---

<div class="post">
  <div class="post-archive">
  {% for post in site.posts  %}
      {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
      {% capture this_month %}{{ post.date | date: "%B" }}{% endcapture %}
      {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}
      {% capture next_month %}{{ post.previous.date | date: "%B" }}{% endcapture %}

      {% if forloop.first %}
        <h2>{{this_year}}</h2>
        <h3>{{this_month}}</h3>
        <ul>
      {% endif %}

      <li><span class="date">{{ post.date | date: "%B %e, %Y" }}</span><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>

      {% if forloop.last %}
        </ul>
      {% else %}
        {% if this_year != next_year %}
          </ul>
          <h2>{{next_year}}</h2>
          <h3>{{next_month}}</h3>
          <ul>
        {% else %}    
          {% if this_month != next_month %}
            </ul>
            <h3>{{next_month}}</h3>
            <ul>
          {% endif %}
        {% endif %}
      {% endif %}
  {% endfor %}
  </div>
</div>
