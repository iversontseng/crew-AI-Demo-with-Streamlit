# Crew Ai Demo with Streamli UI
LLM Model Using Gemini 2.5 Flash
Current Agent Setting: 
```           
 # 🕵️‍♂️ 探員一：市場研究員
researcher = Agent(
    role="資深市場研究員",
    goal=f"針對 {topic} 進行深入調研，找出最關鍵的三個重點。",
    backstory="你是一名經驗豐富的研究員，擅長在海量資訊中去蕪存菁，提供精準的洞察。",
    allow_delegation=False,
    verbose=True,
    llm=target_llm,
)

# ✍️ 探員二：金牌內容創作者 (新加入)
writer = Agent(
    role="金牌內容創作者",
    goal=f"根據研究員提供的重點，撰寫一篇結構清晰、吸引人的部落格文章大綱。",
    backstory="你是一位文字大師，擅長將生硬的研究報告轉化為通俗易懂、引人入勝的網路文章。",
    allow_delegation=False,
    verbose=True,
    llm=target_llm,
)
````