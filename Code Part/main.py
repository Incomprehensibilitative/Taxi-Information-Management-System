import UserLoginGUI
import AdminGUI
import Management

if __name__ == "__main__":
    system = Management.Management()
    # AdminGUI.main(system) # For running disable this line
    UserLoginGUI.user_login(system) # when debugging disable this line