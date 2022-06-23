class Employee:
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    
    def __init__(self,name,email):

        self.name = name
        self._email = email
        domain = email[email.find('@')+1 : ]
        Employee.domains.add(domain)
   
    def display(self):
        print(self.name, self.email)
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,new_email):
        domain = new_email[new_email.find('@')+1 : ]
        if domain not in Employee.allowed_domains:
            raise RuntimeError(f'Domain {domain} is not allowed')
        else:
            self._email = new_email
    
        
e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@xmail.com')
e5.display()
 
e4.email = 'ted@ymail.com'
e4.display()
 
e3.email = 'jill@gmail.com'
e3.display()