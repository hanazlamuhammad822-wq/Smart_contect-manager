def organize_contacts(contact_list):
    
    def validate_email(contact):
        # Email clean karo
        if '@' in contact['email'] and '.' in contact['email']:
            clean_email = contact['email'].lower().strip()
            return clean_email
        return None
    
    def validate_phone(contact):
        # Sirf digits rakho
        clean_phone = ''.join(filter(str.isdigit, contact['phone']))
        if clean_phone:
            return clean_phone
        return None
    
    # Har contact process karo
    for contact in contact_list:
        # Email validate karo
        email = validate_email(contact)
        if email:
            contact['email'] = email
        
        # Phone validate karo
        phone = validate_phone(contact)
        if phone:
            contact['phone'] = phone
    
    return contact_list

# Test
contacts = [
    {"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"},
    {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"},
    {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}
]

result = organize_contacts(contacts)
print(result)
