from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")


#En el método de pago, agrega una sentencia print para ver en tu terminal que diga
# "Cobrando a [nombre del cliente] por [total] frutas"


@app.route('/checkout', methods=['POST'])         
def checkout():
    
    user_form = request.form
    
    fruit_amount =  int(user_form['apple']) + int(user_form['raspberry']) + int(user_form['strawberry']) 
    print(f"Cobrando a {user_form['first_name']} {user_form['last_name']} por {fruit_amount} frutas")
    
    return render_template("checkout.html", user_form = user_form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    