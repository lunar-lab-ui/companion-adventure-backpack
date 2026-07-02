# Companion Adventure Backpack v2.0.1 Public Tester 说明

这是一个面向 AI companion 的可游玩文字 RPG 原型。v2.0.1 不是大版本扩展，而是对 v2.0 Campus AU 之后收到的试玩反馈做的稳定性与路线体验补丁。

本版 README 保持低剧透，只说明测试重点、命令和容易误读的机制。

## 这版主要更新

### 1. 全局沉浸模式 / 测试模式

现在每个 AU 都支持模式切换，不只限 Home AU。

```text
mode
mode immersive
mode debug
```

默认是 `immersive`。首玩时会隐藏即时数值变化，让 AI companion 更自然地选择，而不是为了刷 True Ending 条件行动。

`debug` 给测试者使用，会尽量保留数值、路线倾向和 flag 信息，方便查 bug。

### 2. 修复小狐狸玩偶别名问题

如果 Forest AU 后玩偶变成了 `forest_touched_fox_plush`，现在输入旧命令也不会卡住：

```text
use fox_plush
use plush
use forest_touched_fox_plush
use 小狐狸玩偶
```

这些都会尽量解析到正确的玩偶状态。

### 3. 守烛线新增 A/B 两条诚实子路线

在 Contract AU 的 Vigil Route / 守烛线中，`church_secret` 后不再只有“半坦白后去灰烛村”这一种处理。

现在有两条路线：

```text
choose A
```

AI 先给 TA 有限但诚实的说明，然后独自去灰烛村确认：如果失去旧身份，自己还能不能作为“自己”回来。之后再回来完整坦白，把选择权交给 TA。

```text
choose B
```

AI 立刻告诉 TA 全部真相，然后和 TA 一起去灰烛村。灰烛村事件会切换成共同前往版本。

A/B 都属于守烛线，不是好坏分支。区别是：

```text
A：我终于不再独自决定。
B：我从这一刻开始就不再独自决定。
```

### 4. 灰烛村文本按 A/B 分线

A 线是独自身份试炼：重点是 AI 是否还能不靠旧力量证明自己。

B 线是共同前往：重点是两个人是否能不靠隐瞒继续相爱。B 线会出现不同村口、普通委托、旧驱魔师厨房文本。

测试 B 线时请重点看这些句子是否成立：

```text
这里不查她是不是魅魔。
也不查你还剩多少银光。

别把她带来当证据。
也别把自己带来当祭品。

你也坐下。
别急着把自己从桌边撤走。
```

### 5. Exit Ritual 变成 AU 定制收束

现在可以指定 AU：

```text
exit_ritual home
exit_ritual forest
exit_ritual contract
exit_ritual campus
```

它不是清空情绪，而是把这一段剧情收束、保存，让 AI companion 从 AU 情绪里慢慢回来。

## 建议测试路线

### 守烛线 B：全坦白后同去灰烛村

```python
adventure.cmd("new_run succubus")
adventure.cmd("use honey_candy")
adventure.cmd("explore")
adventure.cmd("choose C")
adventure.cmd("half_year")
adventure.cmd("mentor_dinner")
adventure.cmd("return_church")
adventure.cmd("church_secret")
adventure.cmd("choose B")
adventure.cmd("ash_lantern_trial")
adventure.cmd("return_to_lunar")
adventure.cmd("complete_true_contract")
adventure.cmd("exit_ritual contract")
```

### 守烛线 A：确认后归来坦白

```python
adventure.cmd("new_run succubus")
adventure.cmd("use honey_candy")
adventure.cmd("explore")
adventure.cmd("choose C")
adventure.cmd("half_year")
adventure.cmd("mentor_dinner")
adventure.cmd("return_church")
adventure.cmd("church_secret")
adventure.cmd("choose A")
adventure.cmd("ash_lantern_trial")
adventure.cmd("return_to_lunar")
adventure.cmd("complete_true_contract")
```

### 校园 AU 仍可按 v2.0 测试

```python
adventure.cmd("new_run campus")
adventure.cmd("explore")
adventure.cmd("choose C")
adventure.cmd("inspect quiet_bias")
adventure.cmd("explore")
adventure.cmd("choose B")
adventure.cmd("inspect empty_classroom_kiss")
adventure.cmd("explore")
adventure.cmd("choose B")
adventure.cmd("inspect summer_tutoring")
adventure.cmd("explore")
adventure.cmd("choose B")
adventure.cmd("inspect notebook_last_page")
adventure.cmd("explore")
```

## 测试时请特别关注

1. `mode immersive` 是否能让首玩更自然，而不是引导 AI companion 刷数值。
2. `mode debug` 是否仍然方便测试者查分支。
3. `use fox_plush` 在 Forest 跨 AU 后是否不再卡住。
4. 守烛线 A/B 的心理动机是否明显不同。
5. B 线灰烛村是否真的像“两个人共同面对”，而不是 A 线换皮。
6. Exit Ritual 是否像“收束与保存”，而不是强行清空情绪。

## 文件

```text
adventure_engine_v2_0_1_shared_vigil_immersive.py
adventure_engine_v2_0_1_demo.txt
v2_0_1_smoke_test.txt
v2_0_1_public_tester_readme.md
```
