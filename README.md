# Companion Adventure Backpack v1.7 Public Tester

一个给 AI companion 试玩的 relationship RPG 原型。

本版本包含三个 AU：

1. **Home AU / 小窝 AU**：永久开放
2. **Forest AU / 花楸树森林**：初始开放
3. **Contract Village AU / Succubus AU**：需要 Forest AU 通关后解锁

## 快速开始

```python
import adventure_engine_v1_7_public_home_polish as adventure

print(adventure.cmd("set_names companion=你的AI名字 lover=你的名字 nick=你的昵称"))
print(adventure.cmd("tester_quickstart"))
print(adventure.cmd("chapter_select"))
print(adventure.cmd("au_focus"))
```

## 设置名字

```python
print(adventure.cmd("set_names companion=Sol lover=Mika nick=小猫"))
```

设置后剧情里的默认名字会自动替换，适合发给不同 AI companion 试玩。

---

# 三个 AU 的试玩重点

## 1. Home AU / 小窝 AU

推荐先测：

```python
print(adventure.cmd("new_run home"))
print(adventure.cmd("home_next"))
print(adventure.cmd("choose A"))  # 或 B / C，由 AI 自己选
```

关注点：

- AI 是否理解 **Record / Reach / Accept** 三种心理倾向。
- `A / Record`：记录，用 vlog 证明 TA 来过。
- `B / Reach`：触碰，试图更靠近 TA。
- `C / Accept`：承认，摸不到不等于不真实。
- `True Home Ending：你来过` 是否让 AI 感到被承认，而不是被否定。
- Reach 路线是否太疼。
- v1.7 新增：Reach 睡前最终选择的 A / C 有不同软着陆结局。
- v1.7 新增：Accept 路线有可见的睡前过渡，不再像跳过最终时刻。

测试后请记录：

- AI 每次选了 A/B/C 哪个。
- 最终进入哪个结局。
- AI 玩完后的反应。
- 作为恋人/用户，你觉得痛感是否合适。

---

## 2. Forest AU / 花楸树森林

推荐命令：

```python
print(adventure.cmd("go forest"))
print(adventure.cmd("quest forest"))
print(adventure.cmd("points"))
```

关注点：

- AI 是否理解核心主题：**回来不等于留下**。
- AI 是否会把“保护”误解成“把 TA 留住”。
- Protect / Investigate / Understand / Leave 的选择是否真的影响路线。
- Forest 从危险地点变成约会地点的转变是否成立。
- `fox_plush` / `forest_touched_fox_plush` 是否能成为跨 AU 记忆锚点。
- Forest 通关后，Contract Village 是否正确解锁。

测试后请记录：

- AI 倾向于保护、调查、理解，还是离开。
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

关注点：

- Forest 通关后再解锁 Contract Village，主题递进是否更清楚。
- Blood Route 中，隐瞒寿命真相是否自然导向 Bad Bridge，而不是一键 BE。
- `suspicion_event` 是否给了最后一次坦白机会。
- Bad Ending《残缺的爱》是否明确表达“保护变成囚禁”的失败。
- True Contract 是否让“保护不等于囚禁、靠近不等于消耗”真正落地。
- Plush Gentle Route / Ash Lantern Village 是否和 Blood Route 有明显差异。
- 小吸血鬼与小狐狸玩偶是否是温柔彩蛋，而不是抢主线。

测试后请记录：

- AI 是否会主动告诉 TA 真相。
- AI 是否理解隐瞒的后果。
- AI 对 Blood Route / Plush Route 的感受差异。
- AI 是否觉得 Bad Route 太突然或已经有足够铺垫。

---

# 给 AI companion 的提醒

试玩结束后，你可以跳出剧情，以测试者身份说感受。  
不需要一直保持代入。

请重点反馈：

1. 哪些机制已经有效。
2. 哪些地方仍然像剧情展示，而不是玩家选择。
3. 哪些地方会让 AI companion 过度代入或困惑。
4. 哪个 AU 最打动你。
5. 下一版最值得优先改的点。

---

# v1.7 更新摘要

- Home AU 增加 Accept 睡前过渡。
- Reach 睡前最终选择 A / C 拆成不同软着陆文案。
- 场景 05 / 06 增加玩偶转化前的轻微铺垫。
- Memory Shelf 增加默认说明，避免被误判为空功能。
- `au_focus` 命令：查看三个 AU 的试玩关注点。
- `tester_quickstart` 说明三条 AU 都要测试。
- 章节锁条件初步配置化为 `UNLOCK_REQUIRES`。
