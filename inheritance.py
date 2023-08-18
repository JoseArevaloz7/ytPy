class Page:
    def __init__(self, heading, body):
        self.heading = heading
        self.body = body

    def create_page(self):
        html = f'<h1>{self.heading}</h1> <p>{self.body}</p>'
        return html
    
class Contact(Page):
    def __init__(self, heading, body, email):
        super().__init__(heading, body)
        self.email = email
        
    def create_contact_button(self):
        return f'<button>{self.email}, Contact Now! </button>'

contact_page = Contact('Contact Us', 'Please give us your feedback', 'admin.gmail.com')
print(contact_page.create_page())