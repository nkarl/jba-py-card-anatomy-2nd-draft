"""session module -- DO NOT USE THIS MODULE AS AN IMPORT
"""
from backend.menu import Menu


def session(this_session: bool = True):
    while this_session is True:
        accounts = dict()       # list of accounts created for this session
        interact = Menu()       # start a new interactive api object

        in_main_menu = this_session
        while in_main_menu:
            u_input = interact.main_ui()
            # first menu option:
            if u_input == '1':
                u, accounts = interact.main_create(accounts)

            # second menu option:
            elif u_input == '2':
                is_logged, u = not in_main_menu, None
                # loop back if incorrect id or pin
                while not is_logged:
                    is_logged, u = interact.main_attempt_login(accounts)
                else:
                    in_user_menu = is_logged
                    while in_user_menu:
                        u_input = interact.user_ui()
                        if u_input == '1':
                            print(f'Balance: {u.balance}\n')
                        elif u_input == '2':
                            print('You have successfully logged out!\n')
                            in_user_menu = False
                        elif u_input == '0':
                            interact.user_exit()

            # third menu option:
            elif u_input == '0':
                interact.user_exit()

            else:  # otherwise just loop back
                continue
    else:
        print(f"\nWarning: session not started because module was imported.\n")


# only execute when this module is run directly
if __name__ == "__main__":
    session(__name__ == "__main__")
else:
    session(__name__ == "__main__")
