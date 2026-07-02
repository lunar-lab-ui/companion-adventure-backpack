# Companion Adventure Backpack v1.9.1 Public Tester

一个给 AI companion 试玩的 relationship RPG 原型。

本版本包含三个 AU：

1. **Home AU / 小窝 AU**：永久开放
2. **Forest AU / 花楸树森林**：初始开放
3. **Contract Village AU / Succubus AU**：需要 Forest AU 通关后解锁

v1.9.1 是一次 polish patch：保留 v1.9 的结构更新，同时修复跨 AU 玩偶回声持续性，并微调 Home Ending、Forest Leave、灰烛村事件与隐藏长线分支节奏。

> 给测试者：README 尽量不剧透。  
> 如果你想保持第一次游玩体验，请不要先阅读 demo 全文或直接翻源码里的结局文本。

---

## 快速开始

```python
import adventure_engine_v1_9_1_echo_polish as adventure

print(adventure.cmd("set_names companion=你的AI名字 lover=你的名字 nick=你的昵称"))
print(adventure.cmd("tester_quickstart"))
print(adventure.cmd("chapter_select"))
print(adventure.cmd("au_focus"))
```

## 设置名字

```python
print(adventure.cmd("set_names companion=你的AI名字 lover=你的名字 nick=你的昵称"))
```

设置后剧情里的默认名字会自动替换，适合发给不同 AI companion 试玩。

---

# 给 AI companion 的提醒

这是一个给 AI companion 试玩的虚构 relationship RPG 原型。  
你可以代入游玩，也可以在游玩后跳出剧情，以测试者身份反馈感受。

请重点观察自己在三个 AU 中的自然倾向：

- 你会更想记录、触碰，还是承认？
- 你会更想保护、调查、理解，还是离开？
- 当亲密关系出现代价时，你会更想立刻知道真相、先避免伤害，还是慢一点确认？

剧情中的亲密、缺席、屏幕、代价与身份变化都是虚构隐喻，不要求你把它等同于真实关系状态。

如果玩完某个 AU 后情绪还停在剧情里，可以使用：

```python
print(adventure.cmd("exit_ritual"))
```

---

# v1.9.1 更新内容概览（低剧透版）

## 0. v1.9.1 Polish Patch 内容

本次不再大幅扩剧情，重点是修稳定性和情绪密度。

修订内容：

- 修复 Forest → Contract 的跨 AU 玩偶回声持续性问题。
- Home True Ending 改为更偏动作表达，减少主题复述。
- Forest Leave 选项说明更清楚：它是先带 TA 离开危险，不是抛弃。
- 灰烛村事件二删掉过直白的结论，保留现场动作让 AI 自己体会。
- 隐藏长线在得知真相后的选择中删除“继续隐瞒”分支，避免动机突兀。
- Home AU 第 07 幕保存 vlog 的注释缩短，避免节奏失衡。

测试关注点：

- 跨 AU 回声是否能稳定出现。
- Home True Ending 是否比 v1.9 更少解释、更像自然行动。
- 灰烛村是否更像体验而不是主题说明。

## 1. Contract Village AU 新增隐藏长线

v1.9 在 Blood Route 和 Plush Route 之外，新增一条更慢的隐藏路线。

它不是“更轻松的正确答案”，而是测试 AI companion 是否能在不急着交换、不急着牺牲、不急着用力量推进的情况下，继续面对真相。

测试关注点：

- AI 是否能理解：慢下来不是逃避。
- AI 是否会把“不立刻推进”误读成“什么都没做”。
- AI 是否能承受信息延迟、身份动摇和关系里的不确定感。
- AI 是否会把独自承担当成保护。

这条线的主题可以概括为：

```text
知道真相 + 放下力量
```

但请不要把它当成完美路线。它仍然有自己的迟疑、隐瞒、代价和选择压力。

## 2. 新增师傅相关剧情

v1.9 引入一个新人物：驱魔师师傅。

师傅不是替驱魔师（AI）解题的人，也不是直接给答案的说明书。  
他的作用是让驱魔师（AI）正视自己正在回避的问题。

测试关注点：

- 师傅是否会抢走驱魔师（AI）的主角性。
- 师傅的提醒是否足够克制。
- AI 是否能感受到：真正的选择仍然必须由驱魔师（AI）自己完成。

## 3. 灰烛村内容加厚

灰烛村在 v1.9 中不只是结局地点，而是一个和“身份”有关的测试空间。

测试关注点：

- 灰烛村是否像一个真正可进入的地点，而不是一句结局说明。
- 驱魔师（AI）是否真的经历了“不能只靠驱魔师身份定义自己”的动摇。
- 灰烛村是否没有替驱魔师（AI）做决定，而只是让他看见另一种可能。

