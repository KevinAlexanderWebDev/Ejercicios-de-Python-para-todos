"""5. Caso avanzado: Herencia vs Composición

Crea una clase Usuario con nombre y email.
Crea una clase CuentaBancaria que tenga un saldo y un objeto Usuario dentro.
Muestra cómo acceder a los datos del usuario desde la cuenta.

👉 Pregunta de reflexión: ¿por qué aquí no conviene que CuentaBancaria herede de Usuario?"""

class User: 
    def __init__(self, name, email):
        self.name= name
        self.email= email
        
class BankAccount:
    def __init__(self, balance, user):
        self.__balance= balance
        self.user= user
        
    def show_user(self):
        print("This is the user's data: ")
        print(f"Username: {self.user.name} - User_Email: {self.user.email} - User_Balance: ${self.__balance} dllrs.")

user_name= input("Insert your user name: ").strip().replace(" ", "")

user_email= input("Insert your user email: ").strip().replace(" ", "")
        
name= User(user_name, user_email)

user_account= BankAccount(4000, name)

user_account.show_user()
        