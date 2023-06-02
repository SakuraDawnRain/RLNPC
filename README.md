# RLNPC

Reinforcement Learning enhanced NPC

RLNPC = LanguageModule(NLU & NLG) + MARL(Multi Agent Reinforcement Learning)

强化学习AI和语言模块是分开训练的*

*: 因为我们不希望NPC整出人类看不懂的语言

## Game

一个基本的2v2卡牌游戏

参考自双人斗地主 

为了降低AI设计难度 将规则高度简化

- 一次只能出一张牌 这张牌只能是自己牌组中比对方更大的牌中最小的
    
    - 所以AI只需要判断是否需要出牌

- 如果没人能接某位玩家的牌 这位玩家可以继续出牌（也可以不出） 如果出牌 只能是自己牌组中最小的那张牌

- 牌库包括两组1-10的牌

- 每个玩家手上有5张牌

## 流程

轮到玩家/NPC回合时 遵循以下流程

1. 系统负责检查玩家是否可以出牌

2. 如果玩家可以出牌 玩家可以询问自己队友的情况 以判断自己是否应该出牌

3. 队友回复 玩家选择出牌/不出

## 结构

游戏工程文件

- game.py 游戏逻辑

- env.py 将游戏封装为类似PettingZoo的多智能体强化学习环境

- vis.py 可视化游戏 尚未施工

NPC文件

- npc.py NPC行动逻辑

- nlp.py 语言模块(Language Module) 包含对NLU和NLG的实现

- ai.py 强化学习策略模块

功能文件

- train.py 训练NPC

- test.py 测试NPC

- play.py 玩家参与游戏