---
layout: page
title: 归档
permalink: /archives/
index:
  - type: windbell
    position: top
    items:
      - label: "中洲集"
        url: /zhongzhou/
        color: "#cc9966"
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
      - label: "轨边集"
        url: /guibian/
        color: "#bbbbc3"
      - label: "小猫集"
        url: /xiaomao/
        color: "#cccc66"
  - type: coconut
    position: top
    items:
      - label: "0"
        url: /cocoin_0/
      - label: "1"
        url: /cocoin_1/
      - label: "2"
        url: /cocoin_2/
      - label: "3"
        url: /cocoin_3/
      - label: "3a"
        url: /cocoin_3a/
      - label: "4"
        url: /cocoin_4/
      - label: "5"
        url: /cocoin_5/
      - label: "6"
        url: /cocoin_6/
      - label: "7"
        url: /cocoin_7/
      - label: "8"
        url: /cocoin_8/
      - label: "9"
        url: /cocoin_9/
  - type: record
    position: top
    items:
      - label: "月圆"
        url: /yueyuan/
        id: 58
        album: "星与月"
      - label: "星望"
        url: /xingwang/
        id: 94
        album: "星与月"
      - label: "玉蝴蝶·秋梦"
        url: /yuhudie_qiumeng/
        id: 101
        album: "和诗以歌"
      - label: "等桂花开"
        url: /dengguihuakai/
        id: 102
        album: "二〇一九"
      - label: "不等"
        url: /budeng/
        id: 135
        album: "二〇一九"
      - label: "落叶说"
        url: /luoyeshuo/
        id: 136
        album: "二〇一九"
      - label: "雪风"
        url: /xuefeng/
        id: 139
        album: "雪风"
      - label: "画蝶"
        url: /huadie/
        id: 149
        album: "画蝶"
      - label: "星夜谣"
        url: /xingyeyao/
        id: 151
        album: "星与月"
      - label: "溯流沙"
        url: /suliusha/
        id: 156
        album: "和诗以歌"
      - label: "心桥"
        url: /xinqiao/
        id: 158
        album: "雨温"
      - label: "雨暮离别"
        url: /yumulibie/
        id: 159
        album: "雨温"
      - label: "大东"
        url: /dadong/
        id: 162
        album: "和诗以歌"
      - label: "他乡雨"
        url: /taxiangyu/
        id: 163
        album: "雨温"
      - label: "未解忆长安"
        url: /weijieyichangan/
        id: 164
        album: "和诗以歌"
      - label: "来春可拟共兰舟"
        url: /laichunkenigonglanzhou/
        id: 165
        album: "和诗以歌"
      - label: "三潭印月笺"
        url: /santanyinyuejian/
        id: 166
        album: "ue0c"
      - label: "聚少趁江南"
        url: /jushaochenjiangnan/
        id: 168
        album: "和诗以歌"
      - label: "安远"
        url: /anyuan/
        id: 169
        album: "安远"
      - label: "虬江"
        url: /qiujiang/
        id: 170
        album: "上海滩"
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
