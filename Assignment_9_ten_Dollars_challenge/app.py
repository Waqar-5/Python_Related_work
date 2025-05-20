import streamlit as st

# --- OOP Classes ---

class User:
    def __init__(self, username, email, password, premium=False):
        self.username = username
        self.email = email
        self.password = password
        self.premium = premium
        self.skills_offered = []
        self.skills_wanted = []

class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Session:
    def __init__(self, teacher: User, student: User, skill: Skill, price: float):
        self.teacher = teacher
        self.student = student
        self.skill = skill
        self.price = price
        self.status = "pending"

class Payment:
    def __init__(self, session: Session):
        self.session = session
        self.completed = False

    def process_payment(self):
        # Simulate payment success
        self.completed = True

class SkillSwapApp:
    def __init__(self):
        self.users = []
        self.skills = []
        self.sessions = []
        self.current_user = None

        # Seed with some skills and users for demo
        self._seed_data()

    def _seed_data(self):
        # Add skills
        python_skill = Skill("Python", "Learn Python programming")
        guitar_skill = Skill("Guitar", "Learn guitar basics")
        cooking_skill = Skill("Cooking", "Learn to cook delicious meals")
        self.skills.extend([python_skill, guitar_skill, cooking_skill])

        # Add users
        u1 = User("Asad", "asad@example.com", "pass123", premium=True)
        u1.skills_offered.append(python_skill)
        u2 = User("Ameer", "ameer@example.com", "pass123")
        u2.skills_offered.append(guitar_skill)
        self.users.extend([u1, u2])

    # Authentication
    def signup(self, username, email, password):
        if any(u.email.lower() == email.lower() for u in self.users):
            return False, "Email already registered"
        new_user = User(username, email, password)
        self.users.append(new_user)
        return True, "Signup successful"

    def login(self, email, password):
        for user in self.users:
            if user.email.lower() == email.lower() and user.password == password:
                self.current_user = user
                return True, "Login successful"
        return False, "Invalid credentials"

    # Add skill offered by current user
    def add_skill_for_user(self, skill_name, description):
        if not self.current_user:
            return False, "Please login first"
        # Check if skill already exists globally
        skill = next((s for s in self.skills if s.name.lower() == skill_name.lower()), None)
        if not skill:
            skill = Skill(skill_name, description)
            self.skills.append(skill)
        if skill not in self.current_user.skills_offered:
            self.current_user.skills_offered.append(skill)
        return True, f"Skill '{skill_name}' added to your offered skills"

    # Book session
    def book_session(self, teacher_email, skill_name, price):
        if not self.current_user:
            return False, "Please login first"
        teacher = next((u for u in self.users if u.email.lower() == teacher_email.lower()), None)
        if not teacher:
            return False, "Teacher not found"
        skill = next((s for s in teacher.skills_offered if s.name == skill_name), None)
        if not skill:
            return False, "Skill not found for this teacher"
        session = Session(teacher, self.current_user, skill, price)
        self.sessions.append(session)
        return True, session

    # Make payment
    def make_payment(self, session: Session):
        payment = Payment(session)
        payment.process_payment()
        if payment.completed:
            session.status = "completed"
            return True, "Payment successful, session booked!"
        return False, "Payment failed"

# --- Initialize or retrieve the app instance ---

if "app" not in st.session_state:
    st.session_state.app = SkillSwapApp()

app = st.session_state.app

# --- Streamlit UI ---

st.title("🛠️ SkillSwap Hub - Learn & Teach Skills")

menu = ["Home", "Signup", "Login", "Offer Skill", "Book Session", "My Sessions", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Welcome to SkillSwap Hub! Exchange your skills with others easily.")
    st.write("Please Signup or Login to start.")

elif choice == "Signup":
    st.subheader("Create a new account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        success, msg = app.signup(username, email, password)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif choice == "Login":
    st.subheader("Login to your account")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        success, msg = app.login(email, password)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif choice == "Offer Skill":
    if not app.current_user:
        st.warning("Please login first!")
    else:
        st.subheader("Add a skill you can teach")
        skill_name = st.text_input("Skill Name")
        skill_desc = st.text_area("Skill Description")
        if st.button("Add Skill"):
            success, msg = app.add_skill_for_user(skill_name, skill_desc)
            if success:
                st.success(msg)
            else:
                st.error(msg)

        st.write("Your skills offered:")
        for sk in app.current_user.skills_offered:
            st.write(f"- {sk.name}: {sk.description}")

elif choice == "Book Session":
    if not app.current_user:
        st.warning("Please login first!")
    else:
        st.subheader("Book a learning session")
        teachers = [u for u in app.users if u != app.current_user]
        teacher_email = st.selectbox("Select teacher", [t.email for t in teachers])
        selected_teacher = next((t for t in teachers if t.email == teacher_email), None)
        if selected_teacher:
            skill_names = [s.name for s in selected_teacher.skills_offered]
            skill_name = st.selectbox("Select skill", skill_names)
            price = st.number_input("Session price ($)", min_value=1.0, max_value=500.0, value=20.0, step=1.0)
            if st.button("Book and Pay"):
                success, result = app.book_session(teacher_email, skill_name, price)
                if success:
                    session = result
                    pay_success, pay_msg = app.make_payment(session)
                    if pay_success:
                        st.success(pay_msg)
                    else:
                        st.error(pay_msg)
                else:
                    st.error(result)

elif choice == "My Sessions":
    if not app.current_user:
        st.warning("Please login first!")
    else:
        st.subheader("Your booked sessions")
        booked_sessions = [s for s in app.sessions if s.student == app.current_user]
        if booked_sessions:
            for i, sess in enumerate(booked_sessions, 1):
                st.write(f"{i}. Teacher: {sess.teacher.username}, Skill: {sess.skill.name}, Price: ${sess.price}, Status: {sess.status}")
        else:
            st.write("No sessions booked yet.")

elif choice == "Logout":
    app.current_user = None
    st.success("Logged out successfully.")
