import streamlit as st
import random
import time

# ---------- 你的原始类（稍作调整，增加返回字符串而非直接打印）----------
class ControlFriendByFriend:
    def __init__(self, friend_name, friend_age, friend_height, friend_weight):
        self.name = friend_name
        self.age = friend_age
        self.height = friend_height
        self.weight = friend_weight

    def speak(self):
        greetings = [
            f"我的是{self.name}，你好啊user!",
            f"嗨！我是{self.name}，见到你真开心！",
            f"你好呀，我是{self.name}，请多指教！"
        ]
        age_lines = [
            f"我今年{self.age}岁了！啊！对了，你是喜欢萝莉一点还是御姐一点呢？像我这样的年龄你会不会嫌老啊......",
            f"我已经{self.age}岁了，感觉时间过得好快……你猜我是不是在装嫩？",
            f"年龄嘛……{self.age}岁，反正比你大还是小你猜？"
        ]
        height_lines = [
            f"我现在有{self.height}辣么高啦，不像某个没有170cm的谭姓男子啦......",
            f"我身高{self.height}，其实还算满意啦，至少比某些人高。",
            f"我的身高是{self.height}，你猜我有没有穿内增高？"
        ]
        weight_lines = [
            "我并不知道自己的体重，不过好像我家有个体重称，你要去给我量吗？",
            "体重是秘密，不过你可以猜猜看，猜对了有奖哦。",
            "我的体重……嗯，说出来怕吓到你，还是不说了。"
        ]
        # 返回拼接的字符串，便于显示
        return f"{random.choice(greetings)}\n{random.choice(age_lines)}\n{random.choice(height_lines)}\n{random.choice(weight_lines)}"

    def think(self):
        think_lines = [
            f"(已思考{self.age}秒)谭x没有1m7",
            f"我在想……如果曹xx是gay会发生什么呢？",
            "人之初,性本......饿啊(摔了一跤)",
            "怎么感觉有人在看我？错觉吗……",
            "我今天穿的衣服是不是太显眼了……",
            "刚才那句话是不是说得不太对……好纠结。"
        ]
        return random.choice(think_lines)

    def sleep(self):
        sleep_lines = [
            f"从{self.age}长到{self.age + 10}要多久呢......zzZ",
            "和女神xxoo原来是这中感觉吗......快炸膛了🥵",
            "报告塔台！我已起飞！🫡",
            f'"队友队友你为是么射的那么准？"\n"因为......她离开我了😭😭😭"'
        ]
        return random.choice(sleep_lines)


# ---------- Streamlit 页面配置 ----------
st.set_page_config(page_title="像素朋友", page_icon="🎮", layout="centered")