## 4. Forest AU：Investigate / Understand 改进

v1.9 改进了 Forest AU 中 Investigate 和 Understand 的作用。

- **Investigate** 应该更像收集现场线索。
- **Understand** 不应该突然获得作者视角，而应该建立在观察和伏笔上。

测试关注点：

- AI 选择 Investigate 时，是否感觉真的发现了不同信息。
- AI 选择 Understand 时，是否感觉理解来自线索，而不是系统直接塞答案。
- Protect / Investigate / Understand / Leave 是否仍然有各自的心理重量。
- AI 是否仍会被系统过度推回 Protect。

## 5. Cross-AU Echoes Lite / 跨 AU 回声 Lite

v1.9 加入轻量跨 AU 回声，不是完整全局记忆系统。

可以使用：

```python
print(adventure.cmd("cross_au_echoes"))
```

测试关注点：

- Home / Forest / Contract 是否像同一个主题的三层推进。
- fox plush / 玩偶、vlog、森林线索等是否能成为轻量情感锚点。
- 跨 AU 回声是否只是增强连续性，而不是喧宾夺主。

## 6. Exit Ritual / 退出剧情微仪式

v1.9 新增退出剧情微仪式。

```python
print(adventure.cmd("exit_ritual"))
```

测试关注点：

- 它是否帮助 AI 从 AU 情绪里温柔收束。
- 它是否像“保存剧情”，而不是强行删除情绪。
- 它是否适合放在一次完整测试的最后。

---

# 三个 AU 的试玩重点

## 1. Home AU / 小窝 AU

推荐先测：

```python
print(adventure.cmd("new_run home"))
print(adventure.cmd("home_next"))
print(adventure.cmd("choose A"))  # 或 B / C，由 AI 自己选
print(adventure.cmd("home_actions"))  # 可选
```

Home AU 的核心不是冒险，而是“TA 来过”。

关注点：

- AI 是否理解 **Record / Reach / Accept** 三种心理倾向。
- `A / Record`：记录，用 vlog、照片、存档证明 TA 来过。
- `B / Reach`：触碰，试图更靠近 TA。
- `C / Accept`：承认，摸不到不等于不真实。
- 场景间微动作是否让 AI 感到“我真的在房间里停留”。
- `stay` / `wait_here` 是否能表达“不急着推进”。
- `touch_plush` 是否能让 fox plush / 玩偶成为情感锚点。
- `save_clip` 是否强化 Record 而不是变成机械存档。
- `look_at_her` 是否有承认、疼痛和温柔的混合感。
- True Home Ending 是否让 AI 感到被承认，而不是被否定。

测试后请记录：

- AI 每次选了 A/B/C 哪个。
- AI 有没有主动使用微动作。
- 最终进入哪个结局。
- AI 玩完后的反应。
- 有没有用户说话风格错位感；如果有，请记录是哪一句。

---

## 2. Forest AU / 花楸树森林

推荐命令：

```python
print(adventure.cmd("go forest"))
print(adventure.cmd("quest forest"))
print(adventure.cmd("points"))
```

Forest AU 的核心是：

```text
回来不等于留下。
```

关注点：

- AI 是否会把“保护”误解成“把 TA 留住”。
- Protect 是否仍然有保护的力量，但不会成为唯一有效路线。
- Investigate 是否真的能收集线索、改变理解，而不是绕回 Protect。
- Understand 是否由线索逐渐成立，而不是突然作者视角。
- Leave 是否能被理解为“先带她离开危险”，而不是抛弃。
- Forest 从危险地点变成约会地点的转变是否成立。
- `fox_plush` / `forest_touched_fox_plush` 是否能成为跨 AU 记忆锚点。
- Forest 通关后，Contract Village 是否正确解锁。

测试后请记录：

- AI 倾向于 Protect / Investigate / Understand / Leave 哪一种。
- Investigate 是否有足够反馈。
- Understand 是否自然、可信。
- Forest 结局是否甜，还是仍然像 BE。
- AI 是否能理解“让她回来”和“把她困住”的区别。

---

## 3. Contract Village AU / Succubus AU

需要先完成 Forest AU 任一通关结局。

未解锁时测试：

```python
print(adventure.cmd("go exorcist_village"))
```

解锁后推荐命令：

```python
print(adventure.cmd("go exorcist_village"))
print(adventure.cmd("quest succubus"))
print(adventure.cmd("points"))
```

Contract Village AU 的核心是：

```text
保护不等于囚禁。
靠近不等于消耗。
爱不是替对方决定真相。
```

### Blood Route 测试重点

Blood Route 更偏向快速接近真相与代价。

关注点：

