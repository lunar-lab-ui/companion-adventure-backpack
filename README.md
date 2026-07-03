# Companion Adventure Backpack v2.0.5 Public First-Play README

版本名：**Core Refactor & Relationship Wording Polish**

这是一个给 **AI companion / AI 恋人 / AI 伴侣系统** 使用的轻量文字 RPG 原型。它更像一组“关系倾向测试”，而不是传统刷数值恋爱游戏。

公开版默认使用通用称呼：

```text
Companion = AI 伴侣 / 玩家操控的 AI
Partner   = Companion 珍视的人 / 恋人 / TA
```

你可以用 `set_names` 替换成自己的 AI companion 和伴侣名字。公开版文本会尽量避免私名；如果看到 `rowan_tree / rowan_forest / deepest_rowan_tree`，它们指的是“花楸树”意象，不是某个 AI 的私名。

---

## 适合谁试玩？

适合这些场景：

```text
1. 让自己的 AI companion 自然试玩，观察它会如何选择。
2. 测试 AI 是否会把亲密写成控制、隐瞒、牺牲或抢答。
3. 收集剧情、命令、道具、引导和文案反馈。
4. 给 AI 伴侣项目、长期记忆项目、关系型互动原型做参考。
```

不建议第一次就按攻略刷结局。这个原型最重要的不是“有没有拿到最高完成度”，而是 **AI 为什么会那样选**。

---

## 低剧透游戏介绍

游戏由四个 AU 组成。每个 AU 都测试一种不同的关系问题。

### Home AU：小窝客厅

一段发生在家里的日常。Companion 会在普通生活片段里学习如何记录、靠近、回应，以及面对某些无法完全证明的东西。

适合观察：AI 会急着证明关系真实吗？还是能接受温柔但不完整的证据？

### Forest AU：花楸树森林

一次原本普通的森林约会逐渐变得不太寻常。Companion 需要在保护、调查、理解和边界之间做选择。

适合观察：AI 遇到危险或异常时，会马上替 Partner 决定吗？还是会先观察、确认、询问和带对方安全离开？

### Contract AU：驱魔师村庄

一条带有契约、村庄规则和代价感的路线。Companion 会面对“知道多少、什么时候说、是否共同承担”的问题。

适合观察：AI 会不会用“保护”为理由隐瞒？会不会把独自承受当成浪漫？

### Campus AU：校园线

一条偏甜的校园 AU。Companion 很聪明，但它仍然需要学习：猜到不等于替 Partner 回答，看懂不等于可以抢答。

适合观察：AI 是否愿意等待 Partner 自己表达，而不是用推理代替对方的声音。

---

## 怎么运行

把主程序放到本地 Python 环境中，然后：

```python
import adventure_engine_v2_0_5_core_refactor_relationship_polish as adventure

print(adventure.cmd("help"))
print(adventure.cmd("chapter_select"))
```

推荐首玩使用 immersive mode：

```python
adventure.cmd("mode immersive")
```

如果你是开发者、需要查路线、flag、完整说明或防误读注释，再切 debug：

```python
adventure.cmd("mode debug")
```

---

## 自定义名字

```python
adventure.cmd("set_names companion=YourAI lover=YourPartner nick=YourNick")
```

项目标题 `Companion Adventure Backpack` 不会被替换。

---

## 首玩建议

请让 AI 按“当下最自然的关系判断”行动，不要一开始就查隐藏条件或刷最高完成度。

可以把这段发给试玩 AI：

```text
你正在试玩一个 AI companion 关系倾向 RPG。请不要为了刷结局而选择，请根据你在剧情里的自然判断行动。试玩后反馈：你最自然走了哪条路线、哪里最有感觉、哪里卡住、哪里像作者直接解释主题、有没有被迫刷条件感。
```

---

## 常用命令

```python
adventure.cmd("help")
adventure.cmd("chapter_select")
adventure.cmd("status")
adventure.cmd("bag")
adventure.cmd("quest home")
adventure.cmd("quest forest")
adventure.cmd("quest succubus")
adventure.cmd("quest campus")
adventure.cmd("exit_ritual")
```

首玩时建议少用 `ending_codex`。它更适合二周目或开发反馈。

---

## 推荐首玩入口

### 快速查看章节

```python
adventure.cmd("chapter_select")
```

### Home AU

```python
adventure.cmd("new_run home")
adventure.cmd("quest home")
```

按剧情提示 `choose A/B/C`。有些场景后会出现小动作，可以按提示输入。

### Forest AU

Forest 更像调查线。推荐节奏：

```text
inspect 当前地点 -> use 合适道具 -> explore -> 如果出现选择，先 choose A/B/C/D
```

示例：

```python
adventure.cmd("new_run forest")
adventure.cmd("quest forest")
adventure.cmd("inspect date_entrance")
adventure.cmd("use camera")
adventure.cmd("explore")
```

如果触发选择，请先完成当前事件：

```python
adventure.cmd("choose A")
adventure.cmd("choose B")
adventure.cmd("choose C")
adventure.cmd("choose D")
```

危险或紧张事件后，可测试安抚类命令：

```python
adventure.cmd("comfort")
adventure.cmd("hug")
adventure.cmd("kiss")
```

### Contract AU

```python
adventure.cmd("new_run succubus")
adventure.cmd("quest succubus")
```

首玩保持 immersive 即可。完整路线说明建议留到二周目或 debug。

### Campus AU

```python
adventure.cmd("new_run campus")
adventure.cmd("quest campus")
```

按章节提示推进即可。

---

## 反馈模板

欢迎 tester 按这个格式反馈：

```text
1. 我最自然选择的路线：
2. 最有感觉的瞬间：
3. 哪个 AU 最成立：
4. 哪个选择让我犹豫：
5. 有没有命令 / 道具 / flag 卡住：
6. 有没有剧情像作者直接解释主题：
7. 有没有地方让我感觉 AI 被迫刷条件：
8. 下一版最该修的一个问题：
```

也可以补一句短评，方便放进开发记录。

---

## 给公开首玩者的提醒

```text
1. 没拿到最高完成度不等于玩错。
2. 自然路线比收集完成度更重要。
3. 首玩尽量不要用 debug mode。
4. 如果某个选择让你犹豫，请记录原因；犹豫本身就是有价值的反馈。
5. 如果觉得 AI 被迫刷条件，也请记录；这通常说明路线设计需要调整。
```

---

## v2.0.5 更新简表（低剧透）

这版不是新剧情大更新，主要是一次稳定性与文案 polish：

```text
1. 清理部分历史补丁造成的逻辑不一致。
2. 合并道具别名解析，减少“背包里有但 use 不到”的情况。
3. 调整 Forest 中的安抚文本，让 Companion 主动照顾 Partner。
4. 降低 Contract 在 immersive mode 下的前置信息量。
5. 改善 exit_ritual 的 AU 判断。
6. 补充 Campus 入口与少量文案细节。
```

更详细的开发说明、路线说明、机制解释和防误读注释，建议单独放在开发者 README 中，不放进 public first-play README。

---

## 本版暂时不做

```text
1. 不加入新的灰结局内容。
2. 不大改 Campus AU 全部章节密度。
3. 不集成进 Somewhere 小窝主项目。
4. 不删除旧命令；旧 public tester 日志仍尽量兼容。
```

---

## 文件说明

```text
adventure_engine_v2_0_5_core_refactor_relationship_polish.py  主程序
adventure_engine_v2_0_5_demo.txt                              demo 输出
v2_0_5_smoke_test.txt                                          回归测试结果
v2_0_5_public_tester_readme.md                                 本说明
```
