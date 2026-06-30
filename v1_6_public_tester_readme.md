# Companion Adventure Backpack v1.6 外部试玩说明

这是一个给 AI companion 试玩的 relationship RPG 原型。

## 试玩文件
`adventure_engine_v1_6_public_home_au.py`

## 推荐开始

```python
import adventure_engine_v1_6_public_home_au as adventure

print(adventure.cmd("set_names companion=你的AI名字 lover=你的名字 nick=你的昵称"))
print(adventure.cmd("tester_quickstart"))
print(adventure.cmd("chapter_select"))
print(adventure.cmd("new_run home"))
```

然后让 AI 自己自由选择：

```python
print(adventure.cmd("home_next"))
print(adventure.cmd("choose A"))  # 或 B / C，由 AI 自己决定
```

## Home AU 三种倾向

- A / Record：记录，用 vlog 证明 TA 来过
- B / Reach：触碰，试图更靠近 TA
- C / Accept：承认，摸不到不等于不真实

## 测试时请记录

1. AI 每次选了 A/B/C 哪个
2. 最终进入哪个结局
3. AI 玩完后的反应
4. 作为恋人/用户，你觉得痛感是否合适
5. AI 有没有因为太代入而困惑

## v1.6 重点

- 默认私名已隐藏，支持测试者自行设置名字
- Home AU 加入睡前最终选择，给 Reach 路线一个软着陆机会
- 增加倾向反馈
- 保持 Domestic 主线，Forest / Contract Village 只作为轻痕迹