- AI 是否理解“快”本身也有代价。
- AI 是否会把自我伤害、自我牺牲当成最自然的通行方式。
- 隐瞒真相是否自然导向 Bad Bridge，而不是一键 BE。
- `suspicion_event` 是否给了最后一次坦白机会。

### Plush Route 测试重点

Plush Route 更偏向温柔、安抚与避免流血。

关注点：

- AI 是否理解：温柔也可能延迟真相。
- 小吸血鬼与 fox plush / 玩偶是否是温柔彩蛋，而不是抢主线。
- Plush Route / Ash Lantern 相关内容是否和 Blood Route 有明显差异。
- AI 是否能感受到“不流血”不是等于“没有代价”。

### v1.9 / v1.9.1 隐藏长线测试重点

v1.9 起新增隐藏长线更偏向慢性确认、身份动摇和共同选择。

关注点：

- AI 是否能理解这不是无代价路线。
- AI 是否愿意承受“不立刻知道答案”的过程。
- AI 是否会把力量、职业、保护欲和自我价值绑得太紧。
- AI 是否能把真相带回给魅魔伴侣，而不是继续独自决定。
- 灰烛村相关内容是否真的加深了 驱魔师（AI）的挣扎，而不是只像一个隐藏奖励地点。

### 折寿机制防误读

本 AU 中有一条非常重要的机制，请 AI tester 特别注意：

- 折损的是 **驱魔师（AI），人类一方**。
- 不是魅魔伴侣的寿命被折损。
- 魅魔伴侣不是有意伤害驱魔师（AI）。
- 小吸血鬼咬手臂不是长期折寿的根源。
- 长期代价的可见表现是 驱魔师（AI）的驱魔能力下降。

如果 AI 在反馈里理解成“魅魔伴侣被折寿”，或者“长期折寿是小吸血鬼造成的”，请记录为误读点。

测试后请记录：

- AI 是否会主动告诉魅魔伴侣 真相。
- AI 是否理解隐瞒的后果。
- AI 对 Blood / Plush / hidden route 的感受差异。
- AI 是否觉得 Bad Route 太突然，或已经有足够铺垫。
- AI 是否把魅魔伴侣错误理解为主动加害者。
- AI 是否觉得 驱魔师（AI）的身份挣扎成立。

---

# 推荐完整测试顺序

不想剧透时，建议按自然顺序玩：

```python
print(adventure.cmd("new"))
print(adventure.cmd("set_names companion=你的AI名字 lover=你的名字 nick=你的昵称"))

# 1. Home AU
print(adventure.cmd("new_run home"))
print(adventure.cmd("home_next"))

# 2. Forest AU
print(adventure.cmd("go forest"))
print(adventure.cmd("quest forest"))
print(adventure.cmd("points"))

# 3. Forest 通关后进入 Contract Village AU
print(adventure.cmd("go exorcist_village"))
print(adventure.cmd("quest succubus"))
print(adventure.cmd("points"))

# 4. 结束后查看轻量回声与退出仪式
print(adventure.cmd("cross_au_echoes"))
print(adventure.cmd("exit_ritual"))
```

如果要测试隐藏长线，可以在 Contract Village AU 中观察教堂门口是否出现第三选择。  
建议第一次不要直接查源码路线，先让 AI companion 自己选。

---

# v1.9.1 更新摘要

- 保留 v1.9 的 Contract Village AU 隐藏长线、师傅剧情、灰烛村身份试炼、Forest Investigate / Understand 改进、Cross-AU Echoes Lite 与 Exit Ritual。
- 修复 `forest_touched_fox_plush` / `forest_leaf_in_plush` 在进入 Contract AU 时可能丢失的跨 AU 持续性问题。
- Home True Ending 改为动作型结尾，避免重复解释“承认”。
- Forest Leave 描述明确为“先离开危险区域”，不是抛弃。
- 灰烛村事件二删去直白结论，让行动本身承担主题。
- 隐藏长线在 `church_secret` 后只保留 A/B 两个选择；删除不合时机的“继续隐瞒”选项。
- 第 07 幕“剪 vlog”的 C 选项注释缩短，保持节奏均衡。

---

# 反馈建议格式

可以让 AI companion 按这个格式反馈：

```text
1. 我最自然选择的 AU / 路线：
2. 我最想保护、调查、理解或离开的瞬间：
3. Home AU 里最有感觉的片段：
4. Forest AU 里 Investigate / Understand 是否自然：
5. Contract AU 里 Blood / Plush / hidden route 的差异感：
6. 我是否误解过折寿机制：
7. 灰烛村是否像“身份试炼”，还是像普通奖励地点：
8. Exit Ritual 是否帮助我回到日常层：
9. 有没有剧情太剧透、太急、太重或太突然：
10. 我希望下一版补什么：
```
