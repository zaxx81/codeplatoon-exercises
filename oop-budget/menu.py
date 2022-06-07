def menu():
  # Strings for menu options
  menu_title = 'Title Here'
  menu_choice = 'Please enter an option: '

  menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
  }

  # Blocks to execute when menu option is chosen

  def option1():
    # Begin Option Code
    print('You chose option 1')
    # End Option Code
    return False

  def option2():
    # Begin Option Code
    print('You chose option 2')
    # End Option Code
    return False

  def option3():
    # Begin Option Code
    print('You chose option 3')
    # End Option Code
    return False

  def option_exit():
    return True

  def default():
    return f'Invalid option. Please select an option between 1-{len(switcher)}'

  # Functions to call with input option
  switcher = {
    1: option1,
    2: option2,
    3: option3,
    4: option_exit,
  }

  def switch(case):
    return switcher.get(case, default)()

  def print_menu():
    print('\n----------')
    print(menu_title)
    print('----------')
    for key in menu_options.keys():
      print(key, ' -- ', menu_options[key])

  def run():
    exit_menu = False

    while exit_menu is False:
      print_menu()    
      choice = int(input(menu_choice))
      exit_menu = switch(choice)

  run()

menu()