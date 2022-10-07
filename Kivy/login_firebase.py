import pyrebase


class Accont:
    def __init__(self):
        firebaseConfig = {
            apiKey: "AIzaSyDGswjS_rHoJCfNcqfx3K7F4bHHCweyb9k",
            authDomain: "faculdade-23fdf.firebaseapp.com",
            projectId: "faculdade-23fdf",
            storageBucket: "faculdade-23fdf.appspot.com",
            messagingSenderId: "489059144526",
            appId: "1:489059144526:web:33f9553792c8a8cc52041f",
            measurementId: "G-V9QYWNQK12"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            return True

        except:
            return False

    def sing_up(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            return True

        except:
            return False

    def reset_password(self, email):
        try:
            self.auth.send_password_reset_email(email)
            return True

        except:
            return False