# from twilio.rest import Client

# account_sid='ACcfae2225babca82f529eaa4d12f80148'
# auth_token='ac6b2d2932f4702bd8b6f72988ff5d42'
# my_phone=''

# client=Client(account_sid,auth_token)

# mess=client.messages.create(
#    body='A sample message',
#    from_='',
#    to='+919840707733'
# )

# print(mess.sid)
# # Import the required libraries
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')

# # define columns
# columns = ('first_name', 'last_name', 'email')

# tree = ttk.Treeview(root, columns=columns, show='headings')

# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')

# # generate sample data
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# # add data to the treeview
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)


# def item_selected(event):
#     print(tree.selection())
#     for selected_item in tree.selection():
        
#         item = tree.item(selected_item)
#         record = item['values']
#         print(record)
#         # show a message
#         showinfo(title='Information', message=','.join(record))


# tree.bind('<<TreeviewSelect>>', item_selected)

# tree.grid(row=0, column=0, sticky='nsew')

# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')

# # run the app
# root.mainloop()
file=open('order.txt')
print(file.readlines())
file.close()