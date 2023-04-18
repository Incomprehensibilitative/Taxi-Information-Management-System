from GUI import AdminLoginGUI
import Management

if __name__ == "__main__":
    system = Management.Management()
    AdminLoginGUI.user_login(system)
