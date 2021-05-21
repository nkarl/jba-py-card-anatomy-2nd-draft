"""session module
"""
from backend.menu import Menu

# start a new session:
def session():
    this_session = True
    while this_session is True:
        accounts = dict()       # list of accounts created for this session
        interact = Menu()    # start a new interactive api object

        in_main_menu = True
        # while in main menu
        while in_main_menu:
            u_input = interact.main_ui()

            if u_input == '1':
                u, accounts = interact.main_create(accounts)

            elif u_input == '2':
                is_logged, u = False, None

                # loop back if incorrect id or pin
                while not is_logged:
                    is_logged, u = interact.main_attempt_login(accounts)

                # otherwise, log in:
                else:
                    in_user_menu = True
                    # while logged in
                    while in_user_menu:
                        u_input = interact.user_ui()
                        if u_input == '1':
                            print(f'Balance: {u.balance}\n')
                        elif u_input == '2':
                            print('You have successfully logged out!\n')
                            in_user_menu = False
                        elif u_input == '0':
                            interact.user_exit()

            elif u_input == '0':
                interact.user_exit()


if __name__ == "__main__":
    session()
