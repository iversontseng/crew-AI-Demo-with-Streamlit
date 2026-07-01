import os
import streamlit as st
from crewai import Agent, Crew, Process, Task

# --- 1. 網頁外殼設定 ---
st.set_page_config(page_title="CrewAI 輕量 Demo", layout="centered")
st.title("🤖 CrewAI + Streamlit (Gemini 雙探員完全體)")
st.write("純內建環境 + Gemini 免費算力，輕量化 AI 團隊。")

gemini_api_key = st.sidebar.text_input(
    "請輸入您的 Gemini API Key (AIzaSy...)", type="password"
)
topic = st.text_input("你想讓 AI 團隊研究什麼主題？", "2026年 AI 發展趨勢")

# --- 2. 按鈕觸發邏輯 ---
if st.button("啟動 AI 團隊協作任務"):
    if not gemini_api_key:
        st.error("❌ 錯誤：請先在左側欄位輸入 Gemini API Key！")
    else:
        with st.spinner("🤖 AI 團隊正在密集討論與撰寫中，請稍候..."):

            # 設定環境變數
            os.environ["GEMINI_API_KEY"] = gemini_api_key
            
            # 使用我們測試成功的 Gemini 模型字串
            target_llm = "gemini/gemini-2.5-flash"

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

            # 📋 任務一：研究摘要
            task_research = Task(
                description=f"研究 {topic} 並列出三個最值得關注的核心概念。",
                expected_output="三個核心概念的條列式摘要。",
                agent=researcher,
            )

            # 📋 任務二：撰寫大綱 (新加入)
            task_write = Task(
                description=f"根據研究摘要，規劃出一份包含前言、內文重點與結論的部落格大綱。",
                expected_output="一份美觀的 Markdown 格式部落格大綱。",
                agent=writer,
            )

            # 🤝 組裝團隊：把兩隻探員、兩個任務都放進去
            my_crew = Crew(
                agents=[researcher, writer],
                tasks=[task_research, task_write],
                process=Process.sequential,  # 順序執行：研究完再寫作
                verbose=True,
            )

            # 執行完整工作流
            result = my_crew.kickoff()

        # --- 3. 畫面輸出 ---
        st.success("✨ 團隊任務完全成功！")
        st.subheader("📝 最終產出的部落格文章大綱：")
        st.markdown(result.raw)  # Streamlit 會把 Markdown 渲染得非常漂亮