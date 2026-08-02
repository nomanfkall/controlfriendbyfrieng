import streamlit as st
import random
import time

# ========== 尝试导入自动刷新模块 ==========
try:
    from streamlit_autorefresh import st_autorefresh
    AUTOREFRESH_AVAILABLE = True
except ImportError:
    AUTOREFRESH_AVAILABLE = False
    st.warning("⚠️ `streamlit-autorefresh` 未安装，自动刷新功能已禁用。")

# ==================== 常量配置 ====================
MIN_TIMEOUT = 3.0
MAX_TIMEOUT = 12.0
MAX_MESSAGES = 20
REFRESH_INTERVAL = 1000
MOVE_INTERVAL = 2.5
SCENE_WIDTH = 600
SCENE_HEIGHT = 400
CHAR_SIZE = 30

# ==================== 角色类 ====================
class ControlFriendByFriend:
    def __init__(self, friend_name: str, friend_age: int,
                 friend_height: float, friend_weight: float):
        self.name = friend_name
        self.age = friend_age
        self.height = friend_height
        self.weight = friend_weight

    def speak(self) -> str:
        greetings = [
            f"我是{self.name}，你好啊 user!",
            f"嗨！我是{self.name}，见到你真开心！",
            f"你好呀，我是{self.name}，请多指教！",
            f"嘿嘿，我叫{self.name}，你叫什么名字呀？",
            f"哟！{self.name}在此，有何贵干？",
        ]
        age_lines = [
            f"我今年{self.age}岁了！你喜欢萝莉还是御姐呢？",
            f"我已经{self.age}岁了，时间过得好快……",
            f"年龄嘛……{self.age}岁，猜我比你大还是小？",
            f"岁月不饶人，我{self.age}岁咯～",
            f"永远{self.age}岁，永远年轻！",
        ]
        height_lines = [
            f"我有{self.height}cm 辣么高啦，不像某个没有170的谭姓男子……",
            f"身高{self.height}cm，还算满意，至少比某些人高。",
            f"我的身高是{self.height}cm，猜我有没有穿内增高？",
            f"站在我旁边，你就知道我多高了（{self.height}cm）",
            f"身高{self.height}cm，完美比例～",
        ]
        weight_lines = [
            "体重是秘密，猜对了有奖哦～",
            "我家有个体重秤，你要去给我量吗？",
            "体重……说出来怕吓到你，还是算了。",
            f"我的体重是{self.weight}kg，可别到处说！",
            "体重稳定，吃嘛嘛香～",
        ]
        return "\n".join([
            random.choice(greetings),
            random.choice(age_lines),
            random.choice(height_lines),
            random.choice(weight_lines)
        ])

    @staticmethod
    def think() -> str:
        thoughts = [
            "已思考{}秒…谭x没有1米7！".format(random.randint(2, 8)),
            "如果曹xx是gay会发生什么？",
            "人之初，性本……饿啊(摔了一跤)",
            "怎么感觉有人在看我？错觉吗……",
            "今天穿的是不是太显眼了……",
            "刚才那句话是不是说得不太对……",
            "要不要主动找user聊天呢？好纠结……",
            "房间里的那个秤好像很久没人用了……",
            "待会儿去床上躺一会儿吧。",
            "窗外的风景真不错（其实没有窗）",
        ]
        return random.choice(thoughts)

    def sleep(self) -> str:
        dreams = [
            f"从{self.age}岁长到{self.age + 10}岁要多久呢……zzZ",
            "和女神xxoo原来是这种感觉吗……快炸膛了🥵",
            "报告塔台！我已起飞！🫡",
            '"队友队友你为啥射得那么准？"\n"因为……她离开我了😭"',
            "明天吃什么好呢……zzZ",
            "ZZZ……梦到自己在数羊……ZZZ",
            "呼……呼……（打鼾声）",
        ]
        return random.choice(dreams)

    @staticmethod
    def eat() -> str:
        foods = [
            "🍔 汉堡真好吃！",
            "🍣 寿司太新鲜了！",
            "🍜 拉面汤底浓郁！",
            "🍕 披萨拉丝满分！",
            "🍛 咖喱饭绝了！",
            "🥗 轻食健康～",
        ]
        return random.choice(foods)

    @staticmethod
    def play() -> str:
        plays = [
            "🎮 来局游戏吧！",
            "⚽ 踢球去！",
            "🏀 投篮！",
            "🎵 听歌跳舞～",
            "📖 看漫画中……",
            "🧩 拼图好有趣！",
        ]
        return random.choice(plays)

