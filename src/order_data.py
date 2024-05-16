class OrderData:

    user_data = [['', 'Ivanov', '12345', 'Error: First Name is required'],
                 ['Denis', '', '12345', 'Error: Last Name is required'],
                 ['Denis', 'Ivanov', '', 'Error: Postal Code is required']]

    user_data__with_valid_credential = ['Denis', 'Ivanov', '12345']
    successful_message = 'Thank you for your order!'
