class MainPageLocators:
    # кнопка "личный кабинет"
    my_profile_button = '//*[@id="root"]/div/header/nav/a'
    bun_section = '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]'
    constructor_logo = '//*[@id="root"]/div/header/nav/ul/li[1]/a'


class LoginPageLocators:
    email_input = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    password_input = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    login_button = '//*[@id="root"]/div/main/div/form/button'
    restore_password_button = '//*[@id="root"]/div/main/div/div/p[2]/a'
    login_header = '//*[@id="root"]/div/main/div/h2'


class ProfilePageLocators:
    profile_button = '//*[@id="root"]/div/main/div/nav/ul/li[1]/a'
    logout_button = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'


class PasswordRecoveryPageLocators:
    login_button = '//*[@id="root"]/div/main/div/div/p/a'


class SignUpPageLocators:
    name_input = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    email_input = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    password_input = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    sign_up_button = '//*[@id="root"]/div/main/div/form/button'
    user_already_exists_notification = '//*[@id="root"]/div/main/div/p'