# ==================== 样式 ====================
def set_pixel_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
        .pixel-font {
            font-family: 'Press Start 2P', monospace;
            color: #8BFF8B;
            text-shadow: 2px 2px 0 #000;
            line-height: 1.6;
        }
        .pixel-box {
            background-color: #1a1a2e;
            border: 4px solid #8BFF8B;
            border-radius: 0;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 6px 6px 0 #000;
            word-wrap: break-word;
        }
        .stButton>button {
            font-family: 'Press Start 2P', monospace;
            background-color: #1a1a2e;
            color: #8BFF8B;
            border: 3px solid #8BFF8B;
            border-radius: 0;
            box-shadow: 4px 4px 0 #000;
            transition: all 0.05s ease;
            white-space: normal;
            word-wrap: break-word;
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
        @media (max-width: 600px) {
            .pixel-font { font-size: 11px !important; }
            .stButton>button { font-size: 10px !important; }
        }
        .pixel-scene {
            background-color: #1a1a2e;
            border: 4px solid #8BFF8B;
            border-radius: 0;
            padding: 10px;
            margin: 10px 0;
            box-shadow: 6px 6px 0 #000;
        }
    </style>
    """, unsafe_allow_html=True)

# ==================== 初始化 ====================
def init_session():
    if "step" not in st.session_state:
        st.session_state.step = "init"
        st.session_state.friend = None
        st.session_state.messages = []
        st.session_state.last_action_time = time.time()
        st.session_state.timeout = random.uniform(MIN_TIMEOUT, MAX_TIMEOUT)
        st.session_state.char_x = SCENE_WIDTH // 2 - CHAR_SIZE // 2
        st.session_state.char_y = SCENE_HEIGHT // 2 - CHAR_SIZE // 2
        st.session_state.last_move_time = time.time()
        st.session_state.component_value = None   # 用于存放组件返回值

def init_page():
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
            st.session_state.messages = [f"🎮 欢迎，{name}！和我互动吧～"]
            st.session_state.step = "game"
            st.session_state.last_action_time = time.time()
            st.session_state.timeout = random.uniform(MIN_TIMEOUT, MAX_TIMEOUT)
            st.session_state.char_x = SCENE_WIDTH // 2 - CHAR_SIZE // 2
            st.session_state.char_y = SCENE_HEIGHT // 2 - CHAR_SIZE // 2
            st.session_state.last_move_time = time.time()
            st.rerun()

def build_scene_html(char_x, char_y, furniture):
    furniture_html = ""
    for item in furniture:
        furniture_html += f"""
        <div id="furniture-{item['id']}" 
             style="position:absolute; left:{item['x']}px; top:{item['y']}px; 
                    width:{item['width']}px; height:{item['height']}px; 
                    background-color:{item['color']}; border:2px solid #000; 
                    text-align:center; font-size:12px; color:white; 
                    cursor:pointer; user-select:none; 
                    display:flex; align-items:center; justify-content:center;
                    font-family:'Press Start 2P', monospace;">
            {item['label']}
        </div>
        """
    html = f"""
    <div id="scene-container" style="position:relative; width:{SCENE_WIDTH}px; height:{SCENE_HEIGHT}px; 
          background-color:#2d2d2d; border:4px solid #8BFF8B; image-rendering:pixelated; overflow:hidden; margin:auto;">
        <div style="position:absolute; width:100%; height:100%; background-image: 
             repeating-linear-gradient(0deg, transparent, transparent 20px, rgba(255,255,255,0.03) 20px, rgba(255,255,255,0.03) 21px), 
             repeating-linear-gradient(90deg, transparent, transparent 20px, rgba(255,255,255,0.03) 20px, rgba(255,255,255,0.03) 21px);">
        </div>
        {furniture_html}
        <div id="character" style="position:absolute; left:{char_x}px; top:{char_y}px; 
             width:{CHAR_SIZE}px; height:{CHAR_SIZE}px; 
             background-color:#FFD700; border:2px solid #000; border-radius:50%; 
             text-align:center; line-height:{CHAR_SIZE}px; font-size:20px; 
             cursor:grab; user-select:none; z-index:10;
             box-shadow: 0 0 0 2px #000, 2px 2px 0 0 #000;">
            😊
        </div>
        <div style="position:absolute; bottom:5px; left:5px; color:#8BFF8B; font-size:10px; font-family:'Press Start 2P', monospace; opacity:0.6;">
            🖱️ 拖动小人 | 点击家具互动
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/streamlit-component-lib@1.0.0/dist/streamlit-component-lib.js"></script>
    <script>
        (function() {{
            const charEl = document.getElementById('character');
            let isDragging = false;
            let offsetX = 0, offsetY = 0;
            const container = document.getElementById('scene-container');
            const charSize = {CHAR_SIZE};
            const sceneWidth = {SCENE_WIDTH};
            const sceneHeight = {SCENE_HEIGHT};
            function clamp(val, min, max) {{
                return Math.min(Math.max(val, min), max);
            }}
            function sendPosition(x, y) {{
                const data = {{ type: 'move', x: x, y: y }};
                Streamlit.setComponentValue(data);
            }}
            charEl.addEventListener('mousedown', function(e) {{
                isDragging = true;
                const rect = charEl.getBoundingClientRect();
                offsetX = e.clientX - rect.left;
                offsetY = e.clientY - rect.top;
                charEl.style.cursor = 'grabbing';
                e.preventDefault();
            }});
            document.addEventListener('mousemove', function(e) {{
                if (!isDragging) return;
                const containerRectNow = container.getBoundingClientRect();
                let newX = e.clientX - containerRectNow.left - offsetX;
                let newY = e.clientY - containerRectNow.top - offsetY;
                newX = clamp(newX, 0, sceneWidth - charSize);
                newY = clamp(newY, 0, sceneHeight - charSize);
                charEl.style.left = newX + 'px';
                charEl.style.top = newY + 'px';
                e.preventDefault();
            }});
            document.addEventListener('mouseup', function(e) {{
                if (isDragging) {{
                    isDragging = false;
                    charEl.style.cursor = 'grab';
                    const left = parseInt(charEl.style.left, 10);
                    const top = parseInt(charEl.style.top, 10);
                    if (!isNaN(left) && !isNaN(top)) {{
                        sendPosition(left, top);
                    }}
                }}
            }});
            const furnitures = document.querySelectorAll('[id^="furniture-"]');
            furnitures.forEach(function(el) {{
                el.addEventListener('click', function(e) {{
                    const id = this.id.replace('furniture-', '');
                    let eventData = {{}};
                    if (id === 'scale') {{
                        eventData = {{ type: 'weigh' }};
                    }} else if (id === 'bed') {{
                        eventData = {{ type: 'bed' }};
                    }} else if (id === 'table') {{
                        eventData = {{ type: 'table' }};
                    }} else {{
                        return;
                    }}
                    Streamlit.setComponentValue(eventData);
                }});
            }});
        }})();
    </script>
    """
    return html

def append_message(msg: str):
    st.session_state.messages.append(msg)
    if len(st.session_state.messages) > MAX_MESSAGES:
        st.session_state.messages = st.session_state.messages[-MAX_MESSAGES:]

def _reset_timer():
    st.session_state.last_action_time = time.time()
    st.session_state.timeout = random.uniform(MIN_TIMEOUT, MAX_TIMEOUT)

def game_page():
    if AUTOREFRESH_AVAILABLE:
        st_autorefresh(interval=REFRESH_INTERVAL, limit=None, key="game_refresh")
    else:
        st.caption("🔄 自动刷新不可用，请手动刷新页面（F5）查看最新状态。")

    friend = st.session_state.friend
    messages = st.session_state.messages

    # ===== 第一步：处理上次组件返回值（如果存在） =====
    if st.session_state.component_value is not None:
        data = st.session_state.component_value
        if isinstance(data, dict):
            if data.get("type") == "move":
                new_x = data.get("x")
                new_y = data.get("y")
                if new_x is not None and new_y is not None:
                    st.session_state.char_x = new_x
                    st.session_state.char_y = new_y
                    st.session_state.last_move_time = time.time()  # 重置自动移动计时
            elif data.get("type") == "weigh":
                append_message(f"⚖️ 体重秤显示：{friend.weight} kg")
            elif data.get("type") == "bed":
                append_message(f"💤 {friend.sleep()}")
            elif data.get("type") == "table":
                append_message(f"🍽️ {ControlFriendByFriend.eat()}")
        # 清空已处理
        st.session_state.component_value = None
        # 立即刷新以显示新消息或位置
        st.rerun()

    # ===== 自动移动 =====
    now = time.time()
    if now - st.session_state.last_move_time >= MOVE_INTERVAL:
        dx = random.randint(-8, 8)
        dy = random.randint(-8, 8)
        new_x = st.session_state.char_x + dx
        new_y = st.session_state.char_y + dy
        new_x = max(0, min(SCENE_WIDTH - CHAR_SIZE, new_x))
        new_y = max(0, min(SCENE_HEIGHT - CHAR_SIZE, new_y))
        st.session_state.char_x = new_x
        st.session_state.char_y = new_y
        st.session_state.last_move_time = now

    # ===== 自动思考 =====
    elapsed = now - st.session_state.last_action_time
    if elapsed >= st.session_state.timeout:
        append_message(f"🤔 {ControlFriendByFriend.think()}")
        st.session_state.last_action_time = now
        st.session_state.timeout = random.uniform(MIN_TIMEOUT, MAX_TIMEOUT)

    # ===== 界面布局 =====
    st.markdown(f"""
    <div class='pixel-box'>
        <div class='pixel-font' style='font-size:16px;'>
            👤 {friend.name} &nbsp;|&nbsp; 🎂 {friend.age}岁 &nbsp;|&nbsp; 📏 {friend.height}cm &nbsp;|&nbsp; ⚖️ {friend.weight}kg
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 房屋场景
    st.markdown("<div class='pixel-scene'>", unsafe_allow_html=True)
    furniture = [
        {"id": "table", "x": 30, "y": 30, "width": 60, "height": 60, "color": "#8B4513", "label": "桌子"},
        {"id": "bed", "x": 450, "y": 280, "width": 100, "height": 60, "color": "#A52A2A", "label": "床"},
        {"id": "scale", "x": 250, "y": 320, "width": 50, "height": 50, "color": "#C0C0C0", "label": "秤"},
    ]
    scene_html = build_scene_html(st.session_state.char_x, st.session_state.char_y, furniture)
    result = st.components.v1.html(scene_html, height=SCENE_HEIGHT + 30, scrolling=False)

    # ===== 第二步：保存组件返回值，供下次运行处理 =====
    if result is not None:
        st.session_state.component_value = result

    st.markdown("</div>", unsafe_allow_html=True)

    # 消息记录
    st.markdown("<div class='pixel-box'>", unsafe_allow_html=True)
    for msg in messages:
        msg_formatted = msg.replace("\n", "<br>")
        st.markdown(f"<div class='pixel-font' style='font-size:14px;'>{msg_formatted}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 倒计时进度条
    remaining = max(0.0, st.session_state.timeout - elapsed)
    progress = min(1.0, elapsed / st.session_state.timeout) if st.session_state.timeout > 0 else 0.0
    st.progress(progress, text=f"⏳ 下次自动思考倒计时 {remaining:.1f} 秒")

    # 操作按钮
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("💬 聊天", use_container_width=True):
            append_message(f"💬 {friend.speak()}")
            _reset_timer()
            st.rerun()
    with col2:
        if st.button("💤 睡觉", use_container_width=True):
            append_message(f"💤 {friend.sleep()}")
            _reset_timer()
            st.rerun()
    with col3:
        if st.button("🍽️ 吃饭", use_container_width=True):
            append_message(f"🍽️ {ControlFriendByFriend.eat()}")
            _reset_timer()
            st.rerun()
    with col4:
        if st.button("🎮 玩耍", use_container_width=True):
            append_message(f"🎮 {ControlFriendByFriend.play()}")
            _reset_timer()
            st.rerun()
    with col5:
        if st.button("🚪 退出", use_container_width=True):
            append_message("👋 游戏结束，再见！")
            st.session_state.step = "init"
            st.rerun()

    st.caption("🎮 点击按钮互动，超时将自动触发随机思考。拖动小人走动，点击家具触发事件。")

# ==================== 主入口 ====================
def main():
    set_pixel_style()
    init_session()
    if st.session_state.step == "init":
        init_page()
    else:
        game_page()

if __name__ == "__main__":
    main()