# 像素风格 CSS（复古游戏感）
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    .pixel-font {
        font-family: 'Press Start 2P', monospace;
        color: #8BFF8B;
        text-shadow: 2px 2px 0 #000;
    }
    .pixel-box {
        background-color: #1a1a2e;
        border: 4px solid #8BFF8B;
        border-radius: 0;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 6px 6px 0 #000;
    }
    .stButton>button {
        font-family: 'Press Start 2P', monospace;
        background-color: #1a1a2e;
        color: #8BFF8B;
        border: 3px solid #8BFF8B;
        border-radius: 0;
        box-shadow: 4px 4px 0 #000;
        transition: all 0.05s ease;
    }
    .stButton>button:hover {
        background-color: #8BFF8B;
        color: #1a1a2e;
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0 #000;
    }
    .stProgress > div > div {
        background-color: #8BFF8B !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- 初始化会话状态 ----------
if "friend" not in st.session_state:
    # 第一次运行，让用户输入角色信息
    st.session_state.step = "init"  # init / game
    st.session_state.friend = None
    st.session_state.messages = []   # 存储消息记录
    st.session_state.timer_start = None
    st.session_state.timeout = None
    st.session_state.thinking_triggered = False

# ---------- 初始化页面 ----------
if st.session_state.step == "init":
    st.markdown("<h1 class='pixel-font'>🎮 创建你的像素朋友</h1>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("名字", value="小美")
            age = st.number_input("年龄", min_value=1, max_value=120, value=22, step=1)
        with col2:
            height = st.number_input("身高 (cm)", min_value=50.0, max_value=250.0, value=165.0, step=0.5)
            weight = st.number_input("体重 (kg)", min_value=20.0, max_value=300.0, value=50.0, step=0.5)
        if st.button("🎮 开始游戏", use_container_width=True):
            st.session_state.friend = ControlFriendByFriend(name, age, height, weight)
            st.session_state.messages = [f"🎮 欢迎，{name}！请选择操作："]
            st.session_state.step = "game"
            # 设置初始计时器
            st.session_state.timer_start = time.time()
            st.session_state.timeout = random.uniform(1, 10)
            st.session_state.thinking_triggered = False
            st.rerun()
else:
    # ---------- 游戏主界面 ----------
    friend = st.session_state.friend
    messages = st.session_state.messages

    # 显示角色信息（像素风格）
    st.markdown(f"""
    <div class='pixel-box'>
        <div class='pixel-font' style='font-size:18px;'>
            👤 {friend.name} &nbsp;|&nbsp; 🎂 {friend.age}岁 &nbsp;|&nbsp; 📏 {friend.height}cm &nbsp;|&nbsp; ⚖️ {friend.weight}kg
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 消息显示区（像素风格）
    st.markdown("<div class='pixel-box'>", unsafe_allow_html=True)
    for msg in messages:
        st.markdown(f"<div class='pixel-font' style='font-size:14px;'>{msg}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- 计时器逻辑（超时触发思考）----------
    # 只有在没有触发思考且游戏进行中时，才检查超时
    if not st.session_state.thinking_triggered:
        elapsed = time.time() - st.session_state.timer_start
        if elapsed >= st.session_state.timeout:
            # 超时！执行思考，并重置计时器
            think_msg = friend.think()
            messages.append(f"🤔 {think_msg}")
            st.session_state.thinking_triggered = True  # 防止重复触发
            # 重新设定计时器（等待下次操作）
            st.session_state.timer_start = time.time()
            st.session_state.timeout = random.uniform(1, 10)
            st.session_state.thinking_triggered = False
            st.rerun()   # 刷新页面显示新消息

    # 显示倒计时进度条（像素感觉）
    if st.session_state.timer_start and not st.session_state.thinking_triggered:
        elapsed = time.time() - st.session_state.timer_start
        remaining = max(0, st.session_state.timeout - elapsed)
        progress = 1 - (remaining / st.session_state.timeout)
        st.progress(min(progress, 1.0), text=f"⏳ 剩余 {remaining:.1f} 秒")
    else:
        st.progress(0.0, text="⏳ 等待操作...")

    # ---------- 操作按钮 ----------
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💬 聊天 (t)", use_container_width=True):
            # 用户触发聊天
            speak_msg = friend.speak()
            messages.append(f"💬 {speak_msg}")
            # 重置计时器（准备下一轮）
            st.session_state.timer_start = time.time()
            st.session_state.timeout = random.uniform(1, 10)
            st.session_state.thinking_triggered = False
            st.rerun()
    with col2:
        if st.button("💤 睡觉 (s)", use_container_width=True):
            sleep_msg = friend.sleep()
            messages.append(f"💤 {sleep_msg}")
            st.session_state.timer_start = time.time()
            st.session_state.timeout = random.uniform(1, 10)
            st.session_state.thinking_triggered = False
            st.rerun()
    with col3:
        if st.button("🚪 退出 (q)", use_container_width=True):
            messages.append("👋 游戏结束，再见！")
            st.session_state.step = "init"
            st.rerun()

    # 底部提示
    st.caption("🎮 点击按钮操作，超时自动思考～